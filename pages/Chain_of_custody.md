---
title: "Chain of custody"
source_url: https://judicialknowledge.miraheze.org/wiki/Chain_of_custody
revision_id: 37
last_edited: 2026-06-06T10:31:06Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Chain of custody

The **chain of custody** is the chronological, written, and verifiable documentation that records the sequence of custody, control, transfer, analysis, and disposition of physical or electronic evidence. Maintaining an unbroken chain of custody is a fundamental requirement in [criminal procedure](https://judicialknowledge.miraheze.org/wiki/criminal_procedure), [forensic science](https://judicialknowledge.miraheze.org/wiki/forensic_science), and [digital forensics](Digital_forensics.md).

Because evidence must be presented in a court of law to establish guilt or liability, the presenting party must be able to prove that the evidence collected from the crime scene is identical to the evidence being introduced at trial. Any unaccounted-for gap or discrepancy in this timeline constitutes a "break" in the chain, which can result in the evidence being ruled [inadmissible](Admissible_evidence.md).

## The forensic lifecycle

The chain of custody begins the exact moment an investigator or law enforcement officer identifies and secures an item at a crime scene. The process follows a strict sequential workflow:

### 1. Collection and labeling

Upon seizure, each piece of evidence is assigned a unique tracking identifier. Physical items are placed in tamper-evident packaging (such as evidence bags), while digital items are isolated to prevent remote modification (e.g., using [Faraday bags](https://judicialknowledge.miraheze.org/wiki/Faraday_bag) or disabling network interfaces). A primary label is affixed to the container, detailing:

- Unique case number and item number.
- Exact date, time, and geographic location of recovery.
- Name and signature of the seizing officer.
- Detailed description of the item (including serial numbers or model makes).

### 2. Documentation of transfer

Every time the evidence changes physical location or passes from one individual to another, the transfer must be logged immediately. The documentation must explicitly capture:

- The date and time of the transfer.
- The name and signature of the person relinquishing the item.
- The name and signature of the person receiving the item.
- The explicit reason for the transfer (e.g., "transport to evidence vault", "forensic extraction", or "court exhibit presentation").

### 3. Storage and security

When not actively undergoing analysis, evidence must be retained in a secure, climate-controlled environment with restricted access, such as an evidence locker or a dedicated forensic lab vault. Log sheets monitor access to these storage areas, documenting who entered, when, and for what purpose.

## Application in digital forensics

In [digital forensics](Digital_forensics.md), proving the chain of custody faces unique technical hurdles due to the volatile and easily replicable nature of digital data.

To maintain an unassailable digital chain of custody, investigators utilize specific software and mathematical safeguards:

- **Bit-stream imaging:** Investigators never perform analysis on the original storage drive. Instead, they use hardware [write blockers](Write_blocker.md) to create a bit-stream duplicate (an exact forensic image) of the media.
- **Cryptographic validation:** The moment data is acquired, a [cryptographic hash function](Cryptographic_hash_function.md) (such as SHA-256) is run against the media to generate a unique digital signature. This process is mathematically expressed as:

$$H = h(\text{Evidence})$$ Before any forensic tool processes the data or presents findings, the hash is re-calculated. If the original acquisition hash matches the analysis hash, it proves with mathematical certainty that the data has not been modified, altered, or corrupted.

## Legal implications of a broken chain

In a legal proceeding, the burden of proof lies on the party introducing the evidence to show that proper safeguarding was maintained.

If a defendant can show that an item was left unattended in an unlocked room, that a digital file was accessed without a write blocker, or that a signature is missing from the transfer log, the integrity of that evidence is compromised. Depending on the severity of the oversight, the judge may suppress the item entirely under rules of evidence, or allow it to be admitted while instructing the jury that its reliability is highly suspect, drastically undermining its [probative value](https://judicialknowledge.miraheze.org/wiki/probative_value).

## See also

- [Admissible evidence](Admissible_evidence.md)
- [Digital forensics](Digital_forensics.md)
- [Cryptographic hash function](Cryptographic_hash_function.md)
- [Write blocker](Write_blocker.md)
- [Expert witness](https://judicialknowledge.miraheze.org/wiki/Expert_witness)

## References

[Category:Evidence law](https://judicialknowledge.miraheze.org/wiki/Category:Evidence_law) [Category:Criminal procedure](https://judicialknowledge.miraheze.org/wiki/Category:Criminal_procedure) [Category:Forensic science](https://judicialknowledge.miraheze.org/wiki/Category:Forensic_science) [Category:Digital forensics](https://judicialknowledge.miraheze.org/wiki/Category:Digital_forensics)

---

*Source:* [Chain of custody](https://judicialknowledge.miraheze.org/wiki/Chain_of_custody) on the Judicial Knowledge Hub wiki, revision 37 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Chain of custody*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Chain_of_custody  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
