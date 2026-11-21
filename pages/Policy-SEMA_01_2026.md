---
title: "Policy:SEMA 01 2026"
source_url: https://judicialknowledge.miraheze.org/wiki/Policy%3ASEMA_01_2026
revision_id: 47
last_edited: 2026-06-06T10:57:07Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Policy:SEMA 01 2026

\_\_NOTOC\_\_ \_\_NOEDITSECTION\_\_

|                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="Gavel-icon.png" title="valign=middle|link=" width="36" alt="valign=middle|link=" /> SUPREME COURT CIRCULAR LETTER (SEMA) • OFFICIAL DIRECTIVE |

# SEMA No. 1 of 2026: Remote Signature Validation

**Circular Reference:** SEMA-2026-001-RSV • **Effective Date:** January 15, 2026 • **Classification:** Binding Procedural Regulation

## 1. Background and Purpose

With the rapid integration of electronic litigation frameworks (e-Court) across all jurisdictions, ensuring the integrity and non-repudiation of judicial documents signed outside physical court boundaries is paramount. This Circular Letter provides uniform standards for the validation, cryptographic checking, and courtroom admission of documents utilizing remote electronic signatures.

## 2. Legal Framework

This directive acts as an administrative enforcement framework supplementary to:

- **Law on Electronic Information and Transactions (UU ITE):** Requirements for certified electronic signatures.
- **Supreme Court Regulation (PERMA) on Electronic Case Management:** Extending e-Court protocols to remote validation loops.

## 3. Core Validation Protocol

Every electronic judicial product (including judgments, decrees, warrants, and formal mandates) signed remotely must satisfy a three-tier validation workflow before being entered into the official case repository.

| Validation Stage                        | Requirement Metrics                                                                                                                | Failure Protocol                                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| **1. Certificate Authority (CA) Check** | Signature must be verified via a recognized, licensed Certificate Authority. Self-signed certificates are strictly void.           | Document rejected immediately; flagged for manual re-signing.                                      |
| **2. Cryptographic Hash Match**         | The document's SHA-256 hash upon retrieval must match the hash recorded at the exact timestamp of signature deployment.            | Automatic lockout. The case file is quarantined under suspicion of unauthorized text modification. |
| **3. Biometric / Multi-Factor Tie**     | The remote signatory (Judge or Registrar) must clear hardware-bound multi-factor verification (MFA) within 120 seconds of signing. | Signature session expires. Requires structural re-authentication.                                  |

## 4. Handling Verification Discrepancies

In the event that an electronic signature fails validation during a live trial presentation or automated file processing:

1.  **Immediate Suspension:** The affected legal instrument is temporarily suspended from active proceedings. No enforcement actions or legal mandates may proceed based on a unverified or broken signature loop.
2.  **Official Hash Log Comparison:** The IT Division must extract the metadata log file and manually cross-reference the local database hash against the Certificate Authority's timestamped master block.
3.  **Secondary Authentication:** If a network interruption caused the validation failure, the judicial officer must execute a secondary physical or hardware-bound token validation on a secure intranet terminal.

## 5. Cloud Restrictions & Data Sovereignty

- **Local Storage Mandate:** Caching or passing unencrypted PDF court binaries through third-party commercial public clouds during the signature loop is strictly prohibited.
- **Dedicated Servers:** All validation routines must route exclusively through localized district server instances or the secure, dedicated Supreme Court national cloud environment.

<div class="judicial-notice" style="background-color: #0f213f; color: #ffffff; border-left: 4px solid #c5a059; padding: 15px; margin-top: 30px; border-radius: 4px; font-size: 0.9em; font-family: sans-serif;">

**Security Directive:** Unauthorized tampering with electronic signature verification tools or attempting to bypass CA validation loops constitutes gross professional misconduct and is subject to immediate disciplinary actions under the Judicial Integrity Code.

</div>

[Category:Supreme Court Circular Letters](https://judicialknowledge.miraheze.org/wiki/Category:Supreme_Court_Circular_Letters) [Category:Digital Evidence Standards](https://judicialknowledge.miraheze.org/wiki/Category:Digital_Evidence_Standards) [Category:PERMA SEMA Development](https://judicialknowledge.miraheze.org/wiki/Category:PERMA_SEMA_Development) [Category:Judicial Knowledge Hub](https://judicialknowledge.miraheze.org/wiki/Category:Judicial_Knowledge_Hub)

---

*Source:* [Policy:SEMA 01 2026](https://judicialknowledge.miraheze.org/wiki/Policy%3ASEMA_01_2026) on the Judicial Knowledge Hub wiki, revision 47 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Policy:SEMA 01 2026*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Policy%3ASEMA_01_2026  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
