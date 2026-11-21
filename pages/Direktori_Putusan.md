---
title: "Direktori Putusan"
source_url: https://judicialknowledge.miraheze.org/wiki/Direktori_Putusan
revision_id: 80
last_edited: 2026-08-27T06:46:13Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Direktori Putusan

## Knowledge Metadata

- **Title:** Direktori Putusan Mahkamah Agung: National Open Judicial Repository, Case Law Transparency, and Legal Informatics Portal
- **Canonical Topic:** Direktori Putusan (Supreme Court Judgment Directory)
- **Topic Type:** System / National Portal / Public Legal Repository
- **Jurisdiction:** Indonesia & Global Comparative
- **Legal Domain:** Legal Informatics, Open Government Data, Case Law, Judicial Transparency, Privacy & Data Protection
- **Status:** Stable Architecture / Active National Legal Repository
- **Last Reviewed:** 2026-08-27
- **Next Review Recommended:** 2027-08-27
- **Primary Sources:** 1945 Constitution of Indonesia (Art. 24), Law No. 14/2008 on Public Information Disclosure (UU KIP), Law No. 48/2009 on Judicial Power (Principle of Publicly Pronounced Trials), Law No. 27/2022 on Personal Data Protection (UU PDP), Supreme Court Guidelines on Judgment Publication and Anonymization, PERMA No. 1/2019 jo. PERMA No. 7/2022.
- **Related Wiki Pages:** [Judicial Knowledge Hub](Judicial_Knowledge_Hub.md), [Supreme Court of Indonesia (Mahkamah Agung RI)](Supreme_Court_of_Indonesia_-Mahkamah_Agung_RI.md), [Center for Legal and Judicial Policy Strategy (Pustrajak)](Center_for_Legal_and_Judicial_Policy_Strategy_-Pustrajak.md), [Master System Design Blueprint](Master_System_Design_Blueprint.md), [Court Modernization & Legal Informatics](Court_Modernization_-_Legal_Informatics.md), [Evidence-Based Judicial Policy](Evidence-Based_Judicial_Policy.md)

## Core Definition

- - Direktori Putusan\*\* is the official, publicly accessible national digital repository and open-data portal maintained by the Supreme Court of the Republic of Indonesia (\*Mahkamah Agung RI\*) that archives, indexes, anonymizes, and publishes millions of written judicial decisions and verdicts rendered across all four specialized court branches nationwide.

<!-- -->

- \*\*Simple Definition:\*\* The official online database where anyone can search, read, and download millions of court judgments and legal verdicts issued by judges across Indonesia.
- \*\*Legal / Technical Definition:\*\* The master web-based judicial information portal fulfilling statutory public transparency mandates (Law No. 14/2008 UU KIP and Law No. 48/2009), integrating automated text anonymization filters, structured metadata tagging, full-text search engines, and Application Programming Interfaces (APIs) for legal research and jurimetric analysis.
- \*\*Plain-Language Explanation:\*\* It acts as the ultimate open library of Indonesian case law, allowing citizens, lawyers, scholars, and judges to inspect past court rulings, track judicial precedents, and ensure transparency in how justice is administered.

## Why It Matters

- \*\*Guarantees Judicial Transparency:\*\* Upholds the constitutional and statutory mandate that all court trials and judgments must be pronounced openly to the public (\*sidang terbuka untuk umum\*).
- \*\*Fosters Jurisprudential Consistency:\*\* Enables lower court judges, legal practitioners, and scholars to study Supreme Court jurisprudence and regional appellate precedents, promoting uniform legal interpretation.
- \*\*Powers Evidence-Based Judicial Policy (Pustrajak):\*\* Serves as the primary big-data corpus for jurimetric studies, judicial performance evaluations, and empirical legal research.
- \*\*Protects Citizen Privacy via Anonymization:\*\* Implements strict data masking protocols to redact sensitive personal identifiers (such as national ID numbers, addresses, and victim details) in compliance with personal data protection laws.

## Key Principles

Principle of Open Public Access to Judicial Information (Asas Keterbukaan Informasi Peradilan)  

- \*\*Meaning:\*\* Except for cases strictly mandated by law to be closed to the public (e.g., juvenile matters, sexual assault victim details, or state secrets), all court judgments must be accessible to the public.
- \*\*Why It Matters:\*\* Essential democratic safeguard against corruption and secret tribunals.
- \*\*Legal Basis / Source:\*\* Law No. 14 of 2008 on Public Information Disclosure (UU KIP); Law No. 48 of 2009 Art. 13.
- \*\*Related Concepts:\*\* Open government data, public transparency, right to information.

Principle of Mandatory Privacy Redaction and Anonymization (Asas Anonimisasi Wajib Data Pribadi)  

- \*\*Meaning:\*\* Prior to publication in the Direktori Putusan, automated and manual redaction protocols must strip all identifying personal data of vulnerable litigants, witnesses, and minors.
- \*\*Why It Matters:\*\* Balances the public's right to legal transparency with the individual's constitutional right to privacy and personal data protection.
- \*\*Legal Basis / Source:\*\* Law No. 27 of 2022 on Personal Data Protection (UU PDP); Supreme Court Publication Guidelines.
- \*\*Related Concepts:\*\* Data masking, privacy protection, anonymization filters.

Principle of Jurisprudential Traceability (Asas Keterlacakan Yurisprudensi)  

- \*\*Meaning:\*\* Every judgment must be indexed with standardized metadata (case number, chamber type, presiding judge, legal category, and statutory articles applied) to enable exact legal cross-referencing.
- \*\*Why It Matters:\*\* Ensures legal researchers and judges can reliably track the historical evolution of specific legal doctrines.
- \*\*Legal Basis / Source:\*\* Supreme Court Informatics Standards; SEMA Chamber System Directives.
- \*\*Related Concepts:\*\* Case law indexing, metadata tagging, searchable legal repository.

## Legal / Institutional Framework

    1945 Constitution of the Republic of Indonesia (Right to Information & Open Trials)
           ↓
    Statutory Disclosure Mandates:
    - Law No. 14 of 2008 on Public Information Disclosure (UU KIP)
    - Law No. 48 of 2009 on Judicial Power (Open Pronouncement Principle)
    - Law No. 27 of 2022 on Personal Data Protection (UU PDP)
           ↓
    Supreme Court Administrative Directives & Publication Protocols:
    - Chief Justice Decrees on Judgment Upload Mandates for All Courts
    - Automated & Manual Anonymization Rules
           ↓
    Direktori Putusan Portal Architecture:
    - Ingestion from SIPP & Court Registries
    - NLP Anonymization & Metadata Indexing Pipeline
    - Public Search Interface & API Endpoints for Legal Research

## Indonesia Section

- \*\*Institutional Ownership:\*\* Managed directly by the Supreme Court of Indonesia (Bureau of Legal and Public Relations / \*Biro Hukum dan Humas\* in coordination with the IT Bureau and Pustrajak).
- \*\*Scope and Scale:\*\* The repository archives millions of rulings spanning the four judicial branches: General Courts (\*Peradilan Umum\*), Religious Courts (\*Peradilan Agama\*), State Administrative Courts (\*PTUN\*), and Military Courts (\*Peradilan Militer\*), ranging from first-instance district courts to supreme cassation decisions.
- \*\*Integration with Caseflow Management:\*\* The portal is directly fed by the Court Case Tracking System (\*Sistem Informasi Penelusuran Perkara / SIPP\*). Once a judge finalizes and signs a verdict, the electronic document flows through the anonymization pipeline before publishing on the public portal.
- \*\*Nomenclature:\*\* Direktori Putusan Mahkamah Agung — \*Supreme Court Judgment Directory\*; Portal Putusan Terbuka — \*Open Judgment Portal\*.

## Comparative Perspective

| Jurisdiction       | National Judgment Repository Portal                        | Governing Law / Standard                                              | Anonymization & Privacy Standard                                                            | Public Access Level                                                                     |
|--------------------|------------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Indonesia**      | \*\*Direktori Putusan MA\*\* (putusan.mahkamahagung.go.id) | Law No. 14/2008 (UU KIP) & Law No. 48/2009.                           | Mandatory redaction of names, addresses, and IDs under UU PDP and Supreme Court guidelines. | Free public access for all published decisions across all four court branches.          |
| **United States**  | \*\*CourtListener / RECAP / PACER\*\*                      | E-Government Act of 2002 & Federal Rules of Civil Procedure Rule 5.2. | Parties must redact sensitive data (SSNs, minor names, financial accounts) before filing.   | PACER fee-based access; free archival platforms like CourtListener and RECAP.           |
| **Singapore**      | \*\*SG Courts — LawNet & Judgments Portal\*\*              | Supreme Court of Judicature Act & Public Sector (Governance) Act.     | Automated masking of sensitive personal details in family and juvenile proceedings.         | Free public judgments portal alongside subscription-based professional LawNet services. |
| **European Union** | \*\*CURIA & EUR-Lex\*\*                                    | EU Regulation on Public Access to Documents & GDPR.                   | Strict GDPR compliance; pseudonymization of individuals in sensitive or criminal cases.     | Free multilingual public access to all Court of Justice (CJEU) judgments.               |

## Core Operational Pipeline of Direktori Putusan

    ┌─────────────────────────────────────────────────────────────┐
    │ 1. UPLOAD & INGESTION FROM SIPP                             │
    │ • Finalized judge-signed Word/PDF verdicts uploaded via SIPP│
    │ • Automatic association with case metadata (Case No., Judge)│
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ 2. NLP ANONYMIZATION & PRIVACY REDACTION                    │
    │ • Automated software scans text for NIK, names, & addresses │
    │ • Replacement with pseudonyms (e.g., Terdakwa A, Saksi B)   │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ 3. METADATA INDEXING & FULL-TEXT SEARCH PARSING             │
    │ • Tagging legal domains (Civil, Criminal, Corruption, HKI)  │
    │ • Indexing statutory articles cited within the ruling       │
    └──────────────────────────────┬──────────────────────────────┘
                                   │
                                   ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ 4. PUBLICATION & RAG VECTOR EMBEDDINGS                      │
    │ • Instant deployment to public putusan.mahkamahagung.go.id  │
    │ • Vector embedding ingestion for Judicial Knowledge Hub RAG │
    └──────────────────────────────┬──────────────────────────────┘

## Important Decisions & Regulatory Milestones

- Decision: Supreme Court Administrative Mandate on Universal Judgment Publication

` * *Issuing Body:* Mahkamah Agung RI (Office of the Chief Justice)`  
` * *Instrument Reference:* SK KMA (Supreme Court Decree) on Mandatory Judgment Uploads`  
` * *Legal Principle:* Every first-instance, appellate, and supreme court unit nationwide must upload their finalized written judgments to the Direktori Putusan within statutory time limits following verdict pronouncement.`  
` * *Why It Matters:* Eliminated localized information hoarding and transformed Indonesian jurisprudence into a fully searchable national database.`  
` * *Official Source:* Mahkamah Agung Official Gazette.`

## Key Legislation & Standards

- Instrument: Law on Public Information Disclosure (UU KIP)

` * *Number / Year:* Law No. 14 of 2008`  
` * *Jurisdiction:* Indonesia`  
` * *Status:* In force`  
` * *Relevant Provisions:* Mandates that state institutions proactively publish public documents, including court decisions, while protecting personal privacy.`  
` * *Official Source:* State Gazette of the Republic of Indonesia.`

- Instrument: Law on Personal Data Protection (UU PDP)

` * *Number / Year:* Law No. 27 of 2022`  
` * *Jurisdiction:* Indonesia`  
` * *Status:* In force`  
` * *Relevant Provisions:* Mandatory protection of personal data identifiers during public institutional data publishing.`

## Timeline

| Date           | Milestone / Portal Evolution                   | Significance                                                                                            |
|----------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **2008-04-30** | Enactment of Law No. 14/2008 (UU KIP)          | Established the statutory right of public access to state documents and court rulings.                  |
| **2009-10-29** | Enactment of Law No. 48/2009 on Judicial Power | Reaffirmed open trial pronouncement principles and institutional transparency.                          |
| **2012-01-15** | Official Launch of Direktori Putusan Portal    | Centralized online publication of Supreme Court and lower court verdicts into a searchable web archive. |
| **2022-10-17** | Enactment of Law No. 27/2022 (UU PDP)          | Strengthened privacy redaction and anonymization requirements for public court document archives.       |

## Debates & Controversies

- Debate: Complete Openness vs. Privacy and Reputational Protection

` * *Position A (Radical Transparency Advocates):* Every detail of a trial, including unredacted names and corporate disputes, must be fully public to ensure accountability and expose judicial corruption.`  
` * *Position B (Privacy & Rehabilitation Advocates):* Overly accessible unredacted judgments can permanently stigmatize rehabilitated offenders, expose victims of crime, and compromise sensitive business trade secrets.`  
` * *Evidence:* Ongoing debates regarding Google indexing of old criminal verdicts and the right to be forgotten.`  
` * *Current Status:* Regulated through strict anonymization guidelines: while the legal reasoning and outcome remain transparent, personal identifiers of vulnerable parties are masked in compliance with UU PDP.`

## Rule-of-Law Connection

- \*Judicial Transparency:\* Open access to judgments allows academic scholars, journalists, and civil society to audit judicial quality and impartiality.
- \*Legal Certainty:\* Lawyers and citizens can inspect how courts interpret specific statutes in similar past disputes.
- \*Public Accountability:\* Eliminates hidden judicial decisions and ensures the justice system operates under public scrutiny.

## AI & Future of Law

- \*RAG Integration with Judicial Knowledge Hub:\* The Direktori Putusan corpus serves as the core training and retrieval base for AI legal assistants supporting judges and policy analysts.
- \*Automated Jurimetric Case Analytics:\* Machine learning models analyzing millions of published verdicts to track sentencing trends, judicial disposition times, and regional statutory interpretation variances.
- \*Advanced Natural Language Redaction:\* Deploying state-of-the-art NLP models to automatically identify and mask sensitive personal data with 99.9% accuracy prior to publication.

## Common Misconceptions

- \*Myth:\* The Direktori Putusan contains only Supreme Court cassation rulings.

` * *Reality:* The repository hosts millions of judgments from *all tiers of the judiciary*, including district courts (*Pengadilan Negeri/Agama*), high courts (*Pengadilan Tinggi*), and the Supreme Court.`  
` * *Source:* Direktori Putusan Portal Architecture.`

- \*Myth:\* Publishing a court judgment online violates privacy laws.

` * *Reality:* Publishing judgments is a statutory duty under UU KIP and Law 48/2009, provided sensitive personal identifiers are properly anonymized in accordance with UU PDP.`  
` * *Source:* Law No. 14/2008; Law No. 27/2022.`

## Practical Example

- \*Scenario:\* A corporate lawyer in Surabaya needs to research how commercial courts interpret force majeure clauses in supply contracts following recent economic disruptions.
- \*Question:\* How does the lawyer utilize the Direktori Putusan to build the legal argument?
- \*Applicable Principle:\* Jurisprudential Traceability & Open Access (Direktori Putusan Portal).
- \*Analysis:\*

``  1. The lawyer accesses `putusan.mahkamahagung.go.id`. ``  
` 2. Uses advanced filters to search for commercial dispute verdicts (*Sengketa Perdata Niaga*) containing keywords like "force majeure" and Article 1245 Civil Code.`  
` 3. Reviews multiple appellate and Supreme Court rulings to identify consistent patterns in judicial reasoning (*ratio decidendi*).`  
` 4. Cites the relevant precedents in the legal brief.`

- \*Limitation:\* Published decisions serve as persuasive precedents and interpretive guides, but Indonesian law is primarily statute-based and does not operate under strict common law \*stare decisis\*.

## Key Terms

| Term                            | Definition                                                                                                                                      | Related Term                          |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| **Direktori Putusan**           | The Supreme Court's official online repository publishing millions of written court judgments from across Indonesia.                            | Open Data, Case Law                   |
| **Anonimisasi (Anonymization)** | The data protection process of masking or redacting personal identifiers (names, addresses, NIK) in published court documents.                  | UU PDP, Privacy Redaction             |
| **SIPP**                        | \*Sistem Informasi Penelusuran Perkara\* — the court case tracking system that feeds finalized electronic judgments into the Direktori Putusan. | Case Management, e-Court              |
| **Hak Uji Materiil**            | Material review; the Supreme Court mechanism for reviewing subordinate regulations against higher statutes using judicial precedent databases.  | Supreme Court Review, Legal Certainty |

## Related Wiki Pages

- [Judicial Knowledge Hub](Judicial_Knowledge_Hub.md)
- [Supreme Court of Indonesia (Mahkamah Agung RI)](Supreme_Court_of_Indonesia_-Mahkamah_Agung_RI.md)
- [Center for Legal and Judicial Policy Strategy (Pustrajak)](Center_for_Legal_and_Judicial_Policy_Strategy_-Pustrajak.md)
- [Master System Design Blueprint](Master_System_Design_Blueprint.md)
- [Court Modernization & Legal Informatics](Court_Modernization_-_Legal_Informatics.md)
- [Evidence-Based Judicial Policy](Evidence-Based_Judicial_Policy.md)

## Knowledge Relationships

- **Direktori Putusan** → \*is maintained by\* → [Supreme Court of Indonesia (Mahkamah Agung RI)](Supreme_Court_of_Indonesia_-Mahkamah_Agung_RI.md)
- **Direktori Putusan** → \*feeds data to\* → [Center for Legal and Judicial Policy Strategy (Pustrajak)](Center_for_Legal_and_Judicial_Policy_Strategy_-Pustrajak.md) & [Judicial Knowledge Hub](Judicial_Knowledge_Hub.md)
- **Direktori Putusan** → \*governed by\* → [Law No. 14/2008 (UU KIP)](https://judicialknowledge.miraheze.org/wiki/Law_No._14/2008_%28UU_KIP%29) & [Law No. 27/2022 (UU PDP)](https://judicialknowledge.miraheze.org/wiki/Law_No._27/2022_%28UU_PDP%29)
- **Direktori Putusan** → \*integrated with\* → [Master System Design Blueprint](Master_System_Design_Blueprint.md) & [SIPP](SIPP.md)
- **Direktori Putusan** → \*supports\* → [Evidence-Based Judicial Policy](Evidence-Based_Judicial_Policy.md) & [Court Modernization & Legal Informatics](Court_Modernization_-_Legal_Informatics.md)

## Sources

### Tier 1 — Official / Primary Sources

1.  1945 Constitution of the Republic of Indonesia (Article 24 on Judicial Power).
2.  Law No. 14 of 2008 on Public Information Disclosure (*UU KIP*).
3.  Law No. 48 of 2009 on Judicial Power (*Lembaran Negara RI Tahun 2009 No. 157*).
4.  Law No. 27 of 2022 on Personal Data Protection (*UU PDP*).
5.  Supreme Court of Indonesia, \*Direktori Putusan Official Portal (putusan.mahakamahagung.go.id)\*.

### Tier 2 — Academic & Institutional Sources

1.  Mahkamah Agung RI, \*Pedoman Publikasi dan Anonimisasi Putusan Pengadilan\*, Biro Hukum dan Humas MA RI.
2.  Pustrajak Mahkamah Agung RI, \*Analisis Big Data Direktori Putusan untuk Riset Jurimetrik dan Kebijakan Peradilan\*, 2026.
3.  Institute for Criminal Justice Reform (ICJR), \*Assessment of Judicial Transparency and Judgment Publication Standards in Indonesia\*.

## Update Log

| Date           | Status  | Change Summary                                                     | Source / Authority                                 | Editor                       |
|----------------|---------|--------------------------------------------------------------------|----------------------------------------------------|------------------------------|
| **2026-08-27** | **NEW** | Canonical wiki knowledge baseline generated for Direktori Putusan. | Mahkamah Agung RI / Pustrajak Master Wiki Standard | Judicial Knowledge Architect |

## Review Status

- **Current Status:** Active & Verified
- **Review Trigger:** Updates to national data protection regulations (UU PDP), revisions to public information disclosure laws, or major technical upgrades to the Direktori Putusan web portal.

## SEO & AI Metadata

- **SEO Title:** Direktori Putusan: Supreme Court Judgment Directory \| Indonesia Hub
- **Meta Description:** Definitive wiki reference for Direktori Putusan covering Indonesia's national open judicial repository, case law transparency, anonymization, and UU KIP.
- **Primary Entity:** Direktori Putusan
- **Primary Topic:** National Open Judicial Repository, Case Law Transparency, and Legal Informatics Portal
- **Alternative Terms:** Direktori Putusan Mahkamah Agung, Putusan MA RI Portal, Indonesian Case Law Database.
- **Questions Answered:**
  - What is the Direktori Putusan and how does it serve as Indonesia's national open judicial repository?
  - How do Law No. 14/2008 (UU KIP) and Law No. 27/2022 (UU PDP) govern judgment publication and anonymization?
  - How does the Direktori Putusan integrate with SIPP case tracking and support evidence-based judicial research?

---

*Source:* [Direktori Putusan](https://judicialknowledge.miraheze.org/wiki/Direktori_Putusan) on the Judicial Knowledge Hub wiki, revision 80 (2026-08-27).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Direktori Putusan*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Direktori_Putusan  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
