---
title: "Data erasure"
source_url: https://judicialknowledge.miraheze.org/wiki/Data_erasure
revision_id: 29
last_edited: 2026-06-06T10:21:00Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Data erasure

**Data erasure** (sometimes referred to as **data sanitization**, **data clearing**, or **software overwriting**) is a software-based method of securely overwriting data that aims to completely destroy all electronic data residing on a [hard disk drive](https://judicialknowledge.miraheze.org/wiki/hard_disk_drive) (HDD), [solid-state drive](https://judicialknowledge.miraheze.org/wiki/solid-state_drive) (SSD), or other digital media.

Unlike simple file deletion or drive formatting—which only remove pointers to the data, leaving the actual files recoverable by [digital forensics](Digital_forensics.md) tools—true data erasure ensures that the target data is completely unrecoverable, rendering the storage medium safe for reuse, resale, or recycling.

## Mechanism

The fundamental mechanism of data erasure involves writing a stream of non-destructive data across every addressable sector of a storage device. Typically, this stream consists of binary zeroes (\`0x00\`), binary ones (\`0xFF\`), or completely random pseudo-noise patterns.

By overwriting the physical sectors, the residual magnetic or electrical charges that represented the original data are replaced. This process directly counters [file carving](https://judicialknowledge.miraheze.org/wiki/file_carving) and advanced laboratory hardware recovery techniques, such as magnetic force microscopy.

## Standards and protocols

Various government, military, and independent organizations have established standards for data erasure, defining the number of overwriting passes and the specific patterns required to certify a drive as sanitized.

| Standard                  | Origin                                         | Number of passes | Overwrite pattern sequence                                                                                                                                   |
|---------------------------|------------------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DoD 5220.22-M**         | U.S. Department of Defense                     | 3 passes         | Pass 1: Fixed character (e.g., zeros); Pass 2: Complement (ones); Pass 3: Random character, followed by verification.                                        |
| **NIST SP 800-88 Rev. 1** | National Institute of Standards and Technology | 1 or more        | Emphasizes "Clear" (logical overwrite) and "Purge" (low-level commands) based on media type. Currently the industry standard.                                |
| **Gutmann method**        | Peter Gutmann (1996)                           | 35 passes        | Designed for older MFM/RLL magnetic drives; includes 4 random passes, 27 specific patterns, and 4 final random passes. Highly redundant for modern hardware. |
| **British HMG IS5**       | United Kingdom                                 | 1 or 3 passes    | Baseline uses 1 pass of zeroes; Enhanced uses 3 passes (zeroes, ones, random) with verification.                                                             |

## Challenges with modern hardware

While traditional data erasure standards were optimized for magnetic [hard disk drives](https://judicialknowledge.miraheze.org/wiki/hard_disk_drive), modern storage technology has introduced significant hurdles to software-based overwriting.

### Solid-state drives (SSDs)

[SSDs](https://judicialknowledge.miraheze.org/wiki/Solid-state_drive) utilize [flash memory](https://judicialknowledge.miraheze.org/wiki/flash_memory) managed by an onboard flash translation layer (FTL) controller. Due to architectures designed for efficiency and longevity—such as **[wear leveling](https://judicialknowledge.miraheze.org/wiki/wear_leveling)** and over-provisioning—software utilities cannot directly target physical blocks on the drive. Standard file-shredding or linear overwriting programs often leave data remnants untouched in hidden or reallocated blocks.

To securely erase an SSD, operators must trigger hardware-level commands built into the drive's firmware by the manufacturer:

- **ATA Secure Erase:** A command that applies a voltage spike to all available NAND cells simultaneously, purging data in a single operation.
- **NVMe Format / Sanitize:** Modern commands optimized for Non-Volatile Memory Express drives to clear encryption keys (Crypto Erase) or block allocation tables natively.

## Data erasure vs. physical destruction

Data erasure is often contrasted with physical destruction methods, such as [degaussing](Degaussing.md), physical shredding, or disintegration.

The primary advantage of software-based data erasure is **sustainability and economic value**; the hardware remains fully functional and can be safely redeployed or sold on the secondary market. Physical destruction, by contrast, creates electronic waste ([e-waste](https://judicialknowledge.miraheze.org/wiki/e-waste)) and completely destroys the capital value of the hardware, though it remains favored for ultra-high-security military applications.

## See also

- [Anti-forensics](Anti-forensics.md)
- [Digital forensics](Digital_forensics.md)
- [Degaussing](Degaussing.md)
- [Hardware security](https://judicialknowledge.miraheze.org/wiki/Hardware_security)
- [Data remanence](Remanence.md)

## References

[Category:Computer security](https://judicialknowledge.miraheze.org/wiki/Category:Computer_security) [Category:Data management](https://judicialknowledge.miraheze.org/wiki/Category:Data_management) [Category:Data privacy](https://judicialknowledge.miraheze.org/wiki/Category:Data_privacy)

---

*Source:* [Data erasure](https://judicialknowledge.miraheze.org/wiki/Data_erasure) on the Judicial Knowledge Hub wiki, revision 29 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Data erasure*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Data_erasure  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
