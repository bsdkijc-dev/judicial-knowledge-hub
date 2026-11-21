---
title: "JPAIS:ARCH:VECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE
revision_id: 1024
last_edited: 2026-09-16T02:11:27Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS:ARCH:VECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE

{{#tag:infobox\|\|title=Layer 3 Semantic Structure\|subheader=Knowledge Graph & SMW Engine\|image=<img src="bsdk.png" title="bsdk.png" width="200" alt="bsdk.png" />\|caption=Mahkamah Agung Corporate University Theme\|label1=Semantic Engine\|data1=Semantic MediaWiki (SMW)\|label2=Core Functions\|data2=Properties, Forms, \#ask & \#show Queries\|label3=Platform Target\|data3=Miraheze MediaWiki Hosting\|label4=Knowledge Grapher\|data4=Cecep Mustafa\|label5=Verification Status\|data5=VERIFIED}}

## Portal Navigation / Navigasi Institusional

- [Portal Utama](Main_Page.md)
- 
- 
- 

---

## Summary / Ringkasan

## Entity Ingestion / Ingesti Entitas

- Entity ID: JPAIS-ARCH-VECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Description / Deskripsi

Layer 3 implements the \*\*Semantic Structure Architecture\*\* for the Indonesian Judicial College (IJC) Wiki. By leveraging Semantic MediaWiki (SMW) on Miraheze, this layer transforms static legal and institutional documents into a dynamic, queryable knowledge graph. It defines core semantic properties, category hierarchies, structured input forms, and dynamic \`#ask\` and \`#show\` query templates.

---

## 1. Core Semantic Properties Definition

To establish relational consistency across all knowledge entities, the following properties must be initialized in your wiki (by creating pages in the \`Property:\` namespace):

- \`[Property:Has jurisdiction::Text](https://judicialknowledge.miraheze.org/wiki/Property:Has_jurisdiction::Text)\` — Defines the legal jurisdiction (e.g., Indonesia, Japan, Global).
- \`[Property:Has legal domain::Page](https://judicialknowledge.miraheze.org/wiki/Property:Has_legal_domain::Page)\` — Links the article to its core legal domain category.
- \`[Property:Has entity ID::String](https://judicialknowledge.miraheze.org/wiki/Property:Has_entity_ID::String)\` — Canonical identifier (e.g., \`JPAIS:REFORM-PROPOSAL:018\`).
- \`[Property:Has verification status::String](https://judicialknowledge.miraheze.org/wiki/Property:Has_verification_status::String)\` — Verification state (\`VERIFIED\` / \`PENDING\`).
- \`[Property:Has knowledge grapher::Page](https://judicialknowledge.miraheze.org/wiki/Property:Has_knowledge_grapher::Page)\` — Attribution property pointing to the responsible ingestion lead (\`Cecep Mustafa\`).
- \`[Property:Has publication date::Date](https://judicialknowledge.miraheze.org/wiki/Property:Has_publication_date::Date)\` — Timestamps publication for chronological sorting.

---

## 2. Semantic Forms Integration (\`Special:Forms\`)

Structured data entry forms ensure that every Knowledge Grapher (led by Cecep Mustafa) inputs uniform metadata for regulations, reform proposals, and comparative studies.

``` mediawiki
<noinclude>
Form definition for ingesting JPAIS Reform Proposals and Institutional Knowledge Entities.
</noinclude>
<includeonly>
{{{for template|JPAIS Knowledge Record}}}
<div class="semantic-form-container" style="background:var(--ijc-background); padding:16px; border:1px solid var(--ijc-border);">
  <h3>JPAIS Institutional Knowledge Ingestion Form</h3>
  <p><b>Entity ID:</b> {{{field|Has entity ID|input type=text|size=40}}} </p>
  <p><b>Title (English):</b> {{{field|Title En|input type=text|size=60}}} </p>
  <p><b>Jurisdiction:</b> {{{field|Has jurisdiction|input type=dropdown|values=Indonesia, Japan, Global, International Maritime}}} </p>
  <p><b>Verification Status:</b> {{{field|Has verification status|input type=dropdown|values=VERIFIED, PENDING}}} </p>
  <p><b>Knowledge Grapher:</b> {{{field|Has knowledge grapher|default=Cecep Mustafa|readonly}}} </p>
</div>
{{{end template}}}
</includeonly>
```

---

## 3. Dynamic \#ask Query Component (Automated Knowledge Aggregation)

The following Semantic MediaWiki \`#ask\` query template automatically aggregates verified reform proposals and comparative studies into structured tables without manual index maintenance:

``` mediawiki
{{#ask: [[Category:Reform Proposals]] [[Has verification status::VERIFIED]]
| ?Title = Title
| ?Has jurisdiction = Jurisdiction
| ?Has entity ID = JPAIS ID
| ?Has knowledge grapher = Ingestion Lead
| format = table
| limit = 15
| sort = Modification date
| order = desc
| mainlabel = Knowledge Entity
}}
```

---

## 4. Semantic \#show Component (Inline Entity Attributes)

The \`#show\` function allows articles to pull specific metadata properties inline from other linked knowledge entities or parent governance records:

``` mediawiki
<div style="background:var(--ijc-card); border:1px solid var(--ijc-border); padding:12px; margin:12px 0; border-left:4px solid var(--ijc-navy);">
  <b>Quick Entity Attribute Lookup:</b><br/>
  Current Entity Jurisdiction: {{#show: {{PAGENAME}} | ?Has jurisdiction}}<br/>
  Assigned Knowledge Grapher: {{#show: {{PAGENAME}} | ?Has knowledge grapher}}
</div>
```

---

## Sources / Sumber

## Provenance / Provenans

---

*Source:* [JPAIS:ARCH:VECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE](https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE) on the Judicial Knowledge Hub wiki, revision 1024 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS:ARCH:VECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS%3AARCH%3AVECTOR-2022-LAYER-3-SEMANTIC-STRUCTURE  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
