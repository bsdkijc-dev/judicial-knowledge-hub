"""Privacy rules for the Judicial Knowledge Hub export (owner decisions of 2026-11-21).

Applied to every page:
  * e-mail addresses -> [email removed]
  * the private student named in workspace notes -> [private person]
Applied to court-case pages (JPAIS:PRECEDENT:*):
  * private parties' names -> their role, e.g. [Defendant], [Child] (per-page list in anon_map.py;
    public officials and public figures in public cases are kept, see anon_map.KEPT_PUBLIC)
  * ages, birth dates and places, religion in identity lists, home addresses and NIP numbers removed
"""
import re
from anon_map import M, EXCLUDE_TITLES, GLOBAL_NAMES

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
STUDENT = [(re.compile(r"Najma[\s_]+Ilmi[\s_]+Hulwan", re.I), "[private person]"),
           (re.compile(r"(?<![A-Za-z])(?:Najma|Hulwan)(?![A-Za-z])", re.I), "[private person]"),
           (re.compile(r"born June 30, 2006"), "born [date removed]")]

YEAR = r"\b(?:1[89]|20)\d\d\b"
DETAILS = [
    (re.compile(r"\b\d{1,3}-year-old\s+"), ""),
    (re.compile(r"\b(?:[Aa]ge|[Aa]ged)\s*(?:±|Â±|approx\.?|approximately|about|around)?\s*\d{1,3}"
                r"(?:\s*(?:years|yrs)\.?(?:\s+old)?)?(?:\s+at the time)?"), "[age removed]"),
    (re.compile(r"(?:±\s*|Â±\s*|approx\.\s*)?\b\d{1,3}\s*(?:years old|yrs\b\.?|years of age)(?:\s+at the time)?"), "[age removed]"),
    (re.compile(r"(?<=\()\d{1,2},\s+(?=[a-zA-Z])"), ""),
    (re.compile(r"\b[Bb]orn\b(?!\s+(?:pursuant|therefrom|from|out|of|within|between|in wedlock|during|to|after|before))"
                r"(?:\s+(?:in|at|on))?[^;)\n]{0,70}?" + YEAR), "born [details removed]"),
    (re.compile(r"\b[Bb]orn\s+(?:in|at)\s+(?:\[\[)?[A-Z][^,;)\n]{0,40}?(?:\]\])?(?=[,;)\n]|\s+(?:male|female|Male|Female|and)\b)"),
     "born [place removed]"),
    (re.compile(r"[,;]\s*(?:Muslim|Christian|Catholic|Protestant|Buddhist|Hindu|Confucian|Kong Fu Tsu|Konghucu|Islam)(?=\s*[,;)])"), ""),
    (re.compile(r"\bJl\.\s*[A-Z][^,;)\n]{0,60}"), "[address removed]"),
    (re.compile(r"\b(residing|resident|domiciled|living)(\s+(?:at|in|of))\s+(?=(?:the\s+)?[A-Z]|Jl\.)[^;)\n]{1,140}?"
                r"(?=[;)\n]|'''|$|(?<!\bNo)(?<!\bKp)(?<!\bJl)(?<!\bGg)(?<!\bKel)(?<!\bKec)(?<!\bDs)\.(?:\s+[A-Z\['" + '"' + r"]|\s*$)"
                r"|,\s+(?:was|is|were|filed|and|at the|before|against|charged|brought|sued|a|an|who)\b)"),
     r"\1\2 [address removed]"),
    (re.compile(r"\bNIP\.?\s*:?\s*\d[\d\s]{7,22}\d"), "NIP [removed]"),
]

# a father's name after a replaced party name: "[Plaintiff] binti H. Syafri Atin" -> "[Plaintiff]"
BIN = re.compile(r"(\[[^\]]+\])(?:,?\s+(?:[A-Z][A-Za-z]*\.)+(?:,\s+(?:[A-Z][A-Za-z]*\.)+)*)?\s+(?:bin|binti|BIN|BINTI)\s+"
                 r"(?:(?:H|Hj|Moh|Muh|Abd|R|S|Ir|Drs|Dra|M|Ny)\.?\s+)*(?:\[[^\]]+\]|[A-Z][A-Za-z'./]*)(?:\s+(?:\[[^\]]+\]|[A-Z][A-Za-z'./]*))*")

LABELS = re.compile(r"\[(?:" + "|".join(sorted({re.escape(v) for d in M.values() for v in d.values()} | {"private person", "name removed"}, key=len, reverse=True)) + r")\]")
DETAILS_MARK = re.compile(r"\[age removed\]|born \[(?:details|place) removed\]|\[address removed\]|NIP \[removed\]")

GLOBAL_RX = re.compile(r"(?<![\w])(?:" + "|".join(r"\s+".join(map(re.escape, n.split())) for n in sorted(GLOBAL_NAMES, key=len, reverse=True)) + r")(?![\w])", re.I)

_compiled = {}
def _names(key):
    if key not in _compiled:
        pats = []
        for name in sorted(M.get(key, {}), key=len, reverse=True):
            rx = r"(?<![\w])" + r"\s+".join(re.escape(w) for w in name.split()) + r"(?![\w])"
            pats.append((re.compile(rx, re.I), "[" + M[key][name] + "]"))
        _compiled[key] = pats
    return _compiled[key]

def anonymise(title, text):
    n = {"emails": 0, "names": 0, "details": 0}
    text, n["emails"] = EMAIL.subn("[email removed]", text)
    for rx, rep in STUDENT:
        text, k = rx.subn(rep, text); n["names"] += k
    if title.startswith("JPAIS:PRECEDENT:"):
        for rx, rep in _names(title[len("JPAIS:PRECEDENT:"):]):
            text, k = rx.subn(rep, text); n["names"] += k
        text, k = BIN.subn(r"\1", text); n["names"] += k
        for rx, rep in DETAILS:
            text, k = rx.subn(rep, text); n["details"] += k
    text = GLOBAL_RX.sub("[name removed]", text)
    # report totals from the markers, so re-running on already-cleaned text gives the same counts
    n["emails"] = text.count("[email removed]")
    n["names"] = len(LABELS.findall(text))
    n["details"] = len(DETAILS_MARK.findall(text))
    return text, n
