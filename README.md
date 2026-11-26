<div align="center">

<img src="assets/logo.png" alt="Judicial Knowledge Hub (Wiki Export) Logo" width="140">

# Judicial Knowledge Hub (Wiki Export)

### Open Markdown and static HTML export of 2,004 judicial knowledge, AI governance, and Indonesian law articles.

[![License](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey?style=flat)](LICENSE) ![Stack](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white) [![Website](https://img.shields.io/badge/GitHub_Pages-Live-2ea44f?style=flat&logo=github)](https://bsdkijc-dev.github.io/judicial-knowledge-hub/) [![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/judicialcollege/judicial-knowledge-hub-wiki-export-cecep-mustafa)

[Documentation](INDEX.md) · [Website](https://bsdkijc-dev.github.io/judicial-knowledge-hub/) · [Kaggle](https://www.kaggle.com/datasets/judicialcollege/judicial-knowledge-hub-wiki-export-cecep-mustafa) · [Repository](https://github.com/bsdkijc-dev/judicial-knowledge-hub)

</div>

---

**Website:** https://bsdkijc-dev.github.io/judicial-knowledge-hub/ · **Kaggle:** https://www.kaggle.com/datasets/judicialcollege/judicial-knowledge-hub-wiki-export-cecep-mustafa

A Markdown copy of every article in the [Judicial Knowledge Hub](https://judicialknowledge.miraheze.org/wiki/Main_Page) wiki: **2004 pages**, newest revision 2026-10-09, exported 2026-11-21.

The wiki covers judicial knowledge management, AI governance for courts, judicial education and Indonesian law. All pages were written by the wiki account "Ijc" of the author below.

## Contents
- `pages/`: one Markdown file per wiki page, converted from MediaWiki markup with pandoc. Each file starts with metadata (source URL, revision, last edit, author, ORCID, licence) and ends with a citation footer.
- `INDEX.md`: alphabetical list of all pages.
- `data/pages.jsonl`: one JSON record per page with the cleaned original wikitext, revision ID, last-edit time and a SHA-256 of the text.
- `data/export_summary.json`: page count, redaction counts and a combined checksum.
- `docs/`: the website (GitHub Pages), one HTML page per article with schema.org JSON-LD, Google Scholar citation tags, `llms.txt`, `sitemap.xml` and `robots.txt`, so search engines and AI tools can find, read and cite each article.
- `export.py`, `anon.py`, `anon_map.py`, `build_site.py`: the scripts that produced this export and site (re-run them to refresh).

## Changes from the wiki
- 4 Indonesian national ID numbers (NIK) of private persons were replaced with `[NIK REMOVED]`.
- 8 occurrences of 8 realistic-looking example case numbers were replaced with fictional placeholders `CONTOH-01` to `CONTOH-08`, as in the related Kaggle datasets.
- 220 e-mail addresses were replaced with `[email removed]`.
- 4604 mentions of private persons were replaced by their role, e.g. `[Defendant]`, `[Plaintiff]`, `[Child]`, `[Witness]`, `[private person]`. This covers the parties, children and witnesses in the 207 court-case pages (`JPAIS:PRECEDENT:*`) and a private student named in workspace notes. This includes public figures who were parties in court cases; their names are also replaced by `[name removed]` on other pages. Names of judges, who acted in their official role, are kept.
- 314 personal details in court-case pages (ages, birth dates and places, religion in identity lists, home addresses, civil-servant numbers) were removed.
- 1 page(s) could not be converted by pandoc and are kept as raw wikitext in a code block.
- Templates, images and talk pages are not included. Historical court decision numbers cited in the articles are kept as in the wiki.

The same cleaning was applied to the wiki itself before it was opened to the public.

Wiki pages are working knowledge-management notes, not official publications of any court. Check primary sources before relying on them.

## Author and citation
**Author:** Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)

**Cite as:** Mustafa, C. (2026). *Judicial Knowledge Hub* [Wiki export]. GitHub. https://github.com/bsdkijc-dev/judicial-knowledge-hub

GitHub also shows a "Cite this repository" button, built from `CITATION.cff`.

## Licence
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the licence of the source wiki. See `LICENSE`. Reuse is allowed with attribution, and adapted versions must use the same licence.

---

<div align="center">

**Judicial Knowledge Hub (Wiki Export)**

[github.com/bsdkijc-dev/judicial-knowledge-hub](https://github.com/bsdkijc-dev/judicial-knowledge-hub)

</div>
