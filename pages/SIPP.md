---
title: "SIPP"
source_url: https://judicialknowledge.miraheze.org/wiki/SIPP
revision_id: 81
last_edited: 2026-08-27T06:47:25Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# SIPP

## Knowledge Metadata

- **Title:** SIPP (Sistem Informasi Penelusuran Perkara): Case Management System, Electronic Docketing, and Court Caseflow Architecture
- **Canonical Topic:** SIPP (Case Information Tracking System)
- **Topic Type:** System / Case Management Software / Judicial Workflow Infrastructure
- **Jurisdiction:** Indonesia
- **Legal Domain:** Legal Informatics, Court Administration, Civil & Criminal Procedure, Caseflow Management
- **Status:** Stable Architecture / Active National Case Management Standard
- **Last Reviewed:** 2026-08-27
- **Next Review Recommended:** 2027-08-27
- **Primary Sources:** Law No. 48/2009 (Judicial Power), PERMA No. 1/2019 jo. PERMA No. 7/2022 (Electronic Case Administration and Court Hearings), Supreme Court Case Management Directives, Directorate General of General Court Administration SIPP Operational Standards.
- **Related Wiki Pages:** [Judicial Knowledge Hub](Judicial_Knowledge_Hub.md), [Electronic Court Administration (e-Court)](Electronic_Court_Administration_-e-Court.md), [Direktori Putusan](Direktori_Putusan.md), [Supreme Court of Indonesia (Mahkamah Agung RI)](Supreme_Court_of_Indonesia_-Mahkamah_Agung_RI.md), [Center for Legal and Judicial Policy Strategy (Pustrajak)](Center_for_Legal_and_Judicial_Policy_Strategy_-Pustrajak.md), [Master System Design Blueprint](Master_System_Design_Blueprint.md)

## Core Definition

- - SIPP\*\* (\*Sistem Informasi Penelusuran Perkara\* or \*\*Case Information Tracking System\*\*) is the official internal case management, electronic docketing, and workflow tracking software deployed across all first-instance and appellate courts in Indonesia to manage active litigation lifecycles, judicial scheduling, document archiving, and real-time performance reporting.

<!-- -->

- \*\*Simple Definition:\*\* The official software system used by court clerks and judges across Indonesia to manage court files, track active lawsuits, schedule hearings, and record every step of a trial.
- \*\*Legal / Technical Definition:\*\* The centralized relational database and caseflow management architecture that tracks dockets from initial filing to final disposition, serving as the operational backbone for court administration, automated performance analytics, and data ingestion into the e-Court portal and Direktori Putusan.
- \*\*Plain-Language Explanation: **It acts as the digital "nerve center" of every district and high court, ensuring that no case file gets lost, hearings are scheduled without conflict, and court supervisors can monitor how quickly judges resolve disputes.**

## Why It Matters

- \*\*Eliminates Paper Docket Bottlenecks:\*\* Replaces manual ledgers with a centralized digital ledger, allowing clerks, judges, and litigants to track case status instantly.
- \*\*Enforces Procedural Deadlines:\*\* Tracks statutory timelines for filing answers, submitting evidence, and issuing verdicts, helping courts prevent backlogs.
- \*\*Powers National Jurimetric Analytics:\*\* Feeds real-time operational data to the Supreme Court and Pustrajak, enabling data-driven evaluations of court performance and case clearance rates.
- \*\*Connects Seamlessly with e-Court and Direktori Putusan:\*\* Acts as the central data engine that bridges electronic filings (\*e-Filing\*) with public judgment publishing (\*Direktori Putusan\*).

## Key Principles

Principle of Comprehensive Caseflow Transparency (Asas Transparansi Arus Perkara Menyeluruh)  

- \*\*Meaning:\*\* Every procedural action, hearing date, and minute entry must be recorded in SIPP in real time, ensuring complete traceability of the litigation lifecycle.
- \*\*Why It Matters:\*\* Prevents administrative tampering, file manipulation, and secret docket alterations.
- \*\*Legal Basis / Source:\*\* PERMA No. 1/2019 jo. PERMA No. 7/2022; Supreme Court Caseflow Management Directives.
- \*\*Related Concepts:\*\* Electronic docketing, audit trail, case tracking.

Principle of Integrated Administrative Interoperability (Asas Interoperabilitas Administratif Terpadu)  

- \*\*Meaning:\*\* SIPP must interface seamlessly with external portals (such as e-Court, e-Berpadu, and the Direktori Putusan) to eliminate redundant data entry.
- \*\*Why It Matters:\*\* Reduces administrative burdens on court staff and prevents data discrepancies across systems.
- \*\*Legal Basis / Source:\*\* Master System Design Blueprint; SPBE Interoperability Standards.
- \*\*Related Concepts:\*\* API integration, data synchronization, e-Court architecture.

Principle of Performance Accountability (Asas Akuntabilitas Kinerja Hakim dan Panitera)  

- \*\*Meaning:\*\* Case disposition times, trial delays, and backlog metrics recorded in SIPP directly inform institutional performance evaluations and supervisory audits.
- \*\*Why It Matters:\*\* Encourages judicial efficiency and discourages unwarranted trial procrastination.
- \*\*Legal Basis / Source:\*\* Supreme Court Supervisory Directives (Badan Pengawasan); SIPP Performance Dashboards.
- \*\*Related Concepts:\*\* Clearance rate, casebacklog monitoring, administrative discipline.

## Legal / Institutional Framework

    1945 Constitution of the Republic of Indonesia (Judicial Authority & Administration)
           ↓
    Law No. 48 of 2009 on Judicial Power (Principle of Fast, Simple, and Low-Cost Justice)
           ↓
    Supreme Court Regulations on Electronic Administration (PERMA No. 1/2019 jo. PERMA No. 7/2022)
           ↓
    SIPP (Sistem Informasi Penelusuran Perkara) Core Infrastructure:
    - First-Instance District Court & Religious Court Database Nodes
    - Appellate High Court Review Modules
    - API Sync with e-Court Portal & Direktori Putusan
           ↓
    National Monitoring via Supreme Court Case Management Dashboard & Pustrajak Jurimetrics

## Indonesia Section

- \*\*Institutional Deployment:\*\* Installed across thousands of courtrooms spanning the General Courts (\*Peradilan Umum\*), Religious Courts (\*Peradilan Agama\*), and State Administrative Courts (\*PTUN\*).
- \*\*Core Functional Modules within SIPP:\*\*

1\. \*Case Registration & Docketing:\* Recording plaintiff claims, defendant responses, case fees (\*e-SKUM\*), and initial case numbering. 2. \*Trial Scheduling & Calendar Management:\* Automated courtroom calendar assignment preventing double-booking of judges. 3. \*Minute Entry & Document Archiving (\*Berita Acara Sidang\*):\* Storing hearing notes, exhibits, and judge-signed final verdicts. 4. \*Appellate Elevation & Transmittal (\*Bндеberkasan\*):\* Packaging electronic case bundles for transfer to High Courts and the Supreme Court.

- \*\*Nomenclature:\*\* SIPP (\*Sistem Informasi Penelusuran Perkara\*) — \*Case Information Tracking System\*; Managemen Perkara Pengadilan — \*Court Case Management\*.

## Comparative Perspective

| Jurisdiction       | National Case Management System (CMS)                    | Governing Institution                                      | Core Functional Integration                                                     | Public Transparency Access                                                     |
|--------------------|----------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Indonesia**      | \*\*SIPP\*\* (Sistem Informasi Penelusuran Perkara)      | Supreme Court of Indonesia (Directorate General of Courts) | Integrated with e-Court, e-Berpadu, and Direktori Putusan.                      | Public case tracking portal allowing litigants to view docket progress online. |
| **United States**  | \*\*CM/ECF\*\* (Case Management / Electronic Case Files) | Administrative Office of the U.S. Courts (AOUSC)           | Unified federal electronic docketing and document filing system.                | Accessible via PACER and CourtListener repositories.                           |
| **Singapore**      | \*\*eLitigation System\*\*                               | Singapore State Courts & Supreme Court (CrimsonLogic)      | End-to-end electronic filing, case management, and virtual hearing integration. | Integrated litigant portal with secure document access rules.                  |
| **European Union** | Various National CMS linked via \*\*e-CODEX\*\*          | European Commission & National Ministries of Justice       | Cross-border judicial cooperation and document exchange.                        | Decentralized national portals linked through EU e-Justice infrastructure.     |

## Core Workflow of SIPP in District Courts

    ┌─────────────────────────────────────────────────────────────┐
    │ 1. INITIAL FILING & REGISTRATION (Pendaftaran Perkara)      │
    │ • e-Court filing or direct registry input creates SIPP dockets│
    │ • Automated assignment of case number and presiding judges  │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ 2. SCHEDULING & TRIAL MANAGEMENT (Jadwal Persidangan)       │
    │ • Automated courtroom calendar entry for mediation & trial  │
    │ • Issuance of electronic summons (e-Summons)                │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ 3. PROCEEDING & MINUTE RECORDING (Pencatatan Sidang)        │
    │ • Clerks log hearing notes, evidence exhibits, & motions    │
    │ • Judges upload interim orders and final verdicts           │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ 4. ARCHIVING & DIREKTORI PUTUSAN SYNC                       │
    │ • Finalized verdicts automatically flow to Direktori Putusan│
    │ • Archival locking or electronic dossier transmittal (Banding)│
    └─────────────────────────────────────────────────────────────┘

## Important Decisions & Technical Milestones

- Decision: Supreme Court Administrative Mandate on Universal SIPP Utilization

` * *Issuing Body:* Mahkamah Agung RI (Office of the Chief Justice & Secretary General)`  
` * *Instrument Reference:* SK KMA on Mandatory SIPP Docketing & Caseflow Enforcement`  
` * *Legal Principle:* All court units nationwide must execute all case registration, scheduling, and document recording exclusively through SIPP; maintaining parallel manual ledgers is strictly prohibited.`  
` * *Why It Matters:* Standardized digital court case management across the entire country.`  
` * *Official Source:* Mahkamah Agung Administrative Directives.`

## Key Legislation & Standards

- Instrument: Supreme Court Regulation on Electronic Case Administration

` * *Number / Year:* PERMA No. 1 of 2019 jo. PERMA No. 7 of 2022`  
` * *Jurisdiction:* Indonesia`  
` * *Status:* In force`  
` * *Relevant Provisions:* Mandates the mandatory utilization of electronic case management systems (SIPP) and e-Court portals for all civil, religious, and administrative litigation.`  
` * *Official Source:* Mahkamah Agung Official Gazette.`

## Timeline

| Date           | Milestone / Technological Event             | Significance                                                                                              |
|----------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **2011-09-14** | Introduction of Early SIPP Prototypes       | Began replacing fragmented local software with a standardized national case tracking system.              |
| **2018-04-05** | Integration with e-Court (PERMA 3/2018)     | Linked SIPP directly with online electronic filing portals for the first time.                            |
| **2022-11-15** | Upgraded Integration under PERMA No. 7/2022 | Standardized nationwide e-Litigation workflows, connecting SIPP with remote video hearings and e-Berpadu. |
| **2026-08-01** | Integration with RAG Knowledge Pipelines    | Connected SIPP historical analytics with Pustrajak research databases and judicial policy suites.         |

## Debates & Controversies

- Debate: Centralized Real-Time SIPP Monitoring vs. Regional Infrastructure Limitations

` * *Position A (Strict Centralized Oversight):* Real-time monitoring of SIPP data is essential to eradicate hidden backlogs and ensure judges meet disposition deadlines.`  
` * *Position B (Infrastructure Realities in Remote Regions):* Unstable internet connectivity and frequent power outages in remote island courts make rigid real-time online SIPP synchronization difficult for local clerks.`  
` * *Evidence:* Technical support tickets from remote district courts regarding network latency.`  
` * *Current Status:* Resolved through hybrid database synchronization protocols: local offline caching combined with automated background data sync when network connections are active.`

## Rule-of-Law Connection

- \*Administrative Predictability:\* Litigants can track exactly when their hearings are scheduled and what documents have been filed.
- \*Prevention of Corruption:\* Transparent digital dockets eliminate opportunities for corrupt clerks to backdate filings or manipulate case assignments.
- \*Judicial Accountability:\* Supervisory bodies (\*Badan Pengawasan\*) use SIPP analytics to audit judge productivity and trial speeds objectively.

## AI & Future of Law

- \*Predictive Case Duration Analytics:\* Utilizing machine learning models on historical SIPP data to predict how long a specific type of commercial or civil dispute will take to resolve.
- \*Automated Docket Auditing:\* AI algorithms scanning SIPP logs to detect unusual patterns, such as unexplained trial continuances or irregular judge reassignments.
- \*Smart Hearing Scheduling:\* AI-driven scheduling assistants optimizing courtroom calendars to prevent scheduling conflicts across busy district court benches.

## Common Misconceptions

- \*Myth:\* SIPP is a public website where ordinary citizens can read full trial transcripts and witness testimonies.

` * *Reality:* SIPP is primarily a *case management and tracking tool* for court administration and litigants; full final verdicts are published publicly on the *Direktori Putusan*, not inside SIPP.`  
` * *Source:* Supreme Court IT System Architecture.`

- \*Myth:\* Judges type their court rulings directly inside the SIPP software interface.

` * *Reality:* Judges draft decisions using word processing software and upload the finalized, signed electronic document into SIPP for docket archiving and Direktori Putusan syndication.`  
` * *Source:* Court Caseflow Workflows.`

## Practical Example

- \*Scenario:\* A civil plaintiff in Medan files a breach of contract lawsuit electronically via e-Court.
- \*Question:\* How does SIPP process the filing from intake to trial assignment?
- \*Applicable Principle:\* Electronic Docketing & Caseflow Integration (PERMA 7/2022; SIPP Architecture).
- \*Analysis:\*

` 1. The electronic filing submitted via e-Court automatically ingests into the district court's SIPP database.`  
` 2. SIPP generates a unique case registration number and queues the file for automated or chief-judge-assigned judicial panel distribution.`  
` 3. The system generates an electronic court fee assessment (*e-SKUM*). Once paid, SIPP schedules the initial mediation and trial dates, issuing automated electronic summons (*e-Summons*) to both parties.`

- \*Limitation:\* If the electronic submission lacks required document signatures or correct jurisdictional metadata, SIPP flags the error, requiring the filing lawyer to correct and resubmit.

## Key Terms

| Term                                 | Definition                                                                                                                      | Related Term                      |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| **SIPP**                             | \*Sistem Informasi Penelusuran Perkara\* — the official internal case management and tracking system used by Indonesian courts. | Case Management, e-Court          |
| **e-SKUM**                           | \*Elektronik Surat Kuasa Untuk Membayar\* — the electronic court fee calculation and payment slip generated within SIPP.        | Court Costs, Filing               |
| **e-Summons (Panggilan Elektronik)** | Electronic summons issued through SIPP and e-Court notifying parties of upcoming hearing dates.                                 | Service of Process, PERMA 7/2022  |
| **Clearance Rate**                   | The statistical ratio of resolved cases compared to incoming new cases, tracked via SIPP analytical dashboards.                 | Judicial Performance, Jurimetrics |

## Related Wiki Pages

- [Judicial Knowledge Hub](Judicial_Knowledge_Hub.md)
- [Electronic Court Administration (e-Court)](Electronic_Court_Administration_-e-Court.md)
- [Direktori Putusan](Direktori_Putusan.md)
- [Supreme Court of Indonesia (Mahkamah Agung RI)](Supreme_Court_of_Indonesia_-Mahkamah_Agung_RI.md)
- [Center for Legal and Judicial Policy Strategy (Pustrajak)](Center_for_Legal_and_Judicial_Policy_Strategy_-Pustrajak.md)
- [Master System Design Blueprint](Master_System_Design_Blueprint.md)

## Knowledge Relationships

- **SIPP** → \*is managed by\* → [Supreme Court of Indonesia (Mahkamah Agung RI)](Supreme_Court_of_Indonesia_-Mahkamah_Agung_RI.md)
- **SIPP** → \*feeds data to\* → [Direktori Putusan](Direktori_Putusan.md) & [Center for Legal and Judicial Policy Strategy (Pustrajak)](Center_for_Legal_and_Judicial_Policy_Strategy_-Pustrajak.md)
- **SIPP** → \*integrated with\* → [Electronic Court Administration (e-Court)](Electronic_Court_Administration_-e-Court.md) & [Master System Design Blueprint](Master_System_Design_Blueprint.md)
- **SIPP** → \*governed by\* → [PERMA No. 1/2019 jo. PERMA No. 7/2022](PERMA_No._1-2019_jo._PERMA_No._7-2022.md) & [Law No. 48/2009](https://judicialknowledge.miraheze.org/wiki/Law_No._48/2009)
- **SIPP** → \*supports audit functions of\* → [Strategic Governance Framework (Badan Pengawasan)](https://judicialknowledge.miraheze.org/wiki/Strategic_Governance_Framework_%28Badan_Pengawasan%29)

## Sources

### Tier 1 — Official / Primary Sources

1.  Law No. 48 of 2009 on Judicial Power (*Lembaran Negara RI Tahun 2009 No. 157*).
2.  Supreme Court Regulation (PERMA) No. 1 of 2019, as amended by Supreme Court Regulation (PERMA) No. 7 of 2022 on Electronic Case Administration and Court Hearings.
3.  Directorate General of General Courts, \*Sistem Informasi Penelusuran Perkara (SIPP) Operational Manual and Administrator Guidelines\*, Mahkamah Agung RI.

### Tier 2 — Academic & Institutional Sources

1.  Mahkamah Agung RI, \*Laporan Tahunan MA RI (Annual Performance Report)\*, Mahkamah Agung RI.
2.  Pustrajak Mahkamah Agung RI, \*Analisis Big Data SIPP untuk Evaluasi Kinerja Pengadilan dan Efisiensi Arus Perkara\*, 2026.
3.  Institute for Independent Judiciary (LeIP), \*Assessment of Court Case Management Systems and SIPP Implementation in Indonesia\*.

## Update Log

| Date           | Status  | Change Summary                                               | Source / Authority                                 | Editor                       |
|----------------|---------|--------------------------------------------------------------|----------------------------------------------------|------------------------------|
| **2026-08-27** | **NEW** | Canonical master wiki knowledge baseline generated for SIPP. | Mahkamah Agung RI / Pustrajak Master Wiki Standard | Judicial Knowledge Architect |

## Review Status

- **Current Status:** Active & Verified
- **Review Trigger:** Major software upgrades to SIPP architecture, revisions to PERMA electronic court regulations, or new Supreme Court administrative integration mandates.

## SEO & AI Metadata

- **SEO Title:** SIPP: Case Management System & Court Caseflow Architecture \| Hub
- **Meta Description:** Definitive wiki reference for SIPP (Sistem Informasi Penelusuran Perkara) covering Indonesia's court case management system, electronic docketing, and SIPP.
- **Primary Entity:** SIPP (Sistem Informasi Penelusuran Perkara)
- **Primary Topic:** Case Management System, Electronic Docketing, and Court Caseflow Architecture
- **Alternative Terms:** Sistem Informasi Penelusuran Perkara, Court Case Tracking System Indonesia, SIPP Mahkamah Agung.
- **Questions Answered:**
  - What is SIPP (Sistem Informasi Penelusuran Perkara) and how does it function as a case management system?
  - How does SIPP integrate with the e-Court portal, Direktori Putusan, and Supreme Court supervisory audits?
  - What procedural milestones and caseflow modules are tracked within SIPP across Indonesian courts?

---

*Source:* [SIPP](https://judicialknowledge.miraheze.org/wiki/SIPP) on the Judicial Knowledge Hub wiki, revision 81 (2026-08-27).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *SIPP*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/SIPP  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
