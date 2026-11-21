---
title: "Cryptographic hash function"
source_url: https://judicialknowledge.miraheze.org/wiki/Cryptographic_hash_function
revision_id: 32
last_edited: 2026-06-06T10:26:34Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Cryptographic hash function

A **cryptographic hash function** (CHF) is a mathematical [algorithm](https://judicialknowledge.miraheze.org/wiki/algorithm) that maps data of arbitrary size (often called a "message") to a bit array of a fixed size (the "hash value", "hash", or "message digest"). It is a [one-way function](https://judicialknowledge.miraheze.org/wiki/one-way_function), meaning it is an algorithm that is practically infeasible to invert or reverse.

Cryptographic hash functions are a fundamental primitive of modern [cryptography](https://judicialknowledge.miraheze.org/wiki/cryptography) and are used extensively in [information security](https://judicialknowledge.miraheze.org/wiki/information_security), [digital forensics](Digital_forensics.md), [digital signatures](https://judicialknowledge.miraheze.org/wiki/digital_signature), [message authentication codes](https://judicialknowledge.miraheze.org/wiki/message_authentication_code) (MACs), and various forms of data integrity verification.

## Properties

An ideal cryptographic hash function must satisfy several core mathematical and security properties to be considered safe for cryptographic utility:

### Deterministic

The function must be completely deterministic. For any given input message \$M\$, the function must always produce the exact same output hash value \$H\$.

$$h(M) = H$$

### Quick computation

The function must be computationally efficient, meaning it can return the hash value for any given message quickly (in \$O(1)\$ or linear time relative to message size) on standard computing hardware.

### Pre-image resistance (One-Way)

Given a hash value \$H\$, it must be computationally infeasible to determine or reverse-engineer the original input message \$M\$ such that:

$$h(M) = H$$

### Second pre-image resistance

Given a specific input \$M_1\$ and its corresponding hash \$h(M_1)\$, it must be computationally infeasible to find a distinct, alternative input \$M_2\$ (where \$M_1 \neq M_2\$) that produces the exact same hash value:

$$h(M_1) = h(M_2)$$

### Collision resistance

It must be computationally infeasible to locate *any* two distinct and arbitrary inputs, \$M_1\$ and \$M_2\$, such that they yield an identical output hash:

$$h(M_1) = h(M_2)$$

### Avalanche effect

A minor modification to the input data (such as flipping a single bit) must result in a radically different hash value. The new digest should appear completely uncorrelated with the original digest, making any tracking of input patterns impossible.

## Common algorithms

Over the history of computer science, several cryptographic hashing suites have been designed, with older iterations deprecated as computing power grew and vulnerabilities were discovered.

### MD5

Designed by [Ronald Rivest](https://judicialknowledge.miraheze.org/wiki/Ronald_Rivest) in 1991, [MD5](https://judicialknowledge.miraheze.org/wiki/MD5) produces a 128-bit hash value. While heavily deployed historically for checksum validations, it was found to suffer from severe [collision attack](https://judicialknowledge.miraheze.org/wiki/collision_attack) vulnerabilities. It is no longer considered secure for cryptographic purposes but remains in legacy use for non-security checksums.

### SHA-1

Developed by the [National Security Agency](https://judicialknowledge.miraheze.org/wiki/National_Security_Agency) (NSA) and published in 1995, [SHA-1](https://judicialknowledge.miraheze.org/wiki/SHA-1) produces a 160-bit hash digest. In 2017, the [CWI Amsterdam](https://judicialknowledge.miraheze.org/wiki/CWI_Amsterdam) research institute announced the first practical collision attack against SHA-1 (the SHAttered attack). It has since been deprecated by global tech standards.

### SHA-2

Also designed by the NSA and published in 2001, [SHA-2](https://judicialknowledge.miraheze.org/wiki/SHA-2) is a family of two structurally similar hash functions with different digest sizes: [SHA-256](https://judicialknowledge.miraheze.org/wiki/SHA-256) (256-bit output) and SHA-512 (512-bit output). It remains highly secure and is widely used in protocols like [TLS](https://judicialknowledge.miraheze.org/wiki/Transport_Layer_Security), [SSL](https://judicialknowledge.miraheze.org/wiki/SSL), [Bitcoin](https://judicialknowledge.miraheze.org/wiki/Bitcoin), and PGP.

### SHA-3

Released by the [NIST](https://judicialknowledge.miraheze.org/wiki/National_Institute_of_Standards_and_Technology) in 2015, [SHA-3](https://judicialknowledge.miraheze.org/wiki/SHA-3) is the latest standard. Internally, it relies on a completely different structure called a "sponge construction" based on the Keccak algorithm. It provides an alternative framework to SHA-2 to ensure cryptographic agility should SHA-2 vulnerabilities ever be discovered.

## Applications

### Verifying file integrity

In [digital forensics](Digital_forensics.md) and software distribution, hashes serve as digital fingerprints. By comparing the calculated hash of an acquired file against a known-good source hash, analysts can verify that the file has not been altered, corrupted, or injected with malware.

### Password storage

Information systems do not store raw, plaintext user passwords in databases. Instead, they store the output of a cryptographic hash function applied to the password (often combined with a random string called a [salt](Salt_-cryptography.md)). When a user logs in, the system hashes the entered password and compares it to the stored hash value.

### Blockchain and cryptocurrencies

Cryptographic hash functions are the backbone of [blockchain](https://judicialknowledge.miraheze.org/wiki/blockchain) architectures. In networks like Bitcoin, blocks are chained together by embedding the SHA-256 hash of the previous block's header into the current block, creating an immutable ledger.

## See also

- [Digital forensics](Digital_forensics.md)
- [Salt (cryptography)](Salt_-cryptography.md)
- [Message authentication code](https://judicialknowledge.miraheze.org/wiki/Message_authentication_code)
- [Avalanche effect](https://judicialknowledge.miraheze.org/wiki/Avalanche_effect)
- [Merkle tree](https://judicialknowledge.miraheze.org/wiki/Merkle_tree)

## References

[Category:Cryptographic hash functions](https://judicialknowledge.miraheze.org/wiki/Category:Cryptographic_hash_functions) [Category:Data integrity](https://judicialknowledge.miraheze.org/wiki/Category:Data_integrity) [Category:Information security](https://judicialknowledge.miraheze.org/wiki/Category:Information_security)

---

*Source:* [Cryptographic hash function](https://judicialknowledge.miraheze.org/wiki/Cryptographic_hash_function) on the Judicial Knowledge Hub wiki, revision 32 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Cryptographic hash function*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Cryptographic_hash_function  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
