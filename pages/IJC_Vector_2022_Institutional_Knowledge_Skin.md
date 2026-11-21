---
title: "IJC Vector 2022 Institutional Knowledge Skin"
source_url: https://judicialknowledge.miraheze.org/wiki/IJC_Vector_2022_Institutional_Knowledge_Skin
revision_id: 986
last_edited: 2026-09-16T01:05:06Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# IJC Vector 2022 Institutional Knowledge Skin

{{#tag:infobox\| \|title=Layer 1 Architecture \|subheader=Visual Identity & UI Skin \|image=<img src="bsdk.png" title="bsdk.png" width="200" alt="bsdk.png" /> \|caption=Mahkamah Agung Corporate University Theme \|label1=Base Skin \|data1=Vector 2022 (MediaWiki Core) \|label2=Theme System \|data2=IJC Custom Institutional Skin \|label3=Primary Color \|data3=Institutional Navy (#123B5D) \|label4=Accent Colors \|data4=Judicial Red, Knowledge Gold, Digital Blue, Institutional Green \|label5=Author / Lead \|data5=Cecep Mustafa (Knowledge Grapher & Ingestion Lead) }}

## Portal Navigation / Navigasi Institusional

- [Portal Utama](Main_Page.md)
- 
- 

---

## Summary / Ringkasan

## Entity Ingestion / Ingesti Entitas

- Entity ID: JPAIS-ARCH-VECTOR-2022-LAYER-1
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Description / Deskripsi

Layer 1 establishes the production-ready frontend presentation layer of the \*\*Indonesian Judicial College (IJC) / Mahkamah Agung Corporate University\*\* Wiki. It implements MediaWiki Vector 2022 with a non-destructive custom institutional skin (\`IJCVector\`), integrating the corporate visual identity derived from the BSDK pillar/book logo, a two-tier professional institutional header, a six-domain global navigation system, mobile-first responsive design, and modular CSS variables.

## Core Architectural Specifications / Spesifikasi Arsitektur Inti

- \*\*Skin Foundation:\*\* Built strictly upon MediaWiki Vector 2022 without modifying core files, ensuring upgrade resilience.
- \*\*Color Token Palette:\*\* Anchored around Institutional Navy (\`#123B5D\`), accented by Judicial Red (\`#C90016\`), Knowledge Gold (\`#C98A16\`), Digital Blue (\`#008BC5\`), and Institutional Green (\`#087A43\`).
- \*\*Header Hierarchy:\*\* Displays the official administrative chain: MAHKAMAH AGUNG REPUBLIK INDONESIA → BSDK \| INDONESIAN JUDICIAL COLLEGE → JUDICIAL KNOWLEDGE WIKI.
- \*\*Global Navigation:\*\* Structured across six core institutional pillars: Knowledge, Academy, Research, Policy, Repository, and About.

## Production Code: skin.json

``` json
{
  "name": "IJCVector",
  "version": "2.0.0",
  "author": ["Cecep Mustafa (Knowledge Grapher & Ingestion Lead)"],
  "description": "Custom institutional Vector 2022 skin for Indonesian Judicial College / Mahkamah Agung Corporate University.",
  "type": "skin",
  "requires": {
    "MediaWiki": ">= 1.39.0"
  },
  "valid-skins": ["IJCVector"],
  "sources": {
    "IJCVector": "IJCVector.php"
  },
  "ResourceFileModulePaths": {
    "localBasePath": "resources",
    "remoteSkinPath": "IJCVector/resources"
  },
  "ResourceModules": {
    "skins.ijcvector.styles": {
      "styles": [
        "ijc.css",
        "ijc-components.css",
        "ijc-mobile.css"
      ]
    }
  },
  "config": {
    "IJCInstituteName": "Indonesian Judicial College",
    "IJCCorpUni": "Mahkamah Agung Corporate University"
  },
  "manifest_version": 2
}
```

## Production Code: ijc.css (Modular CSS Stylesheet)

``` css
/* ==========================================================
   IJC VECTOR 2022 INSTITUTIONAL STYLING LAYER (LAYER 1)
   ========================================================== */

:root {
  --ijc-navy: #123B5D;
  --ijc-navy-dark: #0B253B;
  --ijc-navy-light: #1D5B8D;
  --ijc-red: #C90016;
  --ijc-gold: #C98A16;
  --ijc-blue: #008BC5;
  --ijc-green: #087A43;
  --ijc-text: #202124;
  --ijc-text-muted: #5f6368;
  --ijc-background: #F7F8FA;
  --ijc-card: #FFFFFF;
  --ijc-border: #DADCE0;
  --ijc-font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

body {
  background-color: var(--ijc-background);
  color: var(--ijc-text);
  font-family: var(--ijc-font-sans);
}

/* Two-Level Institutional Header */
#ijc-global-header {
  background-color: var(--ijc-navy-dark);
  color: #FFFFFF;
  border-bottom: 3px solid var(--ijc-gold);
}

.ijc-header-level-1 {
  background-color: var(--ijc-navy);
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  padding: 6px 24px;
  text-transform: uppercase;
  font-weight: 600;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.ijc-header-level-2 {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  background-color: var(--ijc-card);
  color: var(--ijc-navy);
  border-bottom: 1px solid var(--ijc-border);
}

.ijc-brand-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--ijc-navy);
  display: flex;
  align-items: center;
  gap: 12px;
}

/* Responsive Mobile Adjustments */
@media screen and (max-width: 768px) {
  .ijc-header-level-2 {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
}
```

## Sources / Sumber

## Provenance / Provenans

[Arsitektur Wiki Vector 2022](https://judicialknowledge.miraheze.org/wiki/Category:Vector_2022_Architecture) [Pusat Pengetahuan Peradilan](https://judicialknowledge.miraheze.org/wiki/Category:Judicial_Knowledge)

---

*Source:* [IJC Vector 2022 Institutional Knowledge Skin](https://judicialknowledge.miraheze.org/wiki/IJC_Vector_2022_Institutional_Knowledge_Skin) on the Judicial Knowledge Hub wiki, revision 986 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *IJC Vector 2022 Institutional Knowledge Skin*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/IJC_Vector_2022_Institutional_Knowledge_Skin  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
