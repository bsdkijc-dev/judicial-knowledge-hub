---
title: "Digital forensics"
source_url: https://judicialknowledge.miraheze.org/wiki/Digital_forensics
revision_id: 27
last_edited: 2026-06-06T10:13:40Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Digital forensics

**Digital forensics** (sometimes known as **digital forensic science**) is a branch of [forensic science](https://judicialknowledge.miraheze.org/wiki/forensic_science) encompassing the recovery, investigation, examination, and analysis of material found in digital devices, often in relation to [cybercrime](https://judicialknowledge.miraheze.org/wiki/cybercrime). The term digital forensics was originally used as a synonym for *computer forensics* but has expanded to cover investigation of all devices capable of storing digital data (including mobile devices, cloud infrastructure, and IoT devices).

## History

Prior to the 1980s, crimes involving computers were dealt with using existing laws. The first computer crimes were recognized in the [Computer Fraud and Abuse Act](https://judicialknowledge.miraheze.org/wiki/Computer_Fraud_and_Abuse_Act) of 1986 in the United States. During the 1990s, the field grew organically as law enforcement agencies formed specialized units, such as the [FBI's](https://judicialknowledge.miraheze.org/wiki/Federal_Bureau_of_Investigation) Computer Analysis and Response Team (CART).

The term "digital forensics" emerged in the early 2000s as the discipline standardized under bodies like the International Organization for Standardization (ISO), leading to the publication of standards such as [ISO/IEC 27037](ISO-IEC_27037.md) for digital evidence handling.

## Forensic process

The digital forensic process is generally divided into several distinct phases, ensuring that investigations are repeatable and legally defensible.

### 1. Identification

The first step involves identifying potential sources of evidence, which may include desktop computers, smartphones, external storage media, and cloud application logs. Investigators must also identify volatility—data stored in [RAM](https://judicialknowledge.miraheze.org/wiki/Random-access_memory) that will be lost if the device loses power.

### 2. Preservation

Data must be isolated and preserved to prevent tampering or modification.

- **Live Acquisition:** Extracting volatile data (RAM) from a system while it is running.
- **Dead Acquisition:** Creating a bit-stream image of a storage device after it has been powered down.

Forensic software utilizes a verification process using [cryptographic hash functions](Cryptographic_hash_function.md). For an acquired data set $D$, the integrity is validated if the acquisition hash $h(D_{orig})$ matches the analysis hash $h(D_{copy})$.

### 3. Analysis

During analysis, the investigator recovers latent evidence using specialized software tools. Common techniques include:

- **File carving:** Reassembling files from raw data blocks based on file headers and footers, ignoring file system structures.
- **Keyword searching:** Scanning raw image files for specific strings or patterns.
- **Registry analysis:** Examining operating system configurations to identify user activity, connected hardware, and executed programs.

### 4. Reporting

The conclusions of the analysis are compiled into a formal report. The report must be detailed enough to allow another independent forensic examiner to replicate the steps and achieve identical results.

## Branches of digital forensics

Because the digital landscape is vast, the discipline is divided into several specialized sub-branches:

| Branch                 | Primary Focus                                           | Common Artifacts Evaluated                                                               |
|------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Computer Forensics** | Desktop systems, laptops, and local storage media.      | [File systems](https://judicialknowledge.miraheze.org/wiki/File_system) (NTFS, ext4), registry files, system logs.        |
| **Mobile Forensics**   | Smartphones, tablets, and wearable technology.          | Call logs, SMS text messages, [GPS](https://judicialknowledge.miraheze.org/wiki/GPS) coordinates, application data.       |
| **Network Forensics**  | Monitoring and analysis of network traffic.             | [Packet capture](https://judicialknowledge.miraheze.org/wiki/Packet_capture) (PCAP) files, firewall logs, proxy records.  |
| **Database Forensics** | Investigations targeting database management systems.   | Transaction logs, database files (e.g., MDF, DB), [SQL](https://judicialknowledge.miraheze.org/wiki/SQL) query histories. |
| **Cloud Forensics**    | Data residing in cloud environments (IaaS, PaaS, SaaS). | API access logs, virtual machine snapshots, cloud provider storage.                      |

## Legal admissibility

For digital evidence to be admitted in a court of law, it must satisfy strict legal guidelines. In the United States, evidence must pass the [Daubert standard](https://judicialknowledge.miraheze.org/wiki/Daubert_standard) or the [Frye standard](https://judicialknowledge.miraheze.org/wiki/Frye_standard), demonstrating that the forensic methods used are generally accepted within the scientific community.

Maintaining a flawless [chain of custody](Chain_of_custody.md)—documenting exactly who possessed, transferred, and analyzed the evidence at every second—is mandatory to prevent claims of evidence contamination.

## See also

- [Anti-forensics](Anti-forensics.md)
- [Chain of custody](Chain_of_custody.md)
- [Cryptographic hash function](Cryptographic_hash_function.md)
- [Information security](https://judicialknowledge.miraheze.org/wiki/Information_security)
- [Write blocker](Write_blocker.md)

## References

## External links

- [ISO/IEC 27037:2012 — Guidelines for identification, collection, acquisition and preservation of digital evidence](https://www.iso.org/standard/53033.html)

[Category:Digital forensics](https://judicialknowledge.miraheze.org/wiki/Category:Digital_forensics) [Category:Forensic science](https://judicialknowledge.miraheze.org/wiki/Category:Forensic_science) [Category:Computer security](https://judicialknowledge.miraheze.org/wiki/Category:Computer_security)

---

*Source:* [Digital forensics](https://judicialknowledge.miraheze.org/wiki/Digital_forensics) on the Judicial Knowledge Hub wiki, revision 27 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Digital forensics*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Digital_forensics  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
