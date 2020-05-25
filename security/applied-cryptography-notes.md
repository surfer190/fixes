## Applied Crytography Notes

> Technology trumps politics

This is about stopping major governments from reading your files

types or encryption:
* file
* email
* digital signatures
* digital certified mail
* secure election protocols
* digital cash

Natural low of cryptography - much easier to user than it is to break

Encryption and decryption grows linearly with keylength but cryptoanalysis grows exponentially

What we have learnt is the NSA circumvents and does not break cryptography. It hacks the computers doing the encryption and decryption.

You have to be targeted - bulk collection is not feasible.

The technical difficulties of implementing cryptography are farore difficult than the mathemtical chanllenges of making crypto secure.

## Foundations

* plaintext - message
* enryption - disguising a message
* ciphertext - encrypted message
* decryption - turning ciphertext into a message
* cryptography - art and science of keeping messages secure
* Cryptanalysis - art and science of breaking ciphertext

Plaintext (M) undergoes encryption (E) to achieve ciphertext (C). Decryption (C) goes the other way.

* Authentication - receiver know the origin / sender is who they say they are
* Integrity - ensure the message has not been modified in transit
* Nonrepudiation - sender should no be able to falsely deny that they sent a message

Cryptographic algorithm or cipher - function used for encryption  / decryption.

A restricted algorithm works by keeping the algorithm secret - the problem is that when a person leaves the group you have to change the algorithm. No standardization or quality control.

Modern cryptography solves teh resticted algoritm problem with a **key**.
The range of possible values is called the **keyspace**

Encryption and decryption operations use a key.

Some systems have a seperate encryption key from the decryption key

The security is based on the key - meaning that the algorithm can be published and analysed.
If an eavesdropper knows your algorithm - she still can't read the message without the key.

Types of keybased algorithms:

* Symmetric - the encryption key can be calculated from the decryption key. Usually a single key - that both sender and received agree on. The security rests on the key - the key must remain secret.
    * Stream ciphers - work on a single bit at a time
    * block ciphers - work on groups of bits
* Public-key algorithms - Designed so enryption key is different from the decryption key. Decryption key cannot be calculated from the encryption key. The encryption key can be made public. A complete stranger can encrypt a message with the encryption key. But only the person with the corresponding decryption key can decrypt the message. The encryption key is the public key. The decrpytion key is the private key or secret key.

Sometimes messages are encrypted with the private key and decrpyed with the public key - used in digital signatures.

The point of cryptography is to keep the plaintext message secret.

Crpytanalysis is retrieving the plaintext message without access to the key.

Types of attacks:

* ciphertext-only - non plaintext
* known-plaintext - has access to ciphertext and messages
* chosen-plaintext - chooses what the message is that gets encrypted - can choose ones that yield more info about the key
* adaptive chosen plaintext - can modify choice about chosen attack
* chosen-ciphertext - can choose ciphertext to be decrypted and has access to decrypted message
* chosen-key attack - knows relationship between keys
* rubber-hose cryptanalysis - the best way - blackmail or torture

### Security of Algorithms

> If the cost required to break an algorithm is greater than the value of the encrypted data then you're probably safe

> If the amont of data encrypted with a single key is less than the amount of data necessary to break the algorithm your probably safe

value of data decreases over time

severity:

* total break - key is found
* global deduction - finds an alternate algorithm without finding K
* instance deduction - finds the plaintext of intercepted ciphers
* information deduction - gains informatino about the key or plaintext

algorithm is **unconditionally secure** if no matter how much ciphertext - there is not enough info to recover the plaintext

Every other cryptosystem is breakable in a cipher-only attack - by trying every possible key and seeing if the message is meaningful. The **brute-force** attack.

We are more interested in **computationally secure** - if it cannot be broken with available resources.

Complexity measurement:

* Data complexity - amount of data input
* processing complexity - time to perform the attack (work factor)
* storage requirements - amount of memory needed

### Steganography

Hiding secret messages in other messages - like invisible ink, pin puntures. MOre recently messages are hidden in graphic images. Replacing the least significant bit of each byte with bits of a message.




