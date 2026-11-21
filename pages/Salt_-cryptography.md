---
title: "Salt (cryptography)"
source_url: https://judicialknowledge.miraheze.org/wiki/Salt_%28cryptography%29
revision_id: 33
last_edited: 2026-06-06T10:27:19Z
author: Cecep Mustafa
affiliation: Indonesian Judicial College (IJC)
orcid: https://orcid.org/0000-0003-0037-497X
license: CC-BY-SA-4.0
---

# Salt (cryptography)

In [cryptography](https://judicialknowledge.miraheze.org/wiki/cryptography), a **salt** is random data that is used as an additional input to a [one-way function](https://judicialknowledge.miraheze.org/wiki/one-way_function) (typically a [cryptographic hash function](Cryptographic_hash_function.md)) that hashes data, a password, or a passphrase.

Salts are primarily used to defend against dictionary attacks and pre-computed [rainbow table](https://judicialknowledge.miraheze.org/wiki/rainbow_table) attacks on stored password databases. By ensuring that every hashed password has a unique salt, identical passwords will result in completely different hashes, forcing an attacker to brute-force each password individually rather than cracking the entire database at once.

## Background

Historically, operating systems and web applications stored passwords by passing the user's plaintext password (\$P\$) through a cryptographic hash function (\$h\$) and storing the output message digest (\$H\$):

$$H = h(P)$$

When a user attempted to log in, the system would hash the entered password and compare it to the stored digest.

However, because cryptographic hash functions are completely [deterministic](https://judicialknowledge.miraheze.org/wiki/deterministic_algorithm), identical passwords always yield identical hashes. If an attacker gains unauthorized access to the password database, they can use a pre-computed database of millions of common passwords and their corresponding hashes—known as a [rainbow table](https://judicialknowledge.miraheze.org/wiki/rainbow_table)—to instantly reverse the hashes back into plaintext.

## Mechanism

A salt addresses this vulnerability by introducing unique randomness to the hashing process. When a user creates an account or changes their password:

1.  The system generates a cryptographically secure random or pseudo-random string of bytes (the salt, \$S\$).
2.  The salt is appended or prepended to the plaintext password (\$P\$).
3.  The combined string is passed through the cryptographic hash function.

The resulting database record stores both the salt and the final hash (\$H\$):

$$H = h(P \parallel S)$$

Where \$\parallel\$ denotes string concatenation.

When the user logs in, the system retrieves the plain text salt from the database record, concatenates it with the newly entered password, runs the hash function, and checks if the output matches the stored digest.

## Benefits and defenses

Salting does not make an individual, weak password complex, but it completely mitigates specific mass-cracking vectors.

### Defeating rainbow tables

Because the salt is unique to each user account, pre-computed rainbow tables become completely useless. An attacker cannot use a generic lookup table because the table would have had to be pre-computed using that specific user's exact salt value.

### Obfuscating identical passwords

If two users on the same system choose the exact same password (e.g., \`Password123\`), they will be assigned different random salts (\$

---

*Source:* [Salt (cryptography)](https://judicialknowledge.miraheze.org/wiki/Salt_%28cryptography%29) on the Judicial Knowledge Hub wiki, revision 33 (2026-06-06).  
*Author:* Cecep Mustafa, Indonesian Judicial College (IJC). ORCID: [0000-0003-0037-497X](https://orcid.org/0000-0003-0037-497X)  
*Cite as:* Mustafa, C. (2026). *Salt (cryptography)*. In *Judicial Knowledge Hub*. https://judicialknowledge.miraheze.org/wiki/Salt_%28cryptography%29  
*Licence:* [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
