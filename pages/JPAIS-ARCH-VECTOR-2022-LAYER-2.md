---
title: "JPAIS:ARCH:VECTOR-2022-LAYER-2"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-2
revision_id: 987
last_edited: 2026-09-16T01:06:52Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS:ARCH:VECTOR-2022-LAYER-2

{{#tag:infobox\|\|title=Layer 2 Architecture\|subheader=Knowledge Design System\|image=<img src="bsdk.png" title="bsdk.png" width="200" alt="bsdk.png" />\|caption=Mahkamah Agung Corporate University Theme\|label1=Base Architecture\|data1=Vector 2022 (MediaWiki Core)\|label2=Component Suite\|data2=Knowledge Cards, Infoboxes, Portal Templates\|label3=Taxonomy Model\|data3=Hierarchical Semantic Categories\|label4=Metadata Standard\|data4=Dublin Core / Schema.org JSON-LD\|label5=Author / Lead\|data5=Cecep Mustafa (Knowledge Grapher & Ingestion Lead)}}

## Portal Navigation / Navigasi Institusional

- [Portal Utama](Main_Page.md)
- 
- 

---

## Summary / Ringkasan

## Entity Ingestion / Ingesti Entitas

- Entity ID: JPAIS-ARCH-VECTOR-2022-LAYER-2
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Description / Deskripsi

Layer 2 defines the complete \*\*Knowledge Design System\*\* for the Indonesian Judicial College (IJC) Wiki. It establishes reusable structural components designed to maintain consistency across long-form legal documents, regulatory repositories, and comparative jurisprudence records. This layer includes the specifications for Modular Knowledge Cards, MediaWiki Infobox Templates, Hierarchical Taxonomy Categories, Portal Page Layout Templates, and Structured Article Metadata.

## 1. Modular Knowledge Cards Component

Knowledge cards provide structured previews for portal pages, allowing users to scan topics, research papers, regulations, and comparative studies at a glance.

``` html
<div class="ijc-knowledge-card" style="border-top-color: var(--ijc-navy);">
  <span class="ijc-card-badge verified">Verified Knowledge</span>
  <h4 style="margin: 4px 0 8px 0;"><a href="...">Tripartite Conciliation Panels and Orders in Lieu of Settlement</a></h4>
  <p style="font-size: 0.9rem; color: var(--ijc-text-muted); margin-bottom: 12px;">Judicial mediation reform adapting the Japanese Minji Chōtei model into the Indonesian judiciary under the JPAIS Framework.</p>
  <div style="font-size: 0.8rem; display: flex; justify-content: space-between; border-top: 1px solid var(--ijc-border); pt-2; color: var(--ijc-text-muted);">
    <span>Jurisdiction: Indonesia / Japan</span>
    <span>ID: JPAIS-REF-001</span>
  </div>
</div>
```

## 2. Infobox Template Architecture (\`Template:Infobox Regulation\`)

Standardized infoboxes ensure uniform presentation of legal instruments, research papers, and institutional frameworks without dominating the reading experience.

``` mediawiki
<div class="ijc-infobox">
<table style="width:100%; border-collapse:collapse;">
  <tr>
    <th colspan="2" style="text-align:center; background:var(--ijc-navy); color:#fff; font-size:1rem; padding:10px;">
      {{{title|Regulatory Instrument}}}
    </th>
  </tr>
  <tr>
    <td><b>Type</b></td>
    <td>{{{type|PERMA / SEMA / Law}}}</td>
  </tr>
  <tr>
    <td><b>Jurisdiction</b></td>
    <td>{{{jurisdiction|Indonesia}}}</td>
  </tr>
  <tr>
    <td><b>Legal Domain</b></td>
    <td>{{{legal_domain|Judicial Reform / Civil Procedure}}}</td>
  </tr>
  <tr>
    <td><b>Status</b></td>
    <td><span style="color:var(--ijc-green); font-weight:600;">{{{status|Active}}}</span></td>
  </tr>
  <tr>
    <td><b>Verification</b></td>
    <td>{{{verification_status|VERIFIED}}}</td>
  </tr>
  <tr>
    <td><b>Knowledge Grapher</b></td>
    <td>{{{knowledge_grapher|Cecep Mustafa}}}</td>
  </tr>
</table>
</div>
```

## 3. Taxonomy & Category Hierarchy

To support GEO/AI discoverability and related-content browsing, the wiki implements a top-level semantic taxonomy:

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

## 4. Standardized Article Metadata Block

Every long-form article requires a standardized metadata container placed immediately below the lead summary to maintain institutional accountability.

``` mediawiki
{| class="wikitable ijc-metadata-table" style="width:100%; background:var(--ijc-card); border:1px solid var(--ijc-border); font-size:0.9rem;"
! Knowledge Type
| Reform Proposal / Comparative Study
|-
! Jurisdiction
| Indonesia / Japan Comparative
|-
! Authority
| Mahkamah Agung Republik Indonesia / JICA KCCP
|-
! Verification Status
| VERIFIED (Ingestion Lead: Cecep Mustafa)
|-
! Last Reviewed
| 2026-09-15
|-
! Associated Entity ID
| <code>JPAIS:REFORM-PROPOSAL:KCCP-REF-001</code>
|}
```

## Sources / Sumber

## Provenance / Provenans

---

*Source:* [JPAIS:ARCH:VECTOR-2022-LAYER-2](https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-2) on the Judicial Knowledge Hub wiki, revision 987 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS:ARCH:VECTOR-2022-LAYER-2*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-2  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
