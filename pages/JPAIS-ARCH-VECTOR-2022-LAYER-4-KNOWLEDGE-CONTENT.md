---
title: "JPAIS:ARCH:VECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT
revision_id: 1031
last_edited: 2026-09-16T02:16:13Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS:ARCH:VECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT

\_\_NOTOC\_\_

{{#tag:infobox\| \|title=Layer 4 Knowledge Content \|subheader=Repository Architecture \|image=<img src="bsdk.png" title="bsdk.png" width="200" alt="bsdk.png" /> \|caption=Mahkamah Agung Corporate University Theme \|label1=Content Repositories \|data1=Articles, Cases, Regulations, Institutions, Concepts \|label2=Platform Target \|data2=Miraheze MediaWiki Hosting \|label3=Knowledge Grapher \|data3=Cecep Mustafa \|label4=Verification Status \|data4=VERIFIED }}

## Portal Navigation / Navigasi Institusional

- [Portal Utama](Main_Page.md)
- 
- 
- 

---

## Summary / Ringkasan

## Entity Ingestion / Ingesti Entitas

- Entity ID: JPAIS-ARCH-VECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Description / Deskripsi

Layer 4 defines the comprehensive \*\*Knowledge Content Architecture\*\* for the Indonesian Judicial College (IJC) Wiki. It establishes standardized content structures across five fundamental repository types: \*\*Long-form Articles\*\*, \*\*Judicial Cases & Reasoning\*\*, \*\*Regulatory Instruments (PERMA/SEMA/SK KMA)\*\*, \*\*Institutional Profiles\*\*, and \*\*Core Legal Concepts\*\*.

---

## 1. Standardized Knowledge Article Template (\`Template:KnowledgeArticle\`)

Designed for long-form legal analyses, academic working papers, and comparative judicial research.

``` mediawiki
<div class="ijc-article-container" style="max-width:900px; margin:0 auto; background:var(--ijc-card); padding:24px; border:1px solid var(--ijc-border); border-radius:4px;">
  <span style="font-size:0.75srem; font-weight:700; text-transform:uppercase; color:var(--ijc-gold);">{{{knowledge_type|Research Article}}}</span>
  <h1 style="color:var(--ijc-navy); margin:4px 0 12px 0; border:none; font-size:2rem;">{{{title}}}</h1>
  
  <div class="ijc-metadata-banner" style="background:var(--ijc-background); border-left:4px solid var(--ijc-navy); padding:12px; margin-bottom:20px; font-size:0.9rem;">
    <b>Jurisdiction:</b> {{{jurisdiction|Indonesia}}} | 
    <b>Legal Domain:</b> {{{legal_domain}}} | 
    <b>Knowledge Grapher:</b> {{{knowledge_grapher|Cecep Mustafa}}} | 
    <b>Verification:</b> <span style="color:var(--ijc-green); font-weight:600;">{{{verification_status|VERIFIED}}}</span>
  </div>

  <div class="ijc-article-body" style="line-height:1.6; color:var(--ijc-text);">
    {{{content}}}
  </div>
</div>
<includeonly>
[[Category:{{{legal_domain}}}]]
[[Category:Jurisdiction: {{{jurisdiction|Indonesia}}}]]
</includeonly>
```

---

## 2. Judicial Case Directory Template (\`Template:JudicialCase\`)

Standardized format for structuring landmark Supreme Court rulings (\*Direktori Putusan\*) and comparative case studies.

``` mediawiki
<div style="background:var(--ijc-card); border:1px solid var(--ijc-border); padding:20px; border-radius:4px; margin-bottom:20px;">
  <h3>⚖ Case Summary: {{{case_title}}}</h3>
  <table style="width:100%; border-collapse:collapse; font-size:0.9rem; margin-top:12px;">
    <tr>
      <td style="width:25%; background:var(--ijc-background); padding:8px; border:1px solid var(--ijc-border);"><b>Decision Number</b></td>
      <td style="padding:8px; border:1px solid var(--ijc-border);"><code>{{{decision_number}}}</code></td>
    </tr>
    <tr>
      <td style="background:var(--ijc-background); padding:8px; border:1px solid var(--ijc-border);"><b>Court Level</b></td>
      <td style="padding:8px; border:1px solid var(--ijc-border);">{{{court_level|Mahkamah Agung Republik Indonesia}}}</td>
    </tr>
    <tr>
      <td style="background:var(--ijc-background); padding:8px; border:1px solid var(--ijc-border);"><b>Legal Issue</b></td>
      <td style="padding:8px; border:1px solid var(--ijc-border);">{{{legal_issue}}}</td>
    </tr>
    <tr>
      <td style="background:var(--ijc-background); padding:8px; border:1px solid var(--ijc-border);"><b>Judicial Reasoning</b></td>
      <td style="padding:8px; border:1px solid var(--ijc-border);">{{{judicial_reasoning}}}</td>
    </tr>
  </table>
</div>
<includeonly>
[[Category:Judicial Decisions]]
</includeonly>
```

---

## 3. Regulatory Instrument Template (\`Template:RegulatoryInstrument\`)

Structured repository format for binding normative rules including PERMA, SEMA, and SK KMA.

``` mediawiki
<div style="background:var(--ijc-card); border:1px solid var(--ijc-border); border-top:4px solid var(--ijc-red); padding:20px; border-radius:4px; margin-bottom:20px;">
  <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; color:var(--ijc-red);">Regulatory Repository Entity</span>
  <h2 style="color:var(--ijc-navy); margin:4px 0 12px 0;">{{{regulation_title}}}</h2>
  <p><b>Regulation Number:</b> <code>{{{regulation_number}}}</code></p>
  <p><b>Promulgation Year:</b> {{{year}}} | <b>Status:</b> <span style="color:var(--ijc-green); font-weight:600;">{{{status|Active}}}</span></p>
  <div style="background:var(--ijc-background); padding:12px; margin-top:12px; border-left:4px solid var(--ijc-gold);">
    <b>Core Scope & Mandate:</b> {{{scope}}}
  </div>
</div>
<includeonly>
[[Category:Legal Framework]]
[[Category:Judicial Policy]]
</includeonly>
```

---

## Sources / Sumber

## Provenance / Provenans

[Arsitektur Wiki Vector 2022](https://judicialknowledge.miraheze.org/wiki/Category:Vector_2022_Architecture) [Repositori Pengetahuan](https://judicialknowledge.miraheze.org/wiki/Category:Knowledge_Repository) [Pusat Pengetahuan Peradilan](https://judicialknowledge.miraheze.org/wiki/Category:Judicial_Knowledge)

---

*Source:* [JPAIS:ARCH:VECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT](https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT) on the Judicial Knowledge Hub wiki, revision 1031 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS:ARCH:VECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-4-KNOWLEDGE-CONTENT  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
