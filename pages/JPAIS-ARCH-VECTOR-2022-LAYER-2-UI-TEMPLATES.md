---
title: "JPAIS:ARCH:VECTOR-2022-LAYER-2-UI-TEMPLATES"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-2-UI-TEMPLATES
revision_id: 1014
last_edited: 2026-09-16T02:03:28Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS:ARCH:VECTOR-2022-LAYER-2-UI-TEMPLATES

{{#tag:infobox\|\|title=Layer 2 UI Templates\|subheader=Modular Component Architecture\|image=<img src="bsdk.png" title="bsdk.png" width="200" alt="bsdk.png" />\|caption=Mahkamah Agung Corporate University Theme\|label1=Component Suite\|data1=Portal, Knowledge Cards, Infobox, Topic Header, Citation Box\|label2=Platform Target\|data2=Miraheze MediaWiki (Apex / Refreshed Skin)\|label3=Color Palette\|data3=<span style="color:#C62828;">Red</span>, <span style="color:#1565C0;">Blue</span>, <span style="color:#2E7D32;">Green</span>, <span style="color:#F57F17;">Gold</span>\|label4=Knowledge Grapher\|data4=Cecep Mustafa\|label5=Verification Status\|data5=VERIFIED}}

## Portal Navigation / Navigasi Institusional

- [Portal Utama](Main_Page.md)
- 
- 
- 

---

## Summary / Ringkasan

## Entity Ingestion / Ingesti Entitas

- Entity ID: JPAIS-ARCH-VECTOR-2022-LAYER-2-UI-TEMPLATES
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Description / Deskripsi

Layer 2 establishes the complete modular \*\*UI Templates Architecture\*\* for the Indonesian Judicial College (IJC) Wiki. Designed to be pasted directly into Miraheze system pages and templates, this layer standardizes five core components: \*\*Portal Layouts\*\*, \*\*Knowledge Cards\*\*, \*\*Institutional Infoboxes\*\*, \*\*Topic Headers\*\*, and \*\*Citation Boxes\*\*.

---

## 1. Portal Template (\`Template:PortalLayout\`)

Used to structure landing pages across the six core institutional domains (Knowledge, Academy, Research, Policy, Repository, About).

``` mediawiki
<div class="ijc-portal-wrapper" style="max-width:1200px; margin:0 auto; padding:16px;">
  <div style="background:linear-gradient(135deg, var(--ijc-navy) 0%, var(--ijc-navy-light) 100%); color:#FFF; padding:40px; border-radius:6px; border-bottom:4px solid var(--ijc-gold); margin-bottom:24px;">
    <h1 style="color:#FFF; border:none; margin:0 0 8px 0; font-size:2rem;">{{{portal_title}}}</h1>
    <p style="font-size:1.1rem; margin:0; opacity:0.9;">{{{portal_subtitle}}}is</p>
  </div>
  {{{portal_content}}}
</div>
<includeonly>
[[Category:Portal]]
</includeonly>
```

---

## 2. Knowledge Card Component (\`Template:KnowledgeCard\`)

Reusable component for displaying structured previews of research papers, regulations, and comparative studies.

``` mediawiki
<div class="ijc-knowledge-card" style="background:var(--ijc-card); border:1px solid var(--ijc-border); border-top:4px solid {{{accent_color|var(--ijc-navy)}}}; border-radius:4px; padding:16px; margin-bottom:16px;">
  <span class="ijc-card-badge" style="display:inline-block; font-size:0.7rem; font-weight:700; text-transform:uppercase; padding:2px 8px; border-radius:2px; margin-bottom:8px; background:rgba(18,59,93,0.08); color:var(--ijc-navy);">{{{badge_text|Knowledge}}}</span>
  <h3 style="margin:4px 0 8px 0; font-size:1.1rem;"><[[--title_link--|{{{title}}}]]></h3>
  <p style="font-size:0.9rem; color:var(--ijc-text-muted); margin-bottom:12px;">{{{description}}}</p>
  <div style="font-size:0.8rem; display:flex; justify-content:space-between; border-top:1px solid var(--ijc-border); padding-top:8px; color:var(--ijc-text-muted);">
    <span>Jurisdiction: {{{jurisdiction|Indonesia}}}</span>
    <span>ID: <code>{{{entity_id}}}</code></span>
  </div>
</div>
```

---

## 3. Institutional Infobox System (\`Template:InfoboxInstitutional\`)

Standardized summary panel for legal instruments, institutional entities, and reform proposals.

``` mediawiki
<div class="ijc-infobox" style="float:right; clear:right; margin:0 0 16px 24px; background:var(--ijc-card); border:1px solid var(--ijc-border); border-top:4px solid var(--ijc-navy); width:320px; font-size:0.9rem; padding:12px; border-radius:4px;">
<table style="width:100%; border-collapse:collapse;">
  <tr>
    <th colspan="2" style="text-align:center; background:var(--ijc-navy); color:#FFF; font-size:1rem; padding:10px;">
      {{{title}}}
    </th>
  </tr>
  <tr>
    <td><b>Entity Type</b></td>
    <td>{{{entity_type}}}</td>
  </tr>
  <tr>
    <td><b>Jurisdiction</b></td>
    <td>{{{jurisdiction}}}</td>
  </tr>
  <tr>
    <td><b>Knowledge Grapher</b></td>
    <td>{{{knowledge_grapher|Cecep Mustafa}}}</td>
  </tr>
  <tr>
    <td><b>Verification Status</b></td>
    <td><span style="color:var(--ijc-green); font-weight:600;">{{{verification_status|VERIFIED}}}</span></td>
  </tr>
</table>
</div>
```

---

## 4. Topic Header Component (\`Template:TopicHeader\`)

Provides a consistent, authoritative title banner for major subject pages and legal domains.

``` mediawiki
<div style="border-bottom: 2px solid var(--ijc-border); margin-bottom: 20px; padding-bottom: 12px;">
  <span style="font-size:0.75rem; font-weight:700; text-transform:uppercase; color:var(--ijc-gold); letter-spacing:0.05em;">{{{domain_label}}}</span>
  <h1 style="color:var(--ijc-navy); margin:4px 0 0 0; border:none; font-size:1.75rem;">{{{topic_title}}}</h1>
</div>
```

---

## 5. Citation Box Component (\`Template:CitationBox\`)

Standardized box for academic and legal reference attribution, ensuring AI engines and researchers extract precise provenance data.

``` mediawiki
<div style="background:var(--ijc-background); border:1px solid var(--ijc-border); border-left:4px solid var(--ijc-gold); padding:16px; border-radius:4px; font-size:0.9rem; margin:20px 0;">
  <b>Suggested Citation:</b><br/>
  Mustafa, Cecep. (2026). <i>{{{document_title}}}</i>. Indonesian Judicial College, Mahkamah Agung Corporate University Knowledge Base. Retrieved from <code>{{{url}}}</code>.
</div>
```

---

## Sources / Sumber

## Provenance / Provenans

---

*Source:* [JPAIS:ARCH:VECTOR-2022-LAYER-2-UI-TEMPLATES](https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-2-UI-TEMPLATES) on the Judicial Knowledge Hub wiki, revision 1014 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS:ARCH:VECTOR-2022-LAYER-2-UI-TEMPLATES*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-2-UI-TEMPLATES  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
