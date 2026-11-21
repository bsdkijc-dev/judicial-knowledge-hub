import json, datetime
s = json.load(open("data/export_summary.json"))
O = "0000-0003-0037-497X"
readme = f"""# Judicial Knowledge Hub (wiki export)

**Website:** https://bsdkijc-dev.github.io/judicial-knowledge-hub/ · **Kaggle:** https://www.kaggle.com/datasets/judicialcollege/judicial-knowledge-hub-wiki-export-cecep-mustafa

A Markdown copy of every article in the [Judicial Knowledge Hub](https://judicialknowledge.miraheze.org/wiki/Main_Page) wiki: **{s['pages']} pages**, newest revision {s['newest_revision'][:10]}, exported {s['exported_at'][:10]}.

The wiki covers judicial knowledge management, AI governance for courts, judicial education and Indonesian law. All pages were written by the wiki account "Ijc" of the author below.

## Contents
- `pages/`: one Markdown file per wiki page, converted from MediaWiki markup with pandoc. Each file starts with metadata (source URL, revision, last edit, author, ORCID, licence) and ends with a citation footer.
- `INDEX.md`: alphabetical list of all pages.
- `data/pages.jsonl`: one JSON record per page with the cleaned original wikitext, revision ID, last-edit time and a SHA-256 of the text.
- `data/export_summary.json`: page count, redaction counts and a combined checksum.
- `docs/`: the website (GitHub Pages), one HTML page per article with schema.org JSON-LD, Google Scholar citation tags, `llms.txt`, `sitemap.xml` and `robots.txt`, so search engines and AI tools can find, read and cite each article.
- `export.py`, `anon.py`, `anon_map.py`, `build_site.py`: the scripts that produced this export and site (re-run them to refresh).

## Changes from the wiki
- {s['nik_removed']} Indonesian national ID numbers (NIK) of private persons were replaced with `[NIK REMOVED]`.
- {s['case_numbers_replaced']} occurrences of 8 realistic-looking example case numbers were replaced with fictional placeholders `CONTOH-01` to `CONTOH-08`, as in the related Kaggle datasets.
- {s['emails_removed']} e-mail addresses were replaced with `[email removed]`.
- {s['names_replaced_by_role']} mentions of private persons were replaced by their role, e.g. `[Defendant]`, `[Plaintiff]`, `[Child]`, `[Witness]`, `[private person]`. This covers the parties, children and witnesses in the {s.get('case_pages', 207)} court-case pages (`JPAIS:PRECEDENT:*`) and a private student named in workspace notes. This includes public figures who were parties in court cases; their names are also replaced by `[name removed]` on other pages. Names of judges, who acted in their official role, are kept.
- {s['personal_details_removed']} personal details in court-case pages (ages, birth dates and places, religion in identity lists, home addresses, civil-servant numbers) were removed.
- {s['pandoc_failures']} page(s) could not be converted by pandoc and are kept as raw wikitext in a code block.
- Templates, images and talk pages are not included. Historical court decision numbers cited in the articles are kept as in the wiki.

The same cleaning was applied to the wiki itself before it was opened to the public.

Wiki pages are working knowledge-management notes, not official publications of any court. Check primary sources before relying on them.

## Author and citation
**Author:** Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [{O}](https://orcid.org/{O})

**Cite as:** Mustafa, C. (2026). *Judicial Knowledge Hub* [Wiki export]. GitHub. https://github.com/bsdkijc-dev/judicial-knowledge-hub

GitHub also shows a "Cite this repository" button, built from `CITATION.cff`.

## Licence
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the licence of the source wiki. See `LICENSE`. Reuse is allowed with attribution, and adapted versions must use the same licence.
"""
open("README.md", "w").write(readme)
cff = f"""cff-version: 1.2.0
message: "If you use this material, please cite it as below."
type: dataset
title: "Judicial Knowledge Hub (wiki export)"
authors:
  - family-names: "Mustafa"
    given-names: "Cecep"
    orcid: "https://orcid.org/{O}"
    affiliation: "Indonesian Judicial College (IJC)"
abstract: "Markdown export of the {s['pages']} articles of the Judicial Knowledge Hub wiki on judicial knowledge management, AI governance for courts, judicial education and Indonesian law."
date-released: "{s['exported_at'][:10]}"
repository-code: "https://github.com/bsdkijc-dev/judicial-knowledge-hub"
url: "https://judicialknowledge.miraheze.org/wiki/Main_Page"
license: CC-BY-SA-4.0
keywords: [Indonesia, judiciary, judicial education, AI governance, knowledge management, wiki]
"""
open("CITATION.cff", "w").write(cff)
print("ok")
