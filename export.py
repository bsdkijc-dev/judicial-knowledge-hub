#!/usr/bin/env python3
"""Export the Judicial Knowledge Hub wiki (all main-namespace pages) to Markdown.
Author of the wiki content: Cecep Mustafa (IJC), ORCID 0000-0003-0037-497X. Licence: CC BY-SA 4.0."""
import json, os, re, subprocess, sys, time, hashlib, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

API = "https://judicialknowledge.miraheze.org/w/api.php"
SITE = "https://judicialknowledge.miraheze.org/wiki/"
UA = {"User-Agent": "judicial-knowledge-hub-export/1.0 (bsdkijc-dev; contact via GitHub)"}
ORCID = "0000-0003-0037-497X"

def get(params):
    params = dict(params, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + attempt * 3)
    raise SystemExit("API failed: " + url)

# Redactions agreed with the owner (2026-11-21)
EXAMPLES = [  # realistic-looking example case numbers -> fictional placeholders (same mapping as Kaggle)
    (r"45/Pid\.Sus/2026/PN\.Jkt\.Pst", "CONTOH-01/Pid.Sus/2026/PN.CONTOH"),
    (r"78/Pid\.B/2026/PN\.Bdg", "CONTOH-04/Pid.B/2026/PN.CONTOH"),
    (r"315 K/Pdt\.Sus-Pailit/2026", "CONTOH-07 K/Pdt.Sus-Pailit/2026"),
    (r"142 K/Pid\.Sus/2026", "CONTOH-06 K/Pid.Sus/2026"),
    (r"89 K/Pid\.Sus/2026", "CONTOH-03 K/Pid.Sus/2026"),
    (r"54 K/TUN/2026", "CONTOH-08 K/TUN/2026"),
    (r"112/Pid\.Sus/2026", "CONTOH-02/Pid.Sus/2026"),
    (r"204/Pid\.Sus/2026", "CONTOH-05/Pid.Sus/2026"),
]
def clean(text, title=""):
    from anon import anonymise
    n = {"nik": 0, "case": 0}
    text = re.sub(r"(?<!\d)\d{16}(?!\d)", "[NIK REMOVED]", text)
    for pat, rep in EXAMPLES:
        text, k = re.subn(r"(?<![\w-])" + pat, rep, text)
    # count markers, so the counts are right whether or not the input was already cleaned
    n["nik"] = text.count("[NIK REMOVED]")
    n["case"] = len(re.findall(r"CONTOH-0[1-8]", text))
    text, a = anonymise(title, text)
    n.update(a)
    return text, n

def slug(title, used):
    s = re.sub(r"[^\w\-. ]+", "-", title, flags=re.UNICODE).strip(" .-")
    s = re.sub(r"\s+", "_", s)[:120] or "page"
    base, i = s, 2
    while s.lower() in used:
        s = f"{base}_{i}"; i += 1
    used.add(s.lower())
    return s

def to_md(wikitext):
    try:
        p = subprocess.run(["pandoc", "-f", "mediawiki", "-t", "gfm", "--wrap=none"],
                           input=wikitext.encode(), capture_output=True, timeout=120)
        if p.returncode == 0:
            return p.stdout.decode(), True
    except Exception:
        pass
    return "```mediawiki\n" + wikitext.replace("```", "ˋˋˋ") + "\n```\n", False

def main():
    import gzip
    if os.path.exists("source_pages.jsonl.gz"):
        recs = [json.loads(l) for l in gzip.open("source_pages.jsonl.gz", "rt", encoding="utf-8")]
        for r in recs:
            r.pop("sha256", None)
        print("pages loaded from source_pages.jsonl.gz:", len(recs), flush=True)
    elif os.path.exists("data/pages.jsonl"):
        # re-run on the previous export (already cleaned of NIKs and example case numbers)
        recs = [{k: r[k] for k in ("pageid", "title", "revision_id", "last_edited", "wikitext")}
                for r in map(json.loads, open("data/pages.jsonl", encoding="utf-8"))]
        print("pages loaded from data/pages.jsonl:", len(recs), flush=True)
    else:
        recs = fetch_all()
    finish(recs)

def fetch_all():
    pages, cont = [], {}
    while True:
        j = get({"action": "query", "list": "allpages", "apnamespace": 0, "aplimit": 500, **cont})
        pages += j["query"]["allpages"]
        if "continue" not in j: break
        cont = {"apcontinue": j["continue"]["apcontinue"]}
    print("pages listed:", len(pages), flush=True)
    recs = []
    ids = [p["pageid"] for p in pages]
    for i in range(0, len(ids), 50):
        j = get({"action": "query", "prop": "revisions", "rvprop": "content|timestamp|ids",
                 "rvslots": "main", "pageids": "|".join(map(str, ids[i:i+50]))})
        for p in j["query"]["pages"]:
            rev = p["revisions"][0]
            recs.append({"pageid": p["pageid"], "title": p["title"], "revision_id": rev["revid"],
                         "last_edited": rev["timestamp"], "wikitext": rev["slots"]["main"]["content"]})
    return recs

def finish(recs):
    from anon_map import EXCLUDE_TITLES
    recs = [r for r in recs if r["title"] not in EXCLUDE_TITLES]
    recs.sort(key=lambda r: r["title"].lower())
    print("pages:", len(recs), flush=True)
    used, tot = set(), {"nik": 0, "case": 0, "emails": 0, "names": 0, "details": 0}
    for r in recs:
        r["wikitext"], n = clean(r["wikitext"], r["title"])
        r["redactions"] = n
        for k in tot: tot[k] += n[k]
        r["url"] = SITE + urllib.parse.quote(r["title"].replace(" ", "_"))
        r["file"] = "pages/" + slug(r["title"], used) + ".md"
        r["sha256"] = hashlib.sha256(r["wikitext"].encode()).hexdigest()
    os.makedirs("pages", exist_ok=True); os.makedirs("data", exist_ok=True)
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        mds = list(ex.map(lambda r: to_md(r["wikitext"]), recs))
    t2f = {r["title"]: os.path.basename(r["file"]) for r in recs}
    def fix_links(md):
        def rep(m):
            tgt = urllib.parse.unquote(m.group(1)).replace("_", " ")
            page, _, anchor = tgt.partition("#")
            page = page[:1].upper() + page[1:]
            if page in t2f:
                return "](" + urllib.parse.quote(t2f[page]) + ")"
            return "](" + SITE + urllib.parse.quote(tgt.replace(" ", "_"), safe="#/:") + ")"
        return re.sub(r'\]\((\S+?) "wikilink"\)', rep, md)
    fails = 0
    for r, (md, ok) in zip(recs, mds):
        md = fix_links(md) if ok else md
        fails += not ok
        date = r["last_edited"][:10]
        fm = ["---", f"title: {json.dumps(r['title'], ensure_ascii=False)}", f"source_url: {r['url']}",
              f"revision_id: {r['revision_id']}", f"last_edited: {r['last_edited']}",
              "author: Cecep Mustafa", "affiliation: Indonesian Judicial College (IJC)",
              f"orcid: https://orcid.org/{ORCID}", "license: CC-BY-SA-4.0"]
        red = r["redactions"]
        parts = [f"{red['nik']} national ID number(s) removed" if red["nik"] else "",
                 f"{red['case']} example case number(s) replaced with CONTOH placeholders" if red["case"] else "",
                 f"{red['emails']} e-mail address(es) removed" if red["emails"] else "",
                 f"{red['names']} personal name(s) replaced by role" if red["names"] else "",
                 f"{red['details']} personal detail(s) (age, birth, religion, address, NIP) removed" if red["details"] else ""]
        parts = [p for p in parts if p]
        if parts:
            fm.append("redactions: " + json.dumps("; ".join(parts)))
        fm.append("---")
        foot = ("\n\n---\n\n"
                f"*Source:* [{r['title']}]({r['url']}) on the Judicial Knowledge Hub wiki, revision {r['revision_id']} ({date}).  \n"
                f"*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [{ORCID}](https://orcid.org/{ORCID})  \n"
                f"*Cite as:* Mustafa, C. (2026). *{r['title']}*. In *Judicial Knowledge Hub*. {r['url']}  \n"
                "*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)\n")
        with open(r["file"], "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + "\n\n# " + r["title"] + "\n\n" + md.strip() + foot)
    with open("data/pages.jsonl", "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps({k: r[k] for k in ["pageid", "title", "url", "revision_id", "last_edited", "file", "sha256", "wikitext"]}, ensure_ascii=False) + "\n")
    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write(f"# Index of pages ({len(recs)})\n\nAuthor: Cecep Mustafa (IJC), ORCID [{ORCID}](https://orcid.org/{ORCID}). Licence: CC BY-SA 4.0.\n\n")
        for r in recs:
            f.write(f"- [{r['title']}]({r['file']})\n")
    combined = hashlib.sha256("".join(r["sha256"] for r in recs).encode()).hexdigest()
    summary = {"pages": len(recs), "pandoc_failures": fails, "nik_removed": tot["nik"],
               "case_numbers_replaced": tot["case"], "emails_removed": tot["emails"],
               "names_replaced_by_role": tot["names"], "personal_details_removed": tot["details"],
               "combined_sha256": combined,
               "exported_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "newest_revision": max(r["last_edited"] for r in recs)}
    json.dump(summary, open("data/export_summary.json", "w"), indent=2)
    print(json.dumps(summary), flush=True)

if __name__ == "__main__":
    main()
