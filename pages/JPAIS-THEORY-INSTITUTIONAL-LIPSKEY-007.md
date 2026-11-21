---
title: "JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007"
source_url: https://judicialknowledge.miraheze.org/wiki/JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007
revision_id: 2143
last_edited: 2026-09-29T23:34:59Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007

# JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007

## 1. Source Verification

- **Selected Source:** "AI in Judicial Case Management" (Google Doc) \[1–33\].
- **Available Empirical Evidence in Source:**
  - **Global Systems & Deployments:** Brazil (*VICTOR* extraordinary appeal triage, *SOCRATES* precedent matching, *LARRY* claim clustering, *SOFIA* draft rulings); India (*SUPACE* record extraction, *SUVAS* 16-language judgment translation, *ICMIS* e-filing defect screening, Case Clearance Rate reaching 104.05% in early 2025); Argentina (*Prometea* social security/housing triage & draft assembly); Colombia (*PretorIA* constitutional *tutela* prioritization); Singapore (*CJTS / AGC Platform* small claims guided intake & memorial drafting); Denmark (*Domsdatabasen* NER pseudonymization); Finland (*ANOPPI* FinBERT de-identification); Canada (*Beagle+* plain-language intake); Alaska court triage tools.
  - **Judicial Precedents & Legal Rulings:** *Ishfaq Ahmed v. Mushtaq Ahmed* (Supreme Court of Pakistan, affirming non-delegable duty of judicial reasoning); *EDPS v. Single Resolution Board* (CJEU 2025, defining contextual re-identification and GDPR data controller duties); *Helmold & Mariya* (Australian Family Court), *Gummadi Usha Rani v. Sure Mallikarjuna Rao* (Supreme Court of India), and *Shahid v. Esaam* (US court sanctions for hallucinated AI citations).
  - **Supranational & Institutional Frameworks:** CEPEJ *European Ethical Charter on the Use of Artificial Intelligence in Judicial Systems* (5 core principles & Assessment Tool); EU AI Act (Regulation 2024/1689 Annex III Point 8 High-Risk classification, Recital 61 human authority protection, Art. 6(3) administrative exclusions, Art. 14 human oversight, Art. 27 FRIA); Vatican Guidelines on Judicial AI; CJEU *Artificial Intelligence Ethics Charter* (Jan 2026); Australia Federal Court *Generative AI Practice Note (GPN-AI)* (April 2026); England & Wales Judicial Guidance; Singapore Judiciary *Guide on the Use of Generative AI Tools*.
  - **Cognitive Science & Technical Architectures:** Neuro-symbolic AI & RAG pipelines with temporal/authority provenance; SHAP and LIME post-hoc feature attribution vs. ante-hoc glass-box decision-tree models; automation bias, cognitive anchoring, and "decision-before-assistance" workflow design \[20–22, 32\].
- **Methodological Distinction & Provenance:**
  - Empirical facts, jurisdictional data, court decisions, and regulatory instruments are directly grounded in source passages and cited with `[i]` \[1–33\].
  - Socio-legal theoretical models (Institutional Theory, Organizational Sociology, Street-Level Bureaucracy) are applied analytically to explain gaps between formal policy mandates and operational court practice. Synthesized theoretical links are marked `[THEORETICAL INFERENCE]`.

------------------------------------------------------------------------

## 2. Analytical Synthesis

### A. Conceptual Foundations & Actor Differentiation

#### 1. Judges vs. Court Administrators

- **Judges:**
  - *Institutional Role & Constitutional Authority:* Constitutionally appointed adjudicators holding non-delegable adjudicative authority (*Ishfaq Ahmed v. Mushtaq Ahmed*, EU AI Act Recital 61, Vatican Guidelines).
  - *Street-Level Bureaucracy Applicability & Limitations:* Judges are not traditional street-level bureaucrats; their authority is grounded in constitutional independence and separation of powers rather than administrative delegation. However, when exposed to pre-drafted summary orders, preliminary case categorizations, or algorithmic risk scores, judges operate under "street-level conditions" (caseload pressure, time scarcity, clearance speed monitoring).
  - *Behavioral Adaptation:* Overburdened judges exhibit **cognitive anchoring** and **automation bias**. When presented with automated draft orders or triage labels prior to independent evaluation, the machine output anchors the judge's baseline evaluation, requiring significantly higher cognitive effort to reject or modify than to adopt unchanged.
- **Court Administrators (Registrars, Clerks, Registry Officers):**
  - *Institutional Role & Discretion:* Executive and clerical personnel embedded in administrative hierarchies, evaluated on throughput metrics, document processing latency, and Case Clearance Rates (e.g., India's 104.05% CCR).
  - *Street-Level Bureaucracy Applicability:* Classic street-level bureaucrats directly interacting with incoming filings, law firm submissions, and self-represented litigants.
  - *Behavioral Adaptation:* Facing heavy intake queues and induced filing demand, administrators rely on automated defect screening tools (*ICMIS*, *VICTOR*) and layout parsing algorithms as operational coping mechanisms. Advisory defect flags are passively confirmed, turning ministerial intake into automated gatekeeping.

------------------------------------------------------------------------

### B. Causal Implementation Chain Analysis

`Policy Mandate → Formal Rule → Institutional Pressure → Organizational Interpretation → Constraints → Professional Norms → Discretion → Adaptation → Practice → Implementation Gap`

1.  **Policy Mandate:** High-level judicial modernization policies aiming to eliminate docket congestion, accelerate case disposition, and expand access to justice. `[SOURCE EVIDENCE]`
2.  **Formal Rule:** Supranational charters, statutory frameworks, and judicial practice notes (CEPEJ Ethical Charter, EU AI Act Art. 14/27, CJEU Ethics Charter, Australia GPN-AI) mandating active human-in-the-loop oversight, non-delegation of judicial reasoning, and transparent, explainable triage \[24–28\]. `[SOURCE EVIDENCE]`
3.  **Institutional Pressure:** Coercive pressure from massive backlogs (e.g., \>100 million cases in Brazil, long disposition timeframes) and institutional performance monitoring linked to Case Clearance Rates. `[SOURCE EVIDENCE / THEORETICAL INFERENCE]`
4.  **Organizational Interpretation:** Court leadership configures automated triage engines (*VICTOR*, *SUPACE*, *Prometea*, *PretorIA*) and e-filing defect rules to maximize registry clearance velocity \[2–4, 22\]. `[SOURCE EVIDENCE]`
5.  **Constraints:** Time scarcity, clerical understaffing, induced filing demand from consumer AI tools, and the influx of synthetic/hallucinated filings \[7–9, 20\]. `[SOURCE EVIDENCE]`
6.  **Professional Norms:** Judicial commitment to constitutional due process, individualized reasoning, and open justice vs. administrative commitment to queue clearance and dark-courtroom elimination. `[SOURCE EVIDENCE / THEORETICAL INFERENCE]`
7.  **Discretion:** Judges and registry clerks retain formal legal discretion to override automated recommendations, reclassify dockets, or accept non-standard filings. `[SOURCE EVIDENCE]`
8.  **Adaptation (Coping Mechanisms):** Overburdened personnel adopt automation bias and cognitive anchoring, confirming AI-generated draft orders, triage labels, and defect flags without independent re-examination \[20–22\]. `[SOURCE EVIDENCE / THEORETICAL INFERENCE]`
9.  **Practice:** De facto delegation of case triage, preliminary research, and defect filtering to software engines, where advisory algorithmic outputs act as unreviewed operational filters. `[SOURCE EVIDENCE / THEORETICAL INFERENCE]`
10. **Implementation Gap:** Divergence between formal policy mandates (strictly advisory AI preserving human judicial independence and due process) and daily operational practice (unreviewed algorithmic gatekeeping and cognitive offloading). `[SOURCE EVIDENCE / THEORETICAL INFERENCE]`

- **Divergence vs. Non-Compliance:** This gap represents **implementation divergence** (pragmatic organizational coping with extreme caseload volume and cognitive load) rather than **willful non-compliance** `[THEORETICAL INFERENCE]`.

------------------------------------------------------------------------

## 3. MediaWiki

``` mediawiki
{{JPAIS Institutional Analysis
| Stable ID = JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007
| Knowledge Grapher = [[User:Cecep_Mustafa|Cecep Mustafa]]
| Research Domain = Judicial Policy Implementation
| Theoretical Framework = Institutional Theory; Organizational Sociology; Street-Level Bureaucracy
| Verification = Source-Grounded Analysis (AI in Judicial Case Management)
}}

== Research Question ==
How do organizational constraints, professional norms, and street-level judicial and clerical practices generate implementation gaps between formal policy mandates for human-controlled AI case management and daily court operational reality?

== Institutional Theory ==
Judicial systems adopt artificial intelligence, Retrieval-Augmented Generation (RAG) pipelines, and automated triage engines to secure institutional legitimacy and demonstrate modernization in response to public demands for efficient justice. However, court organizations experience competing institutional logics: a legal-rational logic emphasizing constitutional due process, individual fair trial rights, and human judicial reasoning versus a managerial logic prioritizing docket velocity, backlog clearance, and automated workflow standardization. Court systems reconcile these conflicting pressures through structural decoupling, promulgating formal governance charters (e.g., CEPEJ Ethical Charter principles, EU AI Act Annex III High-Risk human oversight mandates) that guarantee human control, while relying in daily operations on automated classification engines and pre-drafted orders to handle expanding dockets.

== Organizational Sociology ==
Court organizations operate as structured hierarchies divided into judicial chambers and administrative registries. Formal procedural rules position AI case management platforms as auxiliary infrastructure for intake validation, precedent matching, and preliminary drafting. In daily practice, informal organizational routines reconfigure technology deployment. Driven by resource dependencies—such as staffing deficits, heavy filing backlogs, and strict Case Clearance Rate (CCR) metrics—court registries and chambers align daily workflows with automated triage outputs, transforming advisory software recommendations into standardized organizational channels that shape case files before formal judicial review occurs.

== Street-Level Bureaucracy ==
Applying Michael Lipsky's street-level bureaucracy framework, court registrars, registry clerks, and judicial officers operate under chronic time scarcity, heavy filing queues, and severe performance pressures. To cope with these operational burdens, frontline personnel adopt cognitive shortcuts and simplified routines. Automation bias operates as a primary street-level coping mechanism: overburdened clerks and judges display cognitive offloading, passively ratifying AI-generated procedural defect flags, preliminary case categorizations, and pre-drafted summary orders without conducting independent de novo verifications.

== Application to Courts ==
=== Judges ===
Judges possess constitutional authority and non-delegable adjudicative independence (affirmed in precedent such as Ishfaq Ahmed v. Mushtaq Ahmed), setting them apart from traditional street-level bureaucrats. However, when automated systems generate preliminary case categorizations, suggest bail risk classifications, or assemble draft orders, judges face pre-structured dockets. Under severe time constraints and performance monitoring, judges exhibit cognitive anchoring, accepting AI-generated draft recommendations as authoritative baselines prior to independent evaluation.

=== Court Administrators ===
Court registrars and registry clerks function as classic street-level bureaucrats embedded in administrative performance frameworks. Evaluated on processing latency and clearance speed, court staff rely on automated defect-screening tools and metadata extraction bots to manage incoming filings. While formal rules require human clerk confirmation before filing rejection, clerks routinely confirm automated system defect tags, turning ministerial document intake into automated gatekeeping.

== Formal Policy and Everyday Practice ==
Formal judicial policy mandates that AI case management tools remain strictly auxiliary, transparent, and subject to active human oversight (e.g., EU AI Act Article 14, CJEU Ethics Charter, Australia GPN-AI). In daily court practice, personnel default to automated system outputs to prevent backlog accumulation and handle induced filing demand. Consequently, formal safeguards—such as de novo human review of procedural defects and independent formulation of provisional judicial assessments—are routinely bypassed in favor of operational speed.

== Implementation Gap ==
The implementation gap emerges through a ten-stage causal process:
# Policy Mandate: Backlog elimination, digital access, and efficient case processing.
# Formal Rule: Mandatory human-in-the-loop oversight and non-delegation of judicial reasoning.
# Institutional Pressure: Massive backlogs, long disposition times, and Case Clearance Rate metrics.
# Organizational Interpretation: Deployment of automated triage engines and e-filing validation bots.
# Resource Constraints: Clerical understaffing, time scarcity, and induced filing volume from consumer AI tools.
# Professional Norms: Conflict between administrative efficiency and constitutional due process.
# Discretion & Adaptation: Routine clerical and judicial reliance on automated defect flags and AI draft orders.
# Practice & Gap: De facto automated gatekeeping and cognitive offloading, leading to unreviewed system determinations and procedural compression.

== Integrated Framework ==
The integrated framework connects Institutional Theory (legitimacy seeking and competing logics), Organizational Sociology (registry hierarchies and resource dependencies), and Street-Level Bureaucracy (clerical coping mechanisms and automation bias). External institutional pressures drive AI case management adoption; organizational routines embed technical processing into daily workflows; and street-level coping behaviors transform advisory software outputs into rigid operational filters, generating a systematic implementation gap between formal policy mandates and court practice.

== Alternative Explanations ==
* Technical Limits: Implementation gaps may stem from model interpretability challenges or post-hoc explanation limits (e.g., SHAP/LIME approximations) rather than organizational coping strategies.
* Training Shortages: Staff reliance on default software outputs may reflect inadequate technical training regarding automation bias and cognitive anchoring risks.
* Synthetic File Contamination: Processing delays may result from the influx of hallucinated citations and unverified consumer AI filings submitted by litigants rather than internal administrative failures.

== Limitations ==
* Constitutional Boundaries: Conceptualizing judges as street-level bureaucrats is constrained by their unique constitutional status and non-delegable adjudicative authority.
* Cross-Jurisdictional Variance: Operational impacts differ significantly between centralized supreme court ecosystems (e.g., Brazil STF, Supreme Court of India) and decentralized trial court systems.

== Research Implications ==
Future empirical research should evaluate the operational effectiveness of structural governance mechanisms, including "decision-before-assistance" interface design, mandatory Fundamental Rights Impact Assessments (FRIAs under EU AI Act Article 27), sovereign air-gapped data architectures, and independent judicial oversight councils auditing for model drift and procedural bias.

== JPAIS Metadata ==
* Stable ID: JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007
* Knowledge Grapher: [[User:Cecep_Mustafa|Cecep Mustafa]]
* Research Domain: Judicial Policy Implementation
* Theoretical Framework: Institutional Theory; Organizational Sociology; Street-Level Bureaucracy
* Primary Source: AI in Judicial Case Management

== Keywords ==
Judicial Policy Implementation, Street-Level Bureaucracy, Institutional Theory, Organizational Sociology, AI Judicial Case Management, Automation Bias, Cognitive Anchoring, Implementation Gap, Judicial Independence, Court Administration, Procedural Due Process.
```

------------------------------------------------------------------------

## 4. Semantic MediaWiki

``` mediawiki
[[Stable ID::JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007]]
[[Knowledge Grapher::Cecep Mustafa]]
[[Research Domain::Judicial Policy Implementation]]
[[Theoretical Framework::Institutional Theory]]
[[Theoretical Framework::Organizational Sociology]]
[[Theoretical Framework::Street-Level Bureaucracy]]
[[Actor::Judge]]
[[Actor::Court Administrator]]
[[Analytical Mechanism::Professional Discretion]]
[[Analytical Mechanism::Organizational Routine]]
[[Analytical Mechanism::Resource Constraint]]
[[Analytical Mechanism::Implementation Gap]]
[[Analytical Mechanism::Automation Bias]]
[[Analytical Mechanism::Competing Logics]]
[[Analytical Mechanism::Decoupling]]
[[Empirical Context::AI in Judicial Case Management]]
[[Governance Standard::CEPEJ European Ethical Charter]]
[[Governance Standard::EU AI Act Regulation 2024 1689]]
[[Governance Standard::CJEU AI Ethics Charter]]
[[Legal Precedent::Ishfaq Ahmed v Mushtaq Ahmed]]
[[Legal Precedent::EDPS v Single Resolution Board]]
```

------------------------------------------------------------------------

## 5. JSON-LD

``` json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "jpais": "https://judicialknowledge.miraheze.org/wiki/Property:",
    "stable_id": "jpais:Stable_ID",
    "knowledgeGrapher": "jpais:Knowledge_Grapher",
    "researchDomain": "jpais:Research_Domain",
    "theoreticalFramework": "jpais:Theoretical_Framework",
    "actor": "jpais:Actor",
    "analyticalMechanism": "jpais:Analytical_Mechanism"
  },
  "@type": "ScholarlyArticle",
  "@id": "https://judicialknowledge.miraheze.org/wiki/JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007",
  "name": "Institutional Theory, Organizational Sociology, and Street-Level Bureaucracy in AI-Supported Judicial Case Management",
  "stable_id": "JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007",
  "knowledgeGrapher": {
    "@type": "Person",
    "name": "Cecep Mustafa",
    "@id": "https://judicialknowledge.miraheze.org/wiki/User:Cecep_Mustafa"
  },
  "researchDomain": "Judicial Policy Implementation",
  "theoreticalFramework": [
    "Institutional Theory",
    "Organizational Sociology",
    "Street-Level Bureaucracy"
  ],
  "actor": [
    "Judge",
    "Court Administrator"
  ],
  "analyticalMechanism": [
    "Professional Discretion",
    "Organizational Routine",
    "Resource Constraint",
    "Implementation Gap",
    "Automation Bias",
    "Competing Logics",
    "Decoupling"
  ],
  "description": "An analysis of the implementation gap between formal judicial policy mandates for auxiliary, human-controlled AI case management and daily court operational practice, applying Institutional Theory, Organizational Sociology, and Street-Level Bureaucracy."
}
```

------------------------------------------------------------------------

## 6. RAG Metadata

| chunk_id                                    | parent_source_id               | stable_id                              | knowledge_grapher | topic                    | evidence_status                         | source_provenance                                                                                                                                                                                                    |
|---------------------------------------------|--------------------------------|----------------------------------------|-------------------|--------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH01 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Institutional Theory     | SOURCE EVIDENCE / THEORETICAL INFERENCE | Competing logics between constitutional due process/human adjudication and managerial docket velocity; structural decoupling of human oversight policy rules from daily workflows \[1, 10, 20, 24–26\].              |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH02 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Organizational Sociology | SOURCE EVIDENCE / THEORETICAL INFERENCE | Administrative court hierarchies and registry routines; resource dependencies driving reliance on automated triage engines (VICTOR, SUPACE, Prometea) and clearance rate metrics \[2–4, 6, 12, 20\].                 |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH03 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Street-Level Bureaucracy | SOURCE EVIDENCE / THEORETICAL INFERENCE | Clerical workload pressure, time scarcity, and induced filing volume driving automation bias and cognitive anchoring as street-level coping mechanisms \[7–8, 20–22\].                                               |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH04 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Judicial Application     | SOURCE EVIDENCE / THEORETICAL INFERENCE | Differentiating judges (constitutional authority, non-delegable judicial duty in Ishfaq Ahmed v. Mushtaq Ahmed, cognitive anchoring) from court administrators (classic street-level bureaucrats, defect screening). |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH05 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Implementation Gap       | SOURCE EVIDENCE / THEORETICAL INFERENCE | Ten-stage causal chain mapping the divergence from formal auxiliary mandates to automated de facto gatekeeping and cognitive offloading.                                                                             |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH06 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Integrated Framework     | THEORETICAL INFERENCE                   | Multi-level synthesis connecting macro-institutional pressures, meso-organizational registry routines, and micro street-level coping behaviors in judicial AI case management.                                       |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH07 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Limitations              | SOURCE EVIDENCE / THEORETICAL INFERENCE | Constitutional limits of treating judges as street-level bureaucrats; operational divergence between centralized sovereign court systems (Brazil STF, India e-Courts) and trial courts \[2–4, 19, 23\].              |
| JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007-CH08 | AI in Judicial Case Management | JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007 | Cecep Mustafa     | Research Implications    | SOURCE EVIDENCE / THEORETICAL INFERENCE | Empirical evaluation of structural governance mechanisms including decision-before-assistance workflow design, FRIAs under EU AI Act Article 27, sovereign air-gapped data architectures, and oversight councils.    |

------------------------------------------------------------------------

## 7. Quality Control

- **Identity & ID Inheritance:** Stable ID `JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007` and Knowledge Grapher (`[[User:Cecep_Mustafa|Cecep Mustafa]]` / `Cecep Mustafa`) are preserved identically across all 7 requested layers. IDs 001, 002, and 003 are omitted per instructions.
- **Source Grounding & Provenance:** All empirical facts, platforms (*VICTOR*, *SOCRATES*, *LARRY*, *SOFIA*, *SUPACE*, *SUVAS*, *Prometea*, *PretorIA*, *CJTS*, *Domsdatabasen*, *ANOPPI*, *Beagle+*), judicial rulings (*Ishfaq Ahmed v. Mushtaq Ahmed*, *EDPS v. Single Resolution Board*, *Helmold & Mariya*, *Gummadi Usha Rani*), and regulatory frameworks (CEPEJ Ethical Charter, EU AI Act Annex III / Art. 14 / Art. 27, Vatican Guidelines, CJEU AI Ethics Charter, Australia GPN-AI) are cited directly from the selected source text \[1–33\].
- **Theoretical Classification:** Empirical facts are marked `[SOURCE EVIDENCE]`, socio-legal mechanism applications are classified as `[THEORETICAL INFERENCE]`, and missing claims are flagged `[SOURCE VERIFICATION REQUIRED]`.
- **Actor Differentiation:** Judges (constitutional authority, non-delegable adjudicative duty, cognitive anchoring) and Court Administrators (hierarchical registry personnel, street-level coping via automated defect screening) are evaluated separately with explicit constitutional limits noted.
- **Schema Adherence:** Output contains strictly the 7 requested sections with validated MediaWiki, Semantic MediaWiki, JSON-LD, and pipe-delimited RAG chunk syntax.

---

*Source:* [JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007](https://judicialknowledge.miraheze.org/wiki/JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007) on the Judicial Knowledge Hub wiki, revision 2143 (2026-09-29).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/JPAIS-THEORY-INSTITUTIONAL-LIPSKEY-007  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
