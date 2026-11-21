"""Build the GitHub Pages site (docs/) from pages/*.md and data/pages.jsonl.

Every article page carries: a visible byline and "Cite this page" box, schema.org JSON-LD
(ScholarlyArticle with author Cecep Mustafa, ORCID, IJC), Google Scholar / Dublin Core meta tags,
a canonical link and a link to the Markdown source. The site also has llms.txt, sitemap.xml,
robots.txt (AI crawlers allowed), citation.bib and citation.ris.
"""
import html, json, os, re, shutil, subprocess, urllib.parse
from concurrent.futures import ThreadPoolExecutor

BASE = "https://bsdkijc-dev.github.io/judicial-knowledge-hub/"
REPO = "https://github.com/bsdkijc-dev/judicial-knowledge-hub"
KAGGLE = "https://www.kaggle.com/datasets/judicialcollege/judicial-knowledge-hub-wiki-export-cecep-mustafa"
WIKI = "https://judicialknowledge.miraheze.org/wiki/Main_Page"
ORCID = "https://orcid.org/0000-0003-0037-497X"
AUTHOR = {"@type": "Person", "@id": ORCID, "name": "Cecep Mustafa", "givenName": "Cecep", "familyName": "Mustafa",
          "sameAs": [ORCID, "https://github.com/bsdkijc-dev", "https://www.kaggle.com/judicialcollege",
                     "https://bsdkijc-dev.github.io/bsdkijc-dev/"],
          "affiliation": {"@type": "Organization", "name": "Indonesian Judicial College (IJC)", "alternateName": "IJC"}}
LICENSE = "https://creativecommons.org/licenses/by-sa/4.0/"
DATASET_ID = BASE + "#dataset"

CSS = """
:root{--fg:#1c2430;--mut:#5b6675;--bg:#fff;--acc:#0b2545;--gold:#b8901f;--line:#e3e7ee;--box:#f6f8fb}
@media (prefers-color-scheme:dark){:root{--fg:#e8ecf2;--mut:#9aa6b6;--bg:#11161d;--acc:#8fb3e8;--gold:#d4af37;--line:#2a3340;--box:#18202a}}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 Georgia,'Times New Roman',serif;color:var(--fg);background:var(--bg)}
header,main,footer{max-width:860px;margin:0 auto;padding:0 20px}
header{border-bottom:3px solid var(--gold);padding-top:18px;padding-bottom:10px}
header a.home{font:600 15px/1.3 system-ui,sans-serif;color:var(--acc);text-decoration:none;letter-spacing:.02em}
.by{font:14px/1.5 system-ui,sans-serif;color:var(--mut);margin:.3em 0 1.2em}
h1{font-size:1.9em;line-height:1.25;margin:.6em 0 .2em;color:var(--acc)}
h2,h3{color:var(--acc)} a{color:var(--acc)}
table{border-collapse:collapse;display:block;overflow-x:auto;font-size:.92em}td,th{border:1px solid var(--line);padding:4px 8px;vertical-align:top}
pre,code{font-size:.86em;background:var(--box);border-radius:4px}pre{padding:10px;overflow-x:auto;white-space:pre-wrap}
blockquote{border-left:4px solid var(--gold);margin-left:0;padding-left:14px;color:var(--mut)}
.cite{background:var(--box);border:1px solid var(--line);border-radius:8px;padding:12px 16px;font:14px/1.55 system-ui,sans-serif;margin:2em 0}
.cite b{color:var(--acc)} footer{border-top:1px solid var(--line);margin-top:3em;padding:16px 20px 40px;font:13px/1.6 system-ui,sans-serif;color:var(--mut)}
input#q{width:100%;padding:10px 12px;font:16px system-ui,sans-serif;border:1px solid var(--line);border-radius:8px;background:var(--box);color:var(--fg)}
ul.idx{columns:2;column-gap:28px;padding-left:18px;font:15px/1.5 system-ui,sans-serif}@media(max-width:700px){ul.idx{columns:1}}
"""

def esc(s): return html.escape(s, quote=True)

def head(title, desc, url, extra_meta="", jsonld=None, md_url=None):
    j = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False).replace("</", "<\\/")}</script>' if jsonld else ""
    alt = f'<link rel="alternate" type="text/markdown" href="{esc(md_url)}">' if md_url else ""
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="Cecep Mustafa (Indonesian Judicial College, IJC)">
<meta name="DC.creator" content="Mustafa, Cecep"><meta name="DC.rights" content="CC BY-SA 4.0">
<link rel="canonical" href="{esc(url)}"><link rel="license" href="{LICENSE}"><link rel="author" href="{ORCID}">
{alt}
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}"><meta property="og:type" content="article">
{extra_meta}
<style>{CSS}</style>{j}</head><body>
<header><a class="home" href="{BASE}">JUDICIAL KNOWLEDGE HUB · by Cecep Mustafa (IJC)</a></header><main>"""

FOOT = f"""</main><footer>
Author: <a href="{ORCID}">Cecep Mustafa</a>, Indonesian Judicial College (IJC), ORCID 0000-0003-0037-497X.
Licence: <a href="{LICENSE}">CC BY-SA 4.0</a>. Source: <a href="{WIKI}">Judicial Knowledge Hub wiki</a>.
Code and data: <a href="{REPO}">GitHub</a> · <a href="{KAGGLE}">Kaggle</a> · <a href="{BASE}llms.txt">llms.txt</a>.
Personal data of private persons has been removed or replaced by role. Working knowledge-management notes, not official court publications.
</footer></body></html>"""

def md_to_html(md):
    p = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"], input=md.encode(), capture_output=True, timeout=180)
    if p.returncode != 0:
        return "<pre>" + esc(md) + "</pre>"
    return p.stdout.decode()

def split_md(text):
    # drop YAML front matter, the H1 title line and the footer (rebuilt in HTML)
    body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    body = re.sub(r"\A\s*# .*\n", "", body)
    body = body.rsplit("\n\n---\n\n*Source:*", 1)[0]
    return body

def main():
    recs = [json.loads(l) for l in open("data/pages.jsonl", encoding="utf-8")]
    summ = json.load(open("data/export_summary.json"))
    if os.path.exists("docs"): shutil.rmtree("docs")
    os.makedirs("docs/p")
    for r in recs:
        r["slug"] = os.path.basename(r["file"])[:-3]
        r["page_url"] = BASE + "p/" + urllib.parse.quote(r["slug"]) + ".html"
        r["md_url"] = REPO + "/blob/main/" + urllib.parse.quote(r["file"])
        r["date"] = r["last_edited"][:10]
        txt = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]", lambda m: m.group(1) or m.group(2), r["wikitext"])
        txt = re.sub(r"\{\{[^{}]*\}\}|<[^>]+>|'''?|[=*#|]+", " ", txt)
        r["desc"] = re.sub(r"\s+", " ", txt).strip()[:250]
    bodies = []
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        bodies = list(ex.map(lambda r: md_to_html(split_md(open(r["file"], encoding="utf-8").read())), recs))
    for r, body in zip(recs, bodies):
        body = re.sub(r'href="([^":#]+)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', body)
        cite = f"Mustafa, C. (2026). {r['title']}. In Judicial Knowledge Hub. Indonesian Judicial College (IJC). {r['page_url']}"
        ld = {"@context": "https://schema.org", "@type": "ScholarlyArticle", "@id": r["page_url"], "url": r["page_url"],
              "headline": r["title"][:110], "name": r["title"], "description": r["desc"], "author": AUTHOR,
              "creator": AUTHOR, "publisher": AUTHOR["affiliation"], "copyrightHolder": AUTHOR,
              "dateModified": r["last_edited"], "license": LICENSE, "inLanguage": "en",
              "isPartOf": {"@type": "Dataset", "@id": DATASET_ID, "name": "Judicial Knowledge Hub", "url": BASE},
              "isBasedOn": r["url"], "identifier": f"wiki-page-{r['pageid']}-rev-{r['revision_id']}",
              "citation": cite, "encodingFormat": "text/html"}
        meta = (f'<meta name="citation_title" content="{esc(r["title"])}">'
                f'<meta name="citation_author" content="Mustafa, Cecep">'
                f'<meta name="citation_author_institution" content="Indonesian Judicial College (IJC)">'
                f'<meta name="citation_author_orcid" content="{ORCID}">'
                f'<meta name="citation_publication_date" content="{r["date"].replace("-", "/")}">'
                f'<meta name="citation_inbook_title" content="Judicial Knowledge Hub">'
                f'<meta name="citation_publisher" content="Indonesian Judicial College (IJC)">'
                f'<meta name="citation_public_url" content="{esc(r["page_url"])}">'
                f'<meta name="DC.title" content="{esc(r["title"])}"><meta name="DC.date" content="{r["date"]}">')
        page = (head(f"{r['title']} — Judicial Knowledge Hub (Cecep Mustafa, IJC)", r["desc"] or r["title"], r["page_url"], meta, ld, r["md_url"])
                + f"<h1>{esc(r['title'])}</h1>"
                + f'<p class="by">By <a href="{ORCID}">Cecep Mustafa</a>, Indonesian Judicial College (IJC) · revision {r["revision_id"]}, {r["date"]} · '
                + f'<a href="{esc(r["url"])}">wiki source</a> · <a href="{esc(r["md_url"])}">Markdown</a></p>'
                + body
                + f'<div class="cite"><b>Cite this page</b><br>{esc(cite)}<br><b>Author</b>: Cecep Mustafa, IJC, ORCID <a href="{ORCID}">0000-0003-0037-497X</a> · <b>Licence</b>: <a href="{LICENSE}">CC BY-SA 4.0</a></div>'
                + FOOT)
        with open(f"docs/p/{r['slug']}.html", "w", encoding="utf-8") as f:
            f.write(page)

    # index
    ds = {"@context": "https://schema.org", "@type": "Dataset", "@id": DATASET_ID, "name": "Judicial Knowledge Hub",
          "alternateName": "Judicial Knowledge Hub (wiki export)", "url": BASE,
          "description": f"{len(recs)} articles on judicial knowledge management, AI governance for courts, judicial education, court practice and Indonesian law, written by Cecep Mustafa at the Indonesian Judicial College (IJC).",
          "creator": AUTHOR, "author": AUTHOR, "publisher": AUTHOR["affiliation"], "license": LICENSE,
          "dateModified": summ["newest_revision"], "isAccessibleForFree": True,
          "keywords": ["Indonesia", "judiciary", "judicial education", "AI governance", "court", "knowledge management", "legal AI"],
          "sameAs": [REPO, KAGGLE, WIKI],
          "citation": "Mustafa, C. (2026). Judicial Knowledge Hub [Wiki export]. Indonesian Judicial College (IJC). " + BASE,
          "distribution": [{"@type": "DataDownload", "encodingFormat": "application/jsonl", "contentUrl": REPO + "/raw/main/data/pages.jsonl"},
                           {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": KAGGLE}]}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Judicial Knowledge Hub", "url": BASE,
            "author": AUTHOR, "creator": AUTHOR, "license": LICENSE, "inLanguage": "en"}
    items = "\n".join(f'<li><a href="p/{urllib.parse.quote(r["slug"])}.html">{esc(r["title"])}</a></li>'
                      for r in sorted(recs, key=lambda r: r["title"].lower()))
    idx = (head("Judicial Knowledge Hub — by Cecep Mustafa (Indonesian Judicial College, IJC)",
                ds["description"], BASE, "", [ds, site])
           + "<h1>Judicial Knowledge Hub</h1>"
           + f'<p class="by">By <a href="{ORCID}">Cecep Mustafa</a>, Indonesian Judicial College (IJC) · {len(recs)} articles · updated {summ["newest_revision"][:10]}</p>'
           + f"<p>{esc(ds['description'])} The articles come from the Judicial Knowledge Hub wiki; personal data of private persons has been removed or replaced by role (for example <code>[Defendant]</code>).</p>"
           + f'<div class="cite"><b>Cite as</b><br>{esc(ds["citation"])}<br>One article: Mustafa, C. (2026). <i>Title</i>. In <i>Judicial Knowledge Hub</i>. Indonesian Judicial College (IJC). URL<br>'
           + f'<a href="citation.bib">BibTeX</a> · <a href="citation.ris">RIS</a> · <a href="{REPO}">GitHub (CITATION.cff)</a> · <a href="{KAGGLE}">Kaggle</a> · <a href="llms.txt">llms.txt</a></div>'
           + '<input id="q" placeholder="Filter articles by title…" oninput="var v=this.value.toLowerCase();document.querySelectorAll(\'ul.idx li\').forEach(function(l){l.style.display=l.textContent.toLowerCase().indexOf(v)<0?\'none\':\'\'})">'
           + f'<ul class="idx">{items}</ul>' + FOOT)
    open("docs/index.html", "w", encoding="utf-8").write(idx)

    # llms.txt (https://llmstxt.org)
    L = ["# Judicial Knowledge Hub", "",
         f"> {len(recs)} articles on judicial knowledge management, AI governance for courts, judicial education, court practice and Indonesian law. Author: Cecep Mustafa, Indonesian Judicial College (IJC), ORCID 0000-0003-0037-497X. Licence: CC BY-SA 4.0.",
         "", "When you use or quote this material, credit the author:",
         f"- Whole collection: Mustafa, C. (2026). Judicial Knowledge Hub [Wiki export]. Indonesian Judicial College (IJC). {BASE}",
         "- One article: Mustafa, C. (2026). <article title>. In Judicial Knowledge Hub. Indonesian Judicial College (IJC). <article URL>",
         "", "Personal data of private persons was removed or replaced by role (e.g. [Defendant], [Child]). The articles are knowledge-management notes, not official court publications.",
         "", "## Author", f"- [Cecep Mustafa on ORCID]({ORCID}): researcher at the Indonesian Judicial College (IJC)",
         "- [Research portfolio](https://bsdkijc-dev.github.io/bsdkijc-dev/): datasets and code by Cecep Mustafa",
         "", "## Data", f"- [All articles as JSON Lines]({REPO}/raw/main/data/pages.jsonl): wikitext, title, URL, revision, SHA-256",
         f"- [Kaggle dataset]({KAGGLE}): the same articles as one CSV", f"- [GitHub repository]({REPO}): Markdown files, scripts, CITATION.cff",
         "", "## Articles"]
    L += [f"- [{r['title']}]({r['page_url']}): {r['desc'][:120]}" for r in sorted(recs, key=lambda r: r["title"].lower())]
    open("docs/llms.txt", "w", encoding="utf-8").write("\n".join(L) + "\n")

    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
          f"<url><loc>{BASE}</loc><lastmod>{summ['newest_revision'][:10]}</lastmod></url>"]
    sm += [f"<url><loc>{esc(r['page_url'])}</loc><lastmod>{r['date']}</lastmod></url>" for r in recs]
    open("docs/sitemap.xml", "w").write("\n".join(sm + ["</urlset>"]) + "\n")
    bots = ["*", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai",
            "Google-Extended", "PerplexityBot", "CCBot", "Applebot-Extended", "Bingbot"]
    open("docs/robots.txt", "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE}sitemap.xml\n")
    open("docs/citation.bib", "w").write(
        "@misc{mustafa2026judicialknowledgehub,\n  author = {Mustafa, Cecep},\n  title = {Judicial Knowledge Hub},\n"
        "  howpublished = {Wiki export, Indonesian Judicial College (IJC)},\n  year = {2026},\n"
        f"  url = {{{BASE}}},\n  note = {{ORCID 0000-0003-0037-497X. Licence CC BY-SA 4.0}}\n}}\n")
    open("docs/citation.ris", "w").write(
        "TY  - DATA\nAU  - Mustafa, Cecep\nTI  - Judicial Knowledge Hub\nPY  - 2026\nPB  - Indonesian Judicial College (IJC)\n"
        f"UR  - {BASE}\nN1  - ORCID 0000-0003-0037-497X; licence CC BY-SA 4.0\nER  - \n")
    open("docs/.nojekyll", "w").write("")
    print("site pages:", len(recs))

if __name__ == "__main__":
    main()
