---
title: "JPAIS:REFORM-PROPOSAL:KCCP-REF-001-SK-SIPP"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS%3AREFORM-PROPOSAL%3AKCCP-REF-001-SK-SIPP
revision_id: 937
last_edited: 2026-09-15T04:13:40Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS:REFORM-PROPOSAL:KCCP-REF-001-SK-SIPP

## Summary / Ringkasan

## ID

JPAIS:REFORM-PROPOSAL:KCCP-REF-001-SK-SIPP

## Entity Ingestion / Ingesti Entitas

- Entity ID: KCCP-REF-001 (SK & SIPP Specification Extension)
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Draft Supreme Court Leadership Decree / Rancangan Keputusan Pimpinan Mahkamah Agung

- Title: RANCANGAN SURAT KEPUTUSAN KETUA MAHKAMAH AGUNG REPUBLIK INDONESIA NUMBER: \[XX\]/KMA/SK/\[MONTH\]/2026 CONCERNING THE PILOT IMPLEMENTATION OF TRIPARTITE CONCILIATION PANELS AND ORDERS IN LIEU OF SETTLEMENT (MAJELIS KONSILIASI TRIPARTIT DAN PENETAPAN PENGGANTI PERDAMAIAN) IN SELECTED FIRST-INSTANCE COURTS
- First Dictum (Establishment of Panels): Establishes the Tripartite Conciliation Panel comprising 1 Certified Judge Mediator (Panel Chair) and 2 Accredited Non-Judge Expert Commissioners for claims \> Rp 500 million.
- Second Dictum (Orders in Lieu of Settlement): Authorizes panels to issue provisional evaluative settlement orders (Penetapan Pengganti Perdamaian) upon impasse, which convert into binding Settlement Deeds (Akta Perdamaian) if no objection is filed within 14 calendar days.
- Third Dictum (Pilot Jurisdictions - KCCP-PILOT-001): 90-day pilot across 6 courts: PN Jakarta Pusat, PN Surabaya, PN Medan, PA Jakarta Selatan, PA Surabaya, and PA Malang.
- Fourth Dictum (Performance Metrics & System Integration): Mandates SIPP configuration for KPIs (PN settlement rate $\ge 25.0%$, PA property settlement rate $\ge 60.0%$, duration $\le 21$ days) and certification of 120 Expert Commissioners by BSDK Kumdil.

## SIPP Technical & Workflow Specification / Spesifikasi Teknis & Alur Kerja SIPP

- Workflow Architecture: \[e-Court Filing \> Rp 500M\] ──► \[SIPP Auto-Triaging Engine\] ──► \[Tripartite Session (\<= 21 Days)\] ──► \[Consensus -\> Akta Perdamaian OR Impasse -\> Penetapan Pengganti Perdamaian -\> 14-Day Objection Clock -\> Binding Deed or Trial\].
- Key Technical Modules:

` * Automated Expert Matching Algorithm: Matches dispute classifications with accredited Expert Commissioner registry tags.`  
` * Objection Clock Module: Triggers an automated 14-day countdown upon electronic delivery of the Penetapan Pengganti Perdamaian via e-Court.`  
` * Audit Dashboard: Tracks real-time Substantive Settlement Rates (SSR) and panel performance across pilot courts.`

## Related Entities / Entitas Terkait

- 

- 

- 

## Sources / Sumber

## Provenance / Provenans

---

*Source:* [JPAIS:REFORM-PROPOSAL:KCCP-REF-001-SK-SIPP](https://judicialknowledge.miraheze.org/wiki/JPAIS%3AREFORM-PROPOSAL%3AKCCP-REF-001-SK-SIPP) on the Judicial Knowledge Hub wiki, revision 937 (2026-09-15).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS:REFORM-PROPOSAL:KCCP-REF-001-SK-SIPP*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS%3AREFORM-PROPOSAL%3AKCCP-REF-001-SK-SIPP  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
