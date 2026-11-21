---
title: "IJC:IJC-BHT-001"
source_url: https://judicialknowledge.miraheze.org/wiki/IJC%3AIJC-BHT-001
revision_id: 2282
last_edited: 2026-10-09T20:42:49Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
redactions: "1 example case number(s) replaced with CONTOH placeholders"
---

# IJC:IJC-BHT-001

# Pembuktian Integritas File Melalui Cryptographic Hash SHA-256

| ID               | IJC-BHT-001                                        |
|------------------|----------------------------------------------------|
| Mode             | MODE 1 — BHT KNOWLEDGE                             |
| Chamber / Domain | PIDANA / Pidana Khusus / Cybercrime                |
| Reference        | Putusan No. CONTOH-01/Pid.Sus/2026/PN.CONTOH (BHT) |
| Confidentiality  | PUBLIC                                             |
| Review status    | PASS                                               |
| Verified         | Cecep Mustafa, 2026-09-18 00:00:00                 |

## Definition

Message digest 256-bit untuk memvalidasi konsistensi data bit-per-bit sejak baseline akuisisi (NIST FIPS 180-4 / Bab 4-5).

## Established

Integritas bit data tidak berubah sejak baseline hash dicatat.

## Supported inference

Forensic image identik dengan bitstream saat akuisisi.

## Unknown / not established

Kebenaran isi file, motif pelaku, atau legalitas cara perolehan.

## Atomic claims

- **IJC-CLM-0001** (LEGAL_RULE, PASS): Nilai Cryptographic Hash SHA-256 membuktikan konsistensi bit stream, bukan kebenaran isi file.
  - IJC-EVD-001 \[RAW, PASS\]: Physical Bitstream Clone SSD Workstation Procurement
- **IJC-CLM-0002** (FACT, PASS): Forensic duplicate SSD procurement terjaga utuh tanpa modifikasi stempel waktu sistem.
  - IJC-EVD-001 \[RAW, PASS\]: Physical Bitstream Clone SSD Workstation Procurement

## Related questions

- IJC-Q-0001: Apakah nilai hash SHA-256 yang identik otomatis membuktikan kebenaran isi dokumen atau pembuatnya?

[Category:IJC Knowledge Objects](https://judicialknowledge.miraheze.org/wiki/Category:IJC_Knowledge_Objects) [Category:MODE_1_BHT_KNOWLEDGE](https://judicialknowledge.miraheze.org/wiki/Category:MODE_1_BHT_KNOWLEDGE)

---

*Source:* [IJC:IJC-BHT-001](https://judicialknowledge.miraheze.org/wiki/IJC%3AIJC-BHT-001) on the Judicial Knowledge Hub wiki, revision 2282 (2026-10-09).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *IJC:IJC-BHT-001*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/IJC%3AIJC-BHT-001  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
