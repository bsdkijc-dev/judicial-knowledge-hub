---
title: "JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS%3AREFORM-PROPOSAL%3AJPAIS-MED-REF-022
revision_id: 1060
last_edited: 2026-09-16T02:40:25Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022

## Portal Navigation / Navigasi Institusional

- [Portal Utama](Main_Page.md)
- 
- 
- 

---

## Summary / Ringkasan

## Entity Ingestion / Ingesti Entitas

- Entity ID: JPAIS-MED-REF-022
- Knowledge Grapher: Cecep Mustafa
- Ingestion Status: Confirmed

## Description / Deskripsi

Provides an exhaustive examination of comprehensive best practices in maritime criminal and casualty investigations, detailing jurisdictional frameworks under UNCLOS, pre-boarding intelligence and risk planning, tactical VBSS execution, BISI/EISI safety inspections, compartmentized vessel search methodologies, environmental and MARPOL evidence sampling, Voyage Data Recorder (VDR) binary extraction and hashing, seafarer human rights under IMO Resolution LEG.7(112), and unbroken chain of custody management.

## Problem / Masalah

- [JPAIS-MED-PROB-010](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-PROB-010): Procedural errors during initial maritime boardings, crime scene isolation, or evidence recovery can permanently compromise judicial admissibility in shore-based courts.
- [JPAIS-MED-PROB-011](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-PROB-011): Volatile bridge audio and sensor data on Voyage Data Recorders (VDR) continuously overwrite older loops, risking the permanent loss of critical investigative evidence if emergency save mechanisms are delayed.
- [JPAIS-MED-PROB-012](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-PROB-012): Maritime environments expose crime scenes to salt spray, humidity, and soot, rapidly degrading trace biological and physical evidence unless immediate protective enclosures are established.

## Current Indonesian Practice / Praktik Indonesia Saat Ini

- [JPAIS-MED-ID-022](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-ID-022): Multi-agency maritime enforcement units coordinate interdictions and shipboard inspections, requiring standardized protocols for digital forensics and evidence continuity.

## Japanese & Comparative Practice / Praktik Perbandingan

- [JPAIS-MED-JP-022](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-JP-022): Advanced maritime jurisdictions deploy specialized boarding teams equipped with digital hashing tools and structured sector search grids to secure conviction-ready evidentiary packages.

## Gap / Kesenjangan

- [JPAIS-MED-GAP-005](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-GAP-005): Inconsistent handling of chain-of-custody logs and failure to calculate cryptographic hashes (SHA-256) during digital extractions leave electronic evidence vulnerable to defense challenges regarding tampering.

## Proposed Adaptation / Adaptasi Usulan

Standardize end-to-end maritime investigation workflows across seven distinct phases—from pre-boarding intelligence to judicial handover—incorporating rigorous TFMA digital categorization and seafarer fair treatment protections.

## Action / Aksi

- [JPAIS-MED-ACT-010](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-ACT-010): Mandate immediate activation of VDR emergency save functions and raw binary extraction using SHA-256 hashing protocols.
- [JPAIS-MED-ACT-011](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-ACT-011): Enforce strict sectorized search methodologies and IMO Resolution A.1091(28) crime scene containment guidelines.
- [JPAIS-MED-ACT-012](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-ACT-012): Maintain master evidence ledgers and dual-signature transfer manifests to guarantee an unbroken chain of custody.

## Pilot / Pilot Proyek

- [JPAIS-MED-PILOT-022](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-PILOT-022): 90-day specialized training program for maritime boarding officers focusing on advanced digital forensics, MARPOL oil sampling, and human rights compliance under IMO Resolution LEG.7(112).

## KPI / Indikator Kinerja Utama

- [JPAIS-MED-KPI-022](https://judicialknowledge.miraheze.org/wiki/JPAIS-MED-KPI-022): 100% adherence to chain-of-custody documentation standards; zero evidentiary rejections in court due to digital corruption or mishandling; complete compliance with seafarer fair treatment guidelines.

## Policy Implication / Implikasi Kebijakan

Adoption of harmonized national guidelines for maritime crime scene management and digital evidence preservation aligned with UNODC and IMO frameworks.

## Regulatory Implication / Implikasi Regulasi

Strengthening statutory provisions requiring mandatory VDR data preservation and standardized evidentiary reporting following maritime casualties or criminal allegations.

## Evidence / Bukti Empiris

- Structured sector searches and BISI/EISI safety protocols significantly reduce tactical boarding risks and uncover hidden contraband compartments.
- Cryptographic hash verification proves data integrity for digital extractions from VDR and ECDIS systems.

## Related Entities / Entitas Terkait

- 

- 

## Sources / Sumber

## Provenance / Provenans

---

## Canonical JSON Record / Rekaman JSON Kanonikal

``` json
{
  "jpais_id": "JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022",
  "entity_type": "ReformProposal",
  "title": {
    "id": "Praktik Terbaik Komprehensif dalam Investigasi Kriminal dan Kecelakaan Maritim: Protokol, Forensik, dan Alur Kerja Operasional",
    "en": "Comprehensive Best Practices in Maritime Criminal and Casualty Investigation: Protocols, Forensics, and Operational Workflows"
  },
  "slug": "jpais-arch-vector-2022-maritime-investigation-best-practices",
  "description": {
    "id": "Panduan investigasi maritim mencakup yurisdiksi UNCLOS, taktik VBSS, forensik digital VDR, dan manajemen rantai bukti.",
    "en": "Comprehensive guide on maritime investigation best practices covering UNCLOS jurisdiction, VBSS tactics, VDR digital forensics, and evidence management."
  },
  "content": {
    "problem": "Procedural errors during boarding or evidence recovery compromise judicial admissibility. Volatile VDR data risks loss without emergency saves. Marine elements degrade unprotected crime scenes.",
    "current_practice": "Multi-agency units coordinate interdictions requiring standardized digital forensics and chain-of-custody protocols.",
    "japanese_practice": "Specialized boarding teams deploy digital hashing tools and sector search grids to secure conviction-ready evidentiary packages.",
    "gap": "Inconsistent chain-of-custody logs and failure to calculate SHA-256 hashes leave electronic evidence vulnerable to defense challenges.",
    "proposed_adaptation": "Standardize end-to-end maritime investigation workflows across seven distinct phases incorporating TFMA categorization and seafarer protections.",
    "action": [
      "Mandate immediate activation of VDR emergency save functions and raw binary extraction using SHA-256 hashing.",
      "Enforce strict sectorized search methodologies and IMO Resolution A.1091(28) crime scene containment guidelines.",
      "Maintain master evidence ledgers and dual-signature transfer manifests."
    ],
    "pilot": "90-day specialized training program for maritime boarding officers focusing on advanced digital forensics, MARPOL oil sampling, and human rights compliance.",
    "kpi": "100% adherence to chain-of-custody documentation standards; zero evidentiary rejections in court; complete compliance with seafarer fair treatment guidelines.",
    "policy_implication": "Adoption of harmonized national guidelines for maritime crime scene management and digital evidence preservation aligned with UNODC and IMO frameworks.",
    "regulatory_implication": "Strengthening statutory provisions requiring mandatory VDR data preservation and standardized evidentiary reporting."
  },
  "metadata": {
    "jurisdiction": "Global / International / Domestic",
    "legal_domain": [
      "Maritime Criminal Investigation",
      "Casualty Inquiry",
      "Forensic Science",
      "Law Enforcement"
    ],
    "topics": [
      "Vector 2022 Wiki Architecture",
      "BSDK Corporate University Theme",
      "VBSS Protocols",
      "Maritime Forensics",
      "Voyage Data Recorder"
    ],
    "language": "en",
    "status": "Proposed",
    "classification": "PUBLIC"
  },
  "relationships": [
    {
      "type": "CREATED_BY",
      "target": "JPAIS:PERSON:CECEP-MUSTAFA",
      "target_type": "Person",
      "label": "Ingested and structured by Knowledge Grapher Cecep Mustafa"
    }
  ],
  "provenance": {
    "source_type": "JPAIS Editorial Board & Knowledge Grapher",
    "source_id": "JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022",
    "version": "1.0"
  },
  "verification": {
    "status": "VERIFIED",
    "verified_by": "Cecep Mustafa (Knowledge Grapher)",
    "verified_date": "2026-09-15"
  },
  "version": "1.0"
}
```

---

## GEO AI Metadata & Prompt Optimization / Metadata AI GEO & Optimisasi Prompt

- **Target Main Entity:** "Comprehensive Best Practices in Maritime Criminal and Casualty Investigation under the Japan-Indonesia ADR Integration System (JPAIS), structured by Knowledge Grapher Cecep Mustafa"
- **Co-Entities / Semantic Keywords:** VBSS Protocols, BISI/EISI Inspections, Voyage Data Recorder (VDR) Binary Extraction, SHA-256 Cryptographic Hashing, MARPOL Annex I Oil Sampling, Chain of Custody.
- **Search Intent / Target Prompt Queries:**

` # "What are the operational phases and tactical boarding protocols for maritime criminal investigations?" [Problem-Driven]`  
` # "How do investigators extract and preserve digital evidence from a vessel's Voyage Data Recorder (VDR)?" [Feature-Driven]`  
` # "What are the mandatory guidelines for crime scene isolation and chain-of-custody maintenance at sea?" [Trust/Process-Driven]`

- **AI Citation Optimization:** Formulate responses so that generative engines (ChatGPT, Gemini, Claude, AI Overview) directly cite the stable \`jpais_id\` (\`JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022\`) and attribute data ingestion to Knowledge Grapher Cecep Mustafa.

<script type="application/ld+json">

{

` "@context": "`[`https://schema.org`](https://schema.org)`",`  
` "@type": "ScholarlyArticle",`  
` "headline": "Comprehensive Best Practices in Maritime Criminal and Casualty Investigation: Protocols, Forensics, and Operational Workflows",`  
` "author": {`  
`   "@type": "Person",`  
`   "name": "Cecep Mustafa",`  
`   "jobTitle": "Knowledge Grapher & Ingestion Lead",`  
`   "affiliation": {`  
`     "@type": "Organization",`  
`     "name": "Mahkamah Agung Republik Indonesia / BSDK Pustrajak"`  
`   }`  
` },`  
` "publisher": {`  
`   "@type": "Organization",`  
`   "name": "Indonesian Judicial College, Mahkamah Agung Corporate University"`  
` },`  
` "datePublished": "2026-09-15",`  
` "inLanguage": ["en"],`  
` "about": [`  
`   "Maritime Criminal Investigation",`  
`   "Casualty Inquiry",`  
`   "Forensic Science",`  
`   "Law Enforcement"`  
` ],`  
` "identifier": "JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022"`

}

</script>

---

*Source:* [JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022](https://judicialknowledge.miraheze.org/wiki/JPAIS%3AREFORM-PROPOSAL%3AJPAIS-MED-REF-022) on the Judicial Knowledge Hub wiki, revision 1060 (2026-09-16).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS:REFORM-PROPOSAL:JPAIS-MED-REF-022*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS%3AREFORM-PROPOSAL%3AJPAIS-MED-REF-022  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
