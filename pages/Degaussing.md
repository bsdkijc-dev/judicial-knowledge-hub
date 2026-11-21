---
title: "Degaussing"
source_url: https://judicialknowledge.miraheze.org/wiki/Degaussing
revision_id: 30
last_edited: 2026-06-06T10:21:48Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Degaussing

**Degaussing** is the process of reducing or completely eliminating a remnant [magnetic field](https://judicialknowledge.miraheze.org/wiki/magnetic_field). Named after the [gauss](https://judicialknowledge.miraheze.org/wiki/gauss_%28unit%29), a unit of [magnetic flux density](https://judicialknowledge.miraheze.org/wiki/magnetic_flux_density) which in turn was named after mathematician and physicist [Carl Friedrich Gauss](https://judicialknowledge.miraheze.org/wiki/Carl_Friedrich_Gauss), the technique is widely applied across computer technology, military defense, and analog electronics.

In [computer security](https://judicialknowledge.miraheze.org/wiki/computer_security) and [digital forensics](Digital_forensics.md), degaussing is recognized as a form of physical [data sanitization](Data_erasure.md) that renders magnetic storage media—such as [hard drives](https://judicialknowledge.miraheze.org/wiki/hard_disk_drive) and magnetic tapes—permanently unusable by disrupting the magnetic domains where data is recorded.

## Physical principles

Magnetic storage media relies on the alignment of microscopic magnetic domains, or [dipoles](https://judicialknowledge.miraheze.org/wiki/magnetic_dipole), within a ferromagnetic material to represent binary data (ones and zeroes).

When a device is inserted into a degausser, it is subjected to an intense, alternating magnetic field. This external field forces the magnetic domains to rapidly shift alignment. As the cycle repeats and gradually diminishes to zero, the domains are left in a completely randomized orientation.

Mathematically, this process can be visualized via a [hysteresis](https://judicialknowledge.miraheze.org/wiki/hysteresis) loop. The degausser drives the material's [magnetization](https://judicialknowledge.miraheze.org/wiki/magnetization) (\$M\$) to saturation (\$M\_{\text{sat}}\$) using an external magnetic field (\$H\$) that exceeds the material's [coercivity](https://judicialknowledge.miraheze.org/wiki/coercivity) (\$H_c\$). The loop is continuously collapsed inward until the net magnetization reaches zero:

$$M_{\text{net}} \approx 0$$

Because the internal magnetic structure is physically randomized, the original data tracks and essential internal servo control tracks are permanently destroyed.

## Applications

Degaussing is applied across several engineering and technology domains:

### Data sanitization

In enterprise and government sectors, specialized machines known as **degaussers** are used to destroy sensitive data.

- **Hard Disk Drives (HDDs):** Degaussing neutralizes the magnetic platters. It also destroys the drive's internal read/write head actuators and control chips, meaning a degaussed hard drive **cannot be reused** or reformatted.
- **Magnetic Tape:** High-density backup tapes (such as LTO or DLT) are entirely wiped. Unlike HDDs, some older tape formats without factory-written servo tracks can occasionally be reused after degaussing, though modern high-capacity tapes generally become unusable.

### Naval defense

During [World War II](https://judicialknowledge.miraheze.org/wiki/World_War_II) and continuing into modern naval warfare, degaussing is used to protect steel-hulled warships and submarines from [magnetic mines](https://judicialknowledge.miraheze.org/wiki/magnetic_mine). Ships naturally acquire a large magnetic signature as they travel through Earth's magnetic field. By installing an internal system of electrical cables (degaussing coils) and passing specific currents through them, the vessel generates an equal and opposite magnetic field, effectively masking its magnetic presence from marine sensors.

### Cathode-ray tubes (CRTs)

In older [cathode-ray tube](https://judicialknowledge.miraheze.org/wiki/cathode-ray_tube) (CRT) monitors and televisions, ambient magnetic fields (including the Earth's magnetic field) could cause the internal shadow mask to become magnetized. This caused the electron beams to deflect improperly, leading to color distortion or "bleeding" across the display. Most late-model CRTs included a built-in degaussing coil that activated a brief, high-current pulse whenever the monitor was turned on, accompanied by a distinctive humming sound.

## Standards and compliance

For high-security operations, data erasure via degaussing must meet strict government regulations. Organizations such as the U.S. [National Security Agency](https://judicialknowledge.miraheze.org/wiki/National_Security_Agency) (NSA) maintain an Evaluated Products List (EPL) certifying specific commercial degaussers.

| Regulatory standard       | Authority                                      | Requirement for magnetic media                                                                                                                                         |
|---------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NIST SP 800-88 Rev. 1** | National Institute of Standards and Technology | Approved as a method of "Purging" data from magnetic media, but explicitly notes it is ineffective for [SSDs](https://judicialknowledge.miraheze.org/wiki/solid-state_drive).                           |
| **NSA/CSS EPL**           | National Security Agency                       | Requires degaussers to generate a minimum magnetic field strength measured in [Oersteds](https://judicialknowledge.miraheze.org/wiki/Oersted) (Oe) that far exceeds the coercivity of the target drive. |
| **DoD 5220.22-M**         | U.S. Department of Defense                     | Sanctions degaussing as an acceptable method for destroying classified magnetic records before physical disposal.                                                      |

## Limitations

Degaussing is strictly a magnetic phenomenon. It is completely ineffective against **[solid-state drives](https://judicialknowledge.miraheze.org/wiki/solid-state_drive) (SSDs)**, NVMe drives, flash memory chips, smart cards, or USB thumb drives. Because flash storage relies on trapped electrical charges inside [floating-gate transistors](https://judicialknowledge.miraheze.org/wiki/floating-gate_transistor) rather than magnetic domains, exposing an SSD to a degausser leaves the data completely intact.

## See also

- [Anti-forensics](Anti-forensics.md)
- [Data erasure](Data_erasure.md)
- [Data remanence](Remanence.md)
- [Hysteresis](https://judicialknowledge.miraheze.org/wiki/Hysteresis)
- [Hard disk drive](https://judicialknowledge.miraheze.org/wiki/Hard_disk_drive)

## References

[Category:Magnetic devices](https://judicialknowledge.miraheze.org/wiki/Category:Magnetic_devices) [Category:Computer security](https://judicialknowledge.miraheze.org/wiki/Category:Computer_security) [Category:Data management](https://judicialknowledge.miraheze.org/wiki/Category:Data_management) [Category:Forensic science](https://judicialknowledge.miraheze.org/wiki/Category:Forensic_science)

---

*Source:* [Degaussing](https://judicialknowledge.miraheze.org/wiki/Degaussing) on the Judicial Knowledge Hub wiki, revision 30 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Degaussing*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Degaussing  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
