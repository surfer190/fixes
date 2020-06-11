# Notes on Serious Cryptography

> Cryptography in theory is strong, but cryptography in practice is as prone to failure as any other aspect of a security system

> There was—and there has been—a huge divide between those who know and understand cryptographic algorithms and those who use them

> Crypto is perceived as hard because cryptographers haven’t done a good job of teaching it

> I don’t discuss the details of obsolete or insecure algorithms such as DES (Data Encryption Standard) or MD5

## 1. Encryption

Makes data incomprehensible to ensure confidentiality.
Cipher = Algorithm, Key = Secret value.
Without the secret key you can't decrypt and neither can an attacker.

Symmetric encryption - key used to decrypt is the same used to encrypt.

### Basics

* plaintext - unencrypted message
* ciphertext - encrypted message

> ciphertext can never be shorter than the plaintext only the same size or longer

### Classic Ciphers

#### Caesar Cipher

* Apparently used by Julius Caesar
* Encrypts by moving letters 3 down in the alpahbet - wrapping around at the end.
* Decrypttion is down moving the letters 3 up in the alphabet

#### Vigenère Cipher

* Created in the 1500's by Battista Bellaso
* Used by Confederates in American Civil War

Differect from Caesar Cipher as it uses a key. A colleciton of letters representing their place in the alphabet.

    DUH -> 3, 20, 7

In practice, entrpying the message: "CRYPTO"

    C shifted 3 positions -> F
    R shifted 20 positions -> L
    Y shifted 7 positions -> F
    P shifted 3 positions -> S
    T shifted 20 positions -> N
    O shifted 7 positions -> V
    
    FLFSNV

Breaking this cipher:

1. figure out the key length -> view repeated sections - indiciating the same word was enrypted using the same key
2. determine actual key using frequency analysis -> exploit uneven distribution of letters in languages (E is most common in Engligh)

#### How Ciphers Work

* permutation - function that transforms an item for a unique inverse
* mode of operation - algorithm that uses a permutation for arbitrary mesage size (mode of Caesar is more simple than the Vigenere - where letters at different positions specifiy difference permutations)

##### Permutation

Most classical ciphers work by substitution - replcing one character with another.
If each letter does not have exactly one inverse then it is not a permutation.

For a permutation to be secure:

* The permutation should be determined by the key
* Different keys should result in different permutations
* The permutation should look random - no pattern

##### Mode of Operation

By analysing duplicates in the ciphertet you might learn something about the message.
The mode mitigates the exposure of duplicate letters

> If the key is N letters long, then N different permutations will be used for every N consecutive letters. However, this can still result in patterns in the ciphertext because every Nth letter of the message uses the same permutation. That’s why frequency analysis works to break the Vigenère cipher

If the message is always <= N, then frequency analysis can be defeated. Unless the same key is used multiple times.

For a secure cipher, you must combine a secure cipher with a secure mode.

#### Why classical ciphers are insecure

They are limited to oeprations you can do in your head or a piece of paper.
They lack computational power.

A cipher's permutation should look random and to look random it should be random.

So for a 26 letter alphabet:

    26! = 26 * 25 * 24 * 23 = 2^88

But then the explanation gets a bit hazy:

> But classical ciphers can only use a small fraction of those permutations—namely, those that need only simple operations (such as shifts) and that have a short description (like a short algorithm or a small look-up table). The problem is that a secure permutation can’t accommodate both of these limitations.

>You can get secure permutations using simple operations by picking a random permutation, representing it as a table of 25 letters (enough to represent a permutation of 26 letters, with the 26th one missing), and applying it by looking up letters in this table. But then you wouldn’t have a short description. For example, it would take 250 letters to describe 10 different permutations, rather than just the 10 letters used in the Vigenère cipher.

> You can also produce secure permutations with a short description. Instead of just shifting the alphabet, you could use more complex operations such as addition, multiplication, and so on. That’s how modern ciphers work: given a key of typically 128 or 256 bits, they perform hundreds of bit operations to encrypt a single letter. This process is fast on a computer that can do billions of bit operations per second, but it would take hours to do by hand, and would still be vulnerable to frequency analysis.”

#### Perfect Encryption: One Time Pad

    C = P ^ K

* `^`: Exclusive Or
* `C`: Cyphertext
* `P`: Plaintext
* `K`: Key

Encryption is identical to decryption

    P = C ^ K

The important thing is the one-time pad can only be used one time.

> The one-time pad is utterly inconvenient to use because it requires a key as long as the plaintext and a new random key for each new message or group of data

> To encrypt a one-terabyte hard drive, you’d need another one-terabyte drive to store the key!

##### Why is it secure?

The key must be as long as the plaintext to achieve perfect secrecy.

> if K is random, the resulting C looks as random as K to an attacker because the XOR of a random string with any fixed string yields a random string

> In other words, knowing the ciphertext gives no information whatsoever about the plaintext except its length

If the key is shorter than the plaintext, the attacker could learn what the plaintext is not - which makes the secrecy imperfect.

### Probabilties

Total number of keys if we have n-bit keys is:

    2^n

So probability of a randomly chosen key is correct is:

    1 / 2^n

The proability of not being correct is 1 - p:

    1 - (2 / 2^n)

Which one close enough to 1 means almost certainly

### Encryption Security

The one time pad is impractical. We have to give up some security to be secure and usable.

A cipher is secure if:

* Given a large number of plaintext-ciphertext pairs - nothing can be learned

### Attack Models

Set of assumptions or requirements about how attackers interact with a cipher.

* what attacks to guard against
* guidelines to users about whether use of the cipher is safe
* give clues to cryptoanalysts - to know whether an attack is valid

#### Kerkhoff's Principle

Security of the cipher should rely only on the secrecy of the key and not of the cipher algorithm

* Black box models - no details of algorithm or key but can query
* Gray box models - attacker has access to implementation (algorithm)

### Security Goals

* Indistinguishability - ciphertext should be indistinguishable from random strings
* Non-malleability - Should be impossible to create a ciphertext similar in anyway to previously ciphered text

**The books goes a bit hardcore now...Semantic Security and Randomized Encryption: IND-CPA**

### Types of Encrypton Applications

* In-transit - protects data sent between computers (encrypted before sent and decrypted after received)
* At-rest - protects data in information systems. Data is encrypted before written to memory and decrypted before being read.

### Assymetric Encryption

Symmetric encryption - two parties share a key and use it for both encryption and decryption.

Assymetric encryption - in assymetric encryption there are 2 keys. The encryption key (the public key) and the decryption key (the private key)

The public key can be computer form the private key but (obviously) the private key cannot be computer from the public key.

IE. it is easy to compute in one direction but practically impossible to invert

### When Ciphers do More than Encryption

Basic encrpytion turn plaintext into ciphertext.

#### Authenticated Encryption (AE)

Type of symmetrical encryption that returns an _authentication tag_ in addition to a ciphertext.

Encryption

    AE(P, K) -> (C, T)

Decryption

    AE(K, C, T) -> p

* The decryption happens only if the key and a valid tag (T) is input
* The tag ensures the integrity of the message and evidence that the ciphertext is identical to that sent
* Identifies the sender

#### AEAD (Authenticated Encryption with Associated Header)

Some header remains clear like destination address and payload in encrypted

#### Format Preserving Encryption

* A basic cipher takes bits and returns bits.
* It doesn't care whether the bits represent text, an image or pdf.
* Ciphertext may be encoded as raw bytes, hexadecimal characters, base64.

What if you need the ciphertext to have the same format as the plaintext - required in some database systems.

FPE (Format Preserving Encryption) solves this. Ie. an ip address is encrypted into an ip address.

    127.0.0.1 -> K -> 212.91.12.2

#### FHE - Fully Homomorphic Encryption

* Allows replacing of ciphertext without ever decrypting the the initial ciphertext.
* A cloud provider doesn't know what the data is or what the change is
* It is slow

#### Searchable Encryption

* Searching an encrypted database without leaking search terms by encrypting the query
* Remains experimental

#### Tweakable Encryption

* Simulate different version of a cipher - ie. a unique customer value.
* Main application is disk encryption
* Disk encryption - tweak value is sued based on the position of the data

### When things fo wrong

#### Weak Cipher

Encryption in 2G mobile phones used an `A5/1` cipher - turned out weaker than expected.

## 2. Randomness

Without randomness cryptography would be impossible because all operations become predicatable and therefore insecure.

The algorithm or process that produces random bits.
Certain things appear more random than others because they have _no obvious pattern_

`00000000` is seen as more random than `11010110`, as there can only be 1 pattern with eight zeroes, thereas there are 55 with 5 1's and 3 zeroes.

That is a big mistake. Something that doesn't look random can be random.

> Non-randomness is often synonymous with insecurity

### Probability Distribution

* `0` means impossible
* `1` means certain

probability distribution must contain all possiblities so summed it equals to 1.

* A `uniform distribution` occurs when all probabilities in a distribution are equal
* `non-uniform` probabilities not equal

### Entropy

The measure of uncertainty or disorder in a system
The more biased a result, the less uniform and the lower the entropy.
**mathematics** goes deep here.

### RNG (Random Number Generators) and PRNG (Pseudo Random Number Generators)

You need 2 things

* A source of uncertainty (source of entropy) [RNG]
* A cryptographic algorithm to produce high quality random bits from the source of entropy [PRNG]


* Randomness comes from the uncertain and unpredicatable environment
* Examples: Temperature, acoustic noise, air turbulence, or electrical static
* harvest the entropy in a running operating system by drawing from attached sensors, I/O devices, network or disk activity, system logs, running processes, and user activities such as key presses and mouse movement
* QRNG (Quantum RNG) - radioactive decay, vacuum fluctuations and photon's polarization - can provide real randomness.
* PRNG (Pseudo RNG) - reliably produce many artificial random bits from a few true random bits.
* RNG would not produce bits if you stopped moving your mouse, whereas PRNG will always return.

RNG - true random bits, analog sources, slow, non-deterministic, no gaurentee of high entropy
PRNG - random-looking bits, digital sources, deterministic, high entropy

#### How PRNG works

* recieves random bits from RNG at regular intervals to update an entropy pool
* determinitic random bit generator (DRBG) is deterministic - given one input you get the same output
* reseeding is reseting the entropy pool

#### Security concerns

* backtracking resistence
* predication resistence

**More Info in the book**

#### PRNG Fortuna

* PRNG Fortuna designed in 2003 used in Windows by Niels Ferguson and Bruce Schneier

**More Info in the book**

> Statistical tests for randomness are irrelevant and useless 

Generate a random file with OpenSSL

    openssl rand <number of bytes> -out <outputfile>

### Real World PRNG's

Ubiquotous: desktops, laptops, routers, virtual machines, set-top boxes and mobile phones

#### Generating Random Bits in Unix Based Systems

The device file `/dev/urandom` is the userland interface to the crytpo PRNG of common *nix systems.
Because it is a device file, generating bits from it is done by reading it as a file.

Writing 10MB of random bits to a file

    dd if=/dev/urandom of=<output file> bs=1M count=10

Eg.

    dd if=/dev/urandom of=./random.txt bs=1024 count=10

**Book shows you secure and insecure implementations of using urandom in c code**

Difference between `/dev/urandom` and `/dev/random` is `/dev/random` attempts to estimate the amount of entropy and refuses to return bits if the level of entropy is too low.

That is a bad idea:

* entropy estimators are notoriously unreliable
* it runs out of entropy quickly and can lead to denial of service conditions

You can check the current enrtropy of `/dev/random` with:

    cat /proc/sys/kernel/random/entropy_avail

> As is usually the case in Windows, the process is complicated

##### Hardware PRNG

Intel Digital Random Number Generator is a hardware PRNG introduced in 2012

#### How Things can go Wrong

* Mersenne Twister is a non-crypto PRNG do not use it (`mt_rand()`)

## 3. Cryptographic Security

Cryptographic security is not the same as software security.
Cryptographic security can be quantified - you can calculate the effort required to break a cryptographic algorithm.

Software security focuses on preventing attackers leveraging the code, cryptography focuses on making well defined problems impossible to solve.

* Informational security - whether it is conceivable to break a cipher at all - given unlimied computation time and memory it cannot be broken if computationally secure.
* Computational security - secure if it cannot be broken in a reasonable amount of time, memory, computationa and budget.

Consider the cipher where you have the plaintext-ciphertext pair (P, C) but not the 128-bit key K.
The cipher is not informationally secure because you could try:

    2^128 possible values of K

Even when testing 100 billion keys per second, it would take more than 100 quintillion years.

* `t` number of operations that can be carried out
* `E` epsilon limit of probability of success

**More hectic stuff in the book**

### Generating Keys

If you plan to encrypt you will have to generate a key.

* temporary - session keys when browing on https
* permanent - public keys

> Secret keys are the crux of cryptographic security and should be randomly generated so that they are unpredictable and secret

1. When you browse an HTTPS website, your browser receives the site’s public key
2. Your browser uses public key to create a symmetric key for the session

Cryptographic keys can be generated in 3 ways:

* Randomly using a PRNG (Pseudo Random Number Generator)
* From a password - using a key derivation function (KDF)
* Key agreement protocol - series of message exchanges ends with a shared key

#### Generating Symmetric Keys

* Secret keys shared by 2 parties
* Same length as the security level they provide
* a 128-bit key provides 128-bit security: 2^128 possible keys

Simply ask for `n` pseudo random bits

    $ openssl rand 16 -hex
    6ca519b4176aee70d6639a8d23aa3f43

#### Generating Asymmetric Keys

* Longer than the security level they provide
* Can't just dump `n` bits - they represent a specific object - they represent a specific object such as a large number
* RSA - the product of 2 primes

To generate an assymetric key you send pseudorandom bits to a key generation algorithm.
The algorithm constructs the private and public key.

You can use openssl to generate a 4096-bit RSA private key:

    openssl genrsa 4096
    
    Generating RSA private key, 4096 bit long modulus
    ....................................................................................................++
    ...............++
    e is 65537 (0x10001)
    -----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----
    
* The key is in a specific format: `base64` encoded data between: `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`
* `e is 65537 (0x10001)` indicates the paramter to use when encrypting...
* RSA encrypts by computing `C = Pe mod n` [whatever that means...]

#### Protecting Keys

* Key wrapping - encrypting a key with a second key stored on the filesystem. Usually from generated from a password that is how Secure Shell (SSH) works.
* On-the-fly generation from password - No enrypted file is stored as the key comes straight from the password. Less wide spread as it is vulnerable to weak passwords.
* Storing the key on hardware token - key stored in secure memory - remains safe even if stolen. Safest, but costliest and least conventient.

Remember you private key is to be kept private. Never publish this on github or give it to anyone.

Key wrapping - Tell openSSL to encrypt the key with encrypt the key with the cipher AES-128:

    openssl genrsa -aes128 4096

The passphrase requested is used to encrypt the newly created key

### How Things can go Wrong

#### Incorrect Security Proofs

Proofs were taken as law. For example `Optimal Asymmetric Encryption Padding (OAEP)` is only almost secure.

#### Short Keys for Legacy Support

In 2015 some researchers found that some HTTPS sites and SSH servers support public-key cryptography with shorter keys than expected. Namely 512 bits instead of at least 2048 bits.

* In public-key the security level is not equal to the key size.
* So 512 bits only offers a security level of 60 bits.
* These keys could be broken in 2 weeks using a 72 processors.
* The problem was fixed when Openssl fixed the issue.

> The security of the whole system is often only as strong as that of its weakest component

### Further Info

* [The sponge and duplex constructions](https://keccak.team/sponge_duplex.html)
* [KeyLength](https://www.keylength.com/)

## 4. Block Ciphers

* During the cold war USA and Russia developed their own ciphers.
* US Government created DES - Data Encryption Standard abopted from 1979 to 2005.
* KGB developed GOST 28147-89 - an algorithm key secret until 1990.
* In 2000 the US based NIST (National Institute of Standards and Technology) selected the success of DES - AES - The **Advanced Encryption Standard**

DES, GOST and AES are all block ciphers - a type of algorithm that combines the algorithm working on  blocks of data with a mode of operation.

### What is a Block Cipher?

* Encryption algorithm - takes a Key (K) and Plaintext (P) and produces Ciphertext (C). C = E(K, P)
* Decryption algorithm - Inverse of encryption. Takes Ciphertext (C) and a Key (K) and produces the Plaintext. P = D(K, C)

### Security Goals

* In order for a block cipher to be secure, it should be a pseudorandom permutation (PRP), meaning that as long as the key is secret, an attacker shouldn’t be able to compute an output of the block cipher from any input.
* That is, as long as `K` is secret and random from an attacker’s perspective, they should have no clue about what `E(K, P)` looks like, for any given `P`

### Block Size

Security depends on block size and key size.
Most block ciphers have 64-bit or 128-bit blocks.
DES blocks have 64 bits (2^6)
AES blocks have 128 bits (2^7)

In computing, lengths that are powers of 2 simplify data storage, processing and addressing.
Important that blocks are not too big to mimnimse length of the ciphertext and memory footprint.

A 16-bit message first needs to be made into a 128-bit block before being encrypted.
To process a 128bit block you need at least 128 bits of memory.
Can fit on the register of CPU. Larger blocks cause performance issues.

> 128bit blocks are processed more efficiently than 64 bit blocks on modern CPU's

**A codebook attack can be used with small block sizes - more in the book**

### How to Construct Block Ciphers

**Deep info in the book**

### Advanced Encryption Standard (AES)

> AES is the most-used cipher in the universe

The AES competition was kind of a “Got Talent” competition for cryptographers, where anyone could participate by submitting a cipher or breaking other contestants’ ciphers. Rijmen and Daemen won it.

AES processes blocks of 128 bits using a secret key of 128, 192, or 256 bits.

Whereas some ciphers work with individual bits or 64-bit words, AES manipulates _bytes_

**More detailed info in the book**

#### AES in action

The message needs to be a multiple of the block length. So 16, 32 etc.
You can check then number of bits in a message with `len(<bytes>)`

In python:

    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    from binascii import hexlify as hexa
    from os import urandom

    # pick a random 16-byte key using Python's crypto PRNG
    k = urandom(16)
    print(f'k = { hexa(k) }')


    # create an instance of AES-128 to encrypt a single block
    cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
    aes_encrypt = cipher.encryptor()

    # set plaintext block p to the all-zero string
    my_plaintext_message = "hello world"
    #ensure it is 16 bytes
    my_plaintext_message = my_plaintext_message.ljust(16)
    my_plaintext_message_as_bytes = str.encode(my_plaintext_message)
    print(my_plaintext_message_as_bytes)

    # encrypt plaintext p to ciphertext c
    c = aes_encrypt.update(my_plaintext_message_as_bytes) + aes_encrypt.finalize()
    print(f'enc({ hexa(my_plaintext_message_as_bytes) }) = { hexa(c) }')

    # decrypt ciphertext c to plaintext p
    aes_decrypt = cipher.decryptor()
    p = aes_decrypt.update(c) + aes_decrypt.finalize()

    print(f'dec({ hexa(c) }) = { hexa(p) }')

    my_decoded_str = p.decode()
    type(my_decoded_str) # ensure it is string representation
    print(my_decoded_str)

output:

    $ python aes.py 
    k = b'e5983b521b541527f69c0caff4c9cc56'
    b'hello world     '
    enc(b'68656c6c6f20776f726c642020202020') = b'bb6c99060dc88d8a32ecba3eefb8143b'
    dec(b'bb6c99060dc88d8a32ecba3eefb8143b') = b'68656c6c6f20776f726c642020202020'
    hello world  

If you fix the key eg.

    k = b'750d496960d85a8db7e7991b81539b3d'

The resulting cipher will always be the same

    b'hello world     '
    enc(b'68656c6c6f20776f726c642020202020') = b'9e338bf5802daa37afbd625a087764b6'
    dec(b'9e338bf5802daa37afbd625a087764b6') = b'68656c6c6f20776f726c642020202020'
    hello world

This is an example - and it is slow.
Production grade AES encryption instead uses fast AES software uses special techniques called table-based implementations and native instructions.

**More info on that in the book**

### Is AES Secure?

> AES is as secure as a block cipher can be, and it will never be broken.

* Fundamentally, AES is secure because all output bits depend on all input bits in some complex, pseudorandom way

> The upshot is that you should care about a million things when implementing and deploying crypto, but AES security is not one of those. The biggest threat to block ciphers isn’t in their core algorithms but in their modes of operation. When an incorrect mode is chosen, or when the right one is misused, even a strong cipher like AES won’t save you

### Modes of Operation

**Alot more info in the book**

### How it can go Wrong

* Meet-in-the-middle attacks
* Padding oracle attacks

## 5. Stream Ciphers

Symmetric ciphers can be block or stream ciphers.
Block ciphers mix chunks of plaintext bits with the key to produce blocks of ciphertext of the same size - 128 bits.

Stream ciphers don't mix plaintext and keys. Instead they generate pseudorandom bits from the key and XOR the plaintext with the pseudorandom bits.

* Seen as more fragile and more often broken
* Used in: mobile phones, wi-fi, bluetooth, 4g, TLS connections and public transport cards

### How Stream Ciphers Work

* Deterministic like DRBG (Deterministic Random Bit Generators)
* The determinism allows you to decrypt by regenerating the psueudorandom bits used to encrypt.
* With PRNG you could encrypt but never decrypt - secure but useless (WTF?)

Stream ciphers take a `key` and a `nonce`. Whereas a DRBG takes a single input.
Key is secret and usually 128 or 256 bits.
Nonce doesn't have to be secret but should be unique for each key. - 64 to 128 bits.

The Stream Cipher (SC) takes a Key (K) and a Nonce (N) to produce a _KeyStream_ (KS).

    K + N -> SC -> KS

Ciphertext is created by XORing Keystream and Plaintext

    P ^ KS = C

The encryption and decryption operations are the same. They both XOR bits with the keystream.

> Nonce - _number used only once_

### Types of Strema Ciphers

* Stateful
* Counter Based

**Lots more info in the book**

### Stream Ciphers

* Grain-128a
* A5/1 - encrypt voice on 2G
* RC4 - insecure software based stream cipher. used in first Wifi Encryption (WEP) and TLS (Transport Layer Security) used to establish HTTPS connections.
* Salsa20 - A good one

#### RC4

* Does no crypto operations. It just swaps bytes.
* WEP tried prepends a nonce to the WEP key, but RC4 doesn't have a nonce in the spec.

#### RC4 in WEP

WEP used a 24-bit nonce - too small. You can to wait for 2^24/2 == 2^12 packets to get the same nonce.
A few megabyte worth of traffic until you find the same none.
The same nonce means the same keystream.
A repeated nonce can allow the attacker to decrypt packets.

* `aircrack-ng` implements the entire attack from network sniffing to cryptoanalysis.

#### RC4 in TLS

* `TLS` is the single most important security protocol on the internet
* Best known for underlying HTTPS connections but also for VPN's, email servers and mobile applications.
* TLS doesn't make same mistake as WEP by tweaking the RC4 spec to get a public nonce, instead TLS just feeds unique 128-bit session keys to RC4.
* The issue is RC4's statistical biases and non-randomness

> RC4’s known statistical biases should have been enough to ditch the cipher altogether, even if we didn’t know how to exploit the biases to compromise actual applications

**Then starts showing teh statistical biases**

### How Things can go Wrong

#### Nonce Reuse

When a nonce is reused more than once with the same key - producing identical key streams.
Meaning you can XOR the 2 ciphertexts together - keystream vanishes and you are left with the XOR of 2 plaintexts.

> For example, older versions of Microsoft Word and Excel used a unique nonce for each document, but the nonce wasn’t changed once the document was modified. `the clear and encrpyted text of an old document could be used to decrtypt later documents.

#### Broken RC4 Implementations

#### Weak Ciphers Baked into Hardware

* These days software can be used to upgrade broken crypto.
* Satphones are like mobile phones, except that their signal goes through satellites rather than terrestrial stations. The advantage is that you can use them pretty much everywhere in the world. Their downsides are the price, quality, latency, and, as it turns out, security.
* `GMR-1` cipher was used (similar to A5/2) the delibrately insecure cipher aimed at nonn-western countries
* `GMR-2` is also insecure and will protect only against ameteurs...not state agencies.

## 6. Hash Functions

* MD5, SHA-1, SHA-256, SHA-3, BLAKE-2 comprise the cryptographers swiss army nice.
* They are used in digital signatures, public-key encryption, integrity verification, message authentication, password protection, key agreement protocols...
* Hash functions are by far the most versatile and ubiquitous of all crypto algorithms
* Anyone can compute the hash value - that is the point

> Cloud storage systems use them to identify identical files and to detect modified files; the Git revision control system uses them to identify files in a repository; host-based intrusion detection systems (HIDS) use them to detect modified files; network-based intrusion detection systems (NIDS) use hashes to detect known-malicious data going through a network; forensic analysts use hash values to prove that digital artifacts have not been modified;

    M -> Hash -> H

Unlike stream ciphers, which create a long output from a short one.
Hash functions take a long input and produce a short output - hash value or digest.

Do not confuse cryptographic hash functions with non-cryptographic hash functions...
Non-cryptographic hashes are used in hash table data structures or to detect accidental errors.
For example CRC (Cyclical redundancy checks) are non-cryptographic hashes used to detect accidental modifications of a file.

### Secure Hash Functions

> Whereas **ciphers** protect data confidentiality in an effort to guarantee that _data sent in the clear can’t be read_, **hash** functions protect data integrity in an effort to guarantee that data — whether sent in the clear or encrypted — _hasn’t been modified_

If it is secure 2 distinct pieces of data should have different hashes.
A file's hash can thus serve as an _identifier_

    M -> HASH -> SIGN ( + SK ) -> S

Digital signatures - applications process the hash of the message to be signed rather than the message itself.

> If even a single bit is changed in the message, the hash of the message will be totally different

> Signing a message’s hash is as secure as signing the message itself, and signing a short hash of, say, 256 bits is much faster than signing a message that may be very large.

    SHA-256 uses 256 bits, the NIST standard hash function.

    import hashlib
    hashlib.sha256(b"a").hexdigest() 
    'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
    
    hashlib.sha256(b"b").hexdigest()  
    '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d'
    
    hashlib.sha256(b"c").hexdigest() 
    '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6'

Given the above hashes it would be impossible to figure out the hash for `d` or any of it's bits.

Secure hash values must be _unpreditable_

#### Preimage resistance

    H = Hash(M)

Hash functions are known as one way functions - you can go from message to hash - but not the other way around.

> Even given unlimited computing power, you would never be able to determine the message that I picked to produce this particular hash, since there are many messages hashing to the same value

There are 2^256 possible values or a hash. But there are many more possible values for the message to the hash say 1024 bits...2^1024.

    2^1024 / 2^256 = 2^768 preimages of 1024 bits each

> it is practically impossible to find any message that maps to a given hash value

An attack for the preimage basically is craete random messages until the hash matches teh given hash - hopelessly inefficient. A brute force. The same attack on a block ciper or stream cipher.

### Collision Resistance

pigeonhole principe: For `m` holes and `n` pigeons. If `n` is greater than `m` then at least 1 hole must contain more than 1 pigeon.

Collisions should be as hard to find as the original message in order for a hash to be collision resistant.

**Birthday attack and low memory collision search in the book**

#### Building Hash Functions

Simplest way to hash a message is split it into chunks and process each chunk consecutively - iterative hashing.

Using a compression function (creates smaller outputs) - _Merkle-Damgard_, sponge functions (same size output)

All hash functions from 1980 to 2010's are based on Merkle-Damgard. MD stands for message digest (not Merkle-damgard)

* MD4
* MD5
* SHA-1
* SHA-2

**more info in the book**

### The SHA family of hashes

* SHA - Secure Hash Algorithm
* Worldwide standards
* Only China (SM3), Russia (streebog) and Ukraine (kupyna) use their own for reasons of sovereignty

> MD5 was broken around 2005 - then many applications started using SHA-1. MD5 provides at best 128bit preimage security.
It takes only seconds to find a collision for md5

**More on SHA-1 internals in the book**

SHA-1 is a 160 bit hash - should be granted 80-bit collision resistance. But researchers got 2^63 - not the flaawless 2^80.
A real world example of the collision only appeared 12 years later: https://shattered.io/

So don't use SHA-1, rahter use SHA-2, SHA-3 or BLAKE-2.

### SHA-2 

* Designed by the NSA
* It is the family of 4 hashes: SHA-224, SHA-256, SHA-384 and SHA-512
* Designed for higher security levels than SHA-1

SHA-256

### SHA-3

In 2007 there was a competition

5 Finalists:

* `BLAKE`
* Groestl
* JH
* Keccak - Wons
* Skein

There are few incentives to upgrade to SHA-3 as SHA-2 is still secure and SHA-3 is slower.

**More info on BLAKE2 in the book**

### How things can go wrong

* Using a weak checksum algorithm like `crc` as a crypto hash

## 7. Keyed Hashing

If you don't want just anyone to verify the integrity of a hash, you used a keyed hash or hash with a secret.
Protect the authenticity of a message.

Form basis for:

* Message Authentication Codes (MAC)
* pseudo Random Functions (PRF)

### MACs

You can verify a message has not been tampered with if you know its key

Protocols include both cipher and a MAC:

* IPSec (Internet Protocol Security)
* SSH (Secure Shell)
* TLS (Transport Layer Security) generate a MAc for each packet

It is too much overhead for 3G and 4G voice call encoding - an attacker can modify the encrpyted audio signal and the recipient wouldn't notice. It would sound like static.

**More in the book about PRF's, HMAC, etc**

## 8. Authenticated Encryption

AE produce an authentication tag and a cipher.
Protecting confidentiality and authenticity.

AES-GCM - most widely used authneticated cipher. Advanced Encryption Standard with Golois Counter Mode.

### How things can go wrong

Authenticated Encryptions has a larger attack surface because they do 2 things - condifentiality encryption and authenticity hashing.

## 9. Hard Problems

> In the 1970s, the rigorous study of hard problems gave rise to a new field of science called computational complexity theory

Computational hardness is the property of computational problems for which there is no algorithm that can run in a reasonable amount of time.

Intractable problems - practically impossible to solve.

It is independent of CPU - it is about the algorithm not computing device.

Computational complexity (Big O) - approxmate number of operations done by an algorithm as a function of its input size.

`O(n)` is a simple search - linear.

Sorting a random list takes `O(n * logn)` 

To retrieve the secret key from a Ciphertext and Plaintext.
To bruteforce a `n-bit` key, `2^n` attempts must be made.
Therefore it is _exponential complexity_ - practically impossible to solve.

`O(1)` means an algorithm runs in constant time - the running time does not depend on the input length

`O(n^2)` is quadratic. `O(2^n)` is exponential.

Polynomoal `O(n^k)` are practically feasible.

`O(n^n)` exponential factorial

### Non-deterministic polynomial Time

* `NP` is the second most important complexity class after `P`.
* `NP` is non-deterministic polynomial time - it can be _verified_ in polynomial time. Ie. Verify that a solution is found.
* Problem of recovering a secret key with a known plaintext is `NP`
* The finding of a key can't be done in polynomial time, but verifying the key is done using polynomial time.
* What about if you just know the ciphertext? Then you wouldn't be able to verify if a given key is correct. Therefore it is not `NP`
* Another example that is not NP is verifying the absense of a solution to a problem.

### NP-complete problems

* The hardest problems in the NP class.

Examples:

* `The travelling salesman problem`: Given a set of points on a map and distances between each point. Find a path that hits each point with the shortest distance travelled.
* `The clique problem`: Given a graph and a number `x`. Determine if there is a set of `x` points or less such that all points are connected to each other.
* `the knapsack problem`: Given 2 numbers `x` and `y`, and a set of items each of known value and weight. Can we pick items where price is at least `x` and weight is at most `y`

No one has proved that P is different from NP.

**More intense info in the book**

## 10. RSA

* Rivest-Shamir-Adleman (RSA) cryptosystem revolutionised cryptography in 1977 as the first public key encryption scheme.
* public key encryption uses two keys. One the public key - can be used by anyone to encrypt a message.
* The other is the private key - which is required to decrypt messages.
* The paragon of public-key encryption - the workhorse of internet security.

RSA is an arithmetic trick. 
It creates a _trapdoor permutation_ - a function that transforms a number `x` to a number `y` in the same range - such that computing y from x is easy using the public key but computing x from y is practically impossible unless you know the private key - the _trapdoor_

RSA does digital signatures as well as encryption. The owner of teh private key is the only one able to sign a message and the public key allows anyone to verify the signature's validity.

**Some intense math about RSA**

An RSA modulus should be at least `1024-bits`

### Encrypting with RSA

RSA is used to encrypt a symmetric key that is then used to encrypt a message with a cipher such as AES.
Encrypting a message or symmetric key with RSA is more complicated.

...

### Signing with RSA

Digital signatures can prove that the holder of a private key tied to a digital signature, signed some message and the signature is authentic.

> That verified signature can be used in a court of law to demonstrate that the private-key holder did sign some particular message—a property of undeniability called nonrepudiation

**More Intense Math...**

### How Things can go Wrong

## 11. Diffie-Hellman

* Key Agreement Protocols

## 12. Elliptic Curves

* Elliptic Curve Cryptography revolutionalised public-key cryptography.
* more powerful and efficient than RSA and Diffie-hellman
* Like RSA it multiplies large numbers, but it does so to combinne points on an elliptic curve.

> ECDSA - Elliptic curve digital signature algorithm

This algorithm has replaced RSA and DSA.
It is the only signature algorithm used by bitcoin and is supported by many SSH and TLS implementations.

* RSA is only used for encryption and signatures
* ECC is a family of algorithms that can be used to perform encryption, generate signatures, perform key agreement, and offer advanced cryptographic functionalities such as identity-based encryption (a kind of encryption that uses encryption keys derived from a personal identifier, such as an email address).

RSA's verification process is faster than ECC's signature generation.
But ECC has shorter signatures and signing speed.

ECC produces shorter signatures - hundreds of bits not thousands of bits.
Signing with ECDSA is much faster than signing with RSA - because it is working on smaller numbers.

ECDSA is about 150 times faster at signing and a little faster at verifying.

> ECDSA signatures are also shorter 512 bits rather than 4096 bits

    $ openssl speed ecdsap256 rsa4096
    
    Doing 4096 bit private rsa's for 10s: 50 4096 bit private RSA's in 9.91s
    Doing 4096 bit public rsa's for 10s: 3233 4096 bit public RSA's in 9.82s
    Doing 256 bit sign ecdsa's for 10s: 18673 256 bit ECDSA signs in 9.90s 
    Doing 256 bit verify ecdsa's for 10s: 3988 256 bit ECDSA verify in 9.84s
    LibreSSL 2.2.7
    built on: date not available
    options:bn(64,64) rc4(ptr,int) des(idx,cisc,16,int) aes(partial) blowfish(idx) 
    compiler: information not available
                    sign    verify    sign/s verify/s
    rsa 4096 bits 0.198200s 0.003037s      5.0    329.2
                                sign    verify    sign/s verify/s
    256 bit ecdsa (nistp256)   0.0005s   0.0025s   1886.2    405.3

It is fair to compare the 2 because they provide a similar security level.

Most systems use a 2048 bit RSa signatures which is orders or magnitude less secure than ECDS256

    $ openssl speed rsa2048
    
    Doing 2048 bit private rsa's for 10s: 296 2048 bit private RSA's in 8.88s
    Doing 2048 bit public rsa's for 10s: 11114 2048 bit public RSA's in 9.37s
    LibreSSL 2.2.7
    built on: date not available
    options:bn(64,64) rc4(ptr,int) des(idx,cisc,16,int) aes(partial) blowfish(idx) 
    compiler: information not available
                    sign    verify    sign/s verify/s
    rsa 2048 bits 0.030000s 0.000843s     33.3   1186.1

> Prefer ECDSA over RSA except when signature verification is critical and you don't care about the signing speed - a sign once, verify many scenario. Like a windows executable.

ECC is more commonly used for signing you can encrypt with them

It is rare though as size of the plaintext is resticted. Only 100 bits of plaintext, compared to 4000 in RSA ar the same security level.

**More info and how it can go wrong in the book**

## 13. TLS

* TLS - Transport Layer Security Protocol.
* SSL - Secure Socket Layer is the name of its predecessor.
* Protects connections between servers and clients.
* The workhorse of internet security
* Examples: Between website and visitors, email servers, mobile applications and videogame servers and players.

TLS is application agnostic - it does not care about the type of content encrypted.

You can use for web based systems relying on HTTP and any other system that needs to initiate a connection with a remote server. It is widely used in Internet of Things.

> TLS has become increasingly complex over the years

This bloat has brought in vulnerabilities:

* Heartbleed
* BEAST
* CRIME
* POODLE 

TLS 1.3 ditched the unnecessary and insecure features - resulting in a simpler, faster and more seure protocol.

### What does TLS Aim to Solve?

* TLS is the `S` in `HTTPS`
* Primary use was to protect credit card numbers, user credentials and other information to be stolen between client and server.
* A secure channel is created
* Ensuring the data is confidential, authenticated and unmodified

TLS must defeat the man-in-the-middle attack. The attack whereby encrypted traffic is decrypted, modified then recenrypted.

TLS defeats it by using certificates and trusted certificate authorities.

For wider adoption it needed to:

* Be efficient - minimise the performance penalty (good for server and client)
* Interoperable - work on any hardware or OS
* Extensible - for added features
* Versatile - not bound to a specific application (like TCP it sits on top of)

### TLS Protocol Suite

It is not a transport protocol - it sits between the transport protocol and application protocol.
Between TCP and HTTP or SMTP.
TLS can also work over UDP (User Datagram Protocol) for connectionless transport - such as voice or audio.

UDP does not gaurentee delivery or correct packet ordering - therefore it is slightly different and is called `DTLS`.
Datagram Transport Layer Security.

#### History

* 1995: Netscape developed SSL (Secure Socket Layer)
* SSL 2.0 and SSL 3.0 had security flaws
* 1999: TLS 1.0
* 2001: TLS 1.1
* 2008: TLS 1.2 - suboptimal too many inherited features

TLS 1.3 is TLS the good parts

> Never use SSL always TLS

#### TLS in a nutshell

2 main protocols:

* record protocol - how to transmit - how data is encapsulated
* handshake protocol - what to transmit - key agreement protocol

1. handshake stared by client (`ClientHello` with type of cipher to use)
2. server response (`ServerHello`)
3. session keys are exchanged

#### Certificates and Certificate Authorities

* The TLS handshake is important - the crux of TLS's security.
* A server uses a certificate to authenticate itself to a client
* A certificate is a public key accompanied with a signature of that key and associated information (like domain)

> Certificate baiscally says: I am `fixes.co.za` and this is my public key

1. Connecting to `https://fixes.co.za` your browser receives the certificate and will verify the certificates signature
2. If the signature is verified - the certificate and public key are trusted and the browser can proceed.

How does the browser know the public key needed to verify the signature?

**The Certificate Authority (CA)**

A CA is a public key hard coded into the browser or operating system.
The public key's private key - belongs to a trusted organisation - that ensures the public keys in certificates it issues belongs to the website or entity that claim to be them.

> The CA is a trusted third party

Without a CA there would be no way to verify that a certificate issued actually belongs to google.

### What happens in practice?

    openssl s_client -connect fixes.co.za:443
    
    CONNECTED(00000005)
    depth=1 C = US, O = Let's Encrypt, CN = Let's Encrypt Authority X3
    verify error:num=20:unable to get local issuer certificate
    verify return:0
    ---
    Certificate chain
    0 s:/CN=fixes.co.za
    i:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    1 s:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    i:/O=Digital Signature Trust Co./CN=DST Root CA X3
    ---
    Server certificate
    -----BEGIN CERTIFICATE-----
    MIIGDjCCBPagAwIBAgISAz7feX99SqugFkIUE5YGs53cMA0GCSqGSIb3DQEBCwUA
    MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD
    ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0yMDA1MDgyMjQ4MjlaFw0y
    MDA4MDYyMjQ4MjlaMBYxFDASBgNVBAMTC2ZpeGVzLmNvLnphMIIBIjANBgkqhkiG
    9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6nJ4tFHTGgb8uHHPwS82NtRo27QLtzrHhe9s
    sFcXY/3L509HrI3dPy5UQZuNODIZbMB57Js97KkEcFkZBuDi5U6gHzb+V3JMKBOv
    qrQxUqgcgnDQB7dMoHYC5bOoAUcOApvv8eD1R7ifPLkmOkcFnRb2vpBOqVdFaxep
    g0Hh68AK3wix4nnQFyNVFbmonyN6hmfbSPMBZuG0IS/vhFEj1gYU/0KIR/5/8sBK
    3HOUE91kbIv+LbqioG6sRMmnX5oYCWrjS85FYKNfE928VBpz6rg+bmVkUguv44ts
    GFd8EKy044AqYe2rPUyirnR8cNsqe1wX87x1InNxI5v+/ECLvQIDAQABo4IDIDCC
    AxwwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcD
    AjAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBR3M9l4ZMExGMcjfPv1aATA7oMbITAf
    BgNVHSMEGDAWgBSoSmpjBH3duubRObemRWXv86jsoTBvBggrBgEFBQcBAQRjMGEw
    LgYIKwYBBQUHMAGGImh0dHA6Ly9vY3NwLmludC14My5sZXRzZW5jcnlwdC5vcmcw
    LwYIKwYBBQUHMAKGI2h0dHA6Ly9jZXJ0LmludC14My5sZXRzZW5jcnlwdC5vcmcv
    MIHUBgNVHREEgcwwgcmCF2Jsb2cuaG93LXRvLXRyYWRlLmNvLnphggtmaXhlcy5j
    by56YYISaG93LXRvLXRyYWRlLmNvLnphghJtYXRvbW8uZml4ZXMuY28uemGCDW51
    bWJlcjEuY28uemGCFHN5bmVyZ3lzeXN0ZW1zLmNvLnphgg93d3cuZml4ZXMuY28u
    emGCFnd3dy5ob3ctdG8tdHJhZGUuY28uemGCEXd3dy5udW1iZXIxLmNvLnphghh3
    d3cuc3luZXJneXN5c3RlbXMuY28uemEwTAYDVR0gBEUwQzAIBgZngQwBAgEwNwYL
    KwYBBAGC3xMBAQEwKDAmBggrBgEFBQcCARYaaHR0cDovL2Nwcy5sZXRzZW5jcnlw
    dC5vcmcwggEFBgorBgEEAdZ5AgQCBIH2BIHzAPEAdgCyHgXMi6LNiiBOh2b5K7mK
    JSBna9r6cOeySVMt74uQXgAAAXH2sLodAAAEAwBHMEUCIQDaVfqAv2NbqQijpX4q
    8T8KEcchm23J7iK18rXZpFUKUwIgGCI8BjlI9RvF0rgUZUh7UCRPnF8EDtPRTMKq
    jYlu72IAdwDnEvKwN34aYvuOyQxhhPHqezfLVh0RJlvz4PNL8kFUbgAAAXH2sLor
    AAAEAwBIMEYCIQC4kcsuY4Uj4cBS78GbZ05iNH7YTxgGdR7vDSYEFDRd7wIhANhP
    enNUM9eu6K2CJEt2Tn1F2rdV8wS/Hg4PRGKfs/BnMA0GCSqGSIb3DQEBCwUAA4IB
    AQBt/oWiS/M28uYv/x64LyDbFrhUuJDahc32AGYNyzPWqDIWflFMOMbqMwqCoCDA
    ipgVHi7Naphr62aShgOkIO81xm+2nG7MjvQIHuLn7yd+8lmXVIyouZ8rWzriIn98
    vHxReFtj0fDgVHZBI1qxVbxRII2I23scZqKxZlihyiNdCfkWvnexx3W7gSxONbo+
    FjhcUJ4mUMWE58zoFYO08/tsfTvrSa6hKiurVMvA0ERAvf5U4gdsxSl4nTPlLuLF
    fFl/4T1ZrcpRf9IxpCZp5PPKCRY8xuzxm91zUf0f1NW8m5XVI93ax2Toar/gksAx
    5X+RI1UkaeGkVltucFAH0GXZ
    -----END CERTIFICATE-----
    subject=/CN=fixes.co.za
    issuer=/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    ---
    No client certificate CA names sent
    ---
    SSL handshake has read 3417 bytes and written 444 bytes
    ---
    New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
    Server public key is 2048 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    No ALPN negotiated
    SSL-Session:
        Protocol  : TLSv1.2
        Cipher    : ECDHE-RSA-AES256-GCM-SHA384
        Session-ID: B895FE1CB7B513AF123A0CE767FB48FA0E724E9E68C9430932817A5D87820ADB
        Session-ID-ctx: 
        Master-Key: 37D4483776B0F2B13DD426967AC5CE40DBA8742CA5B75204CB32B1A33EF8369889660F3DDBEFDC086CAEFF57FDB50563
        TLS session ticket lifetime hint: 300 (seconds)
        TLS session ticket:
        0000 - 2a 85 67 25 90 fe 1a 30-b6 08 a2 9e 7f 86 9f 58   *.g%...0.......X
        0010 - 6c eb 38 2c 97 ea f8 a9-5f c3 46 98 71 0c 45 46   l.8,...._.F.q.EF
        0020 - 8e ad c2 f1 20 26 a1 d6-20 55 97 7c 27 f2 22 b5   .... &.. U.|'.".
        0030 - 43 26 62 4d e0 ef 09 f2-4a 2e ca f8 a1 b1 1a 9c   C&bM....J.......
        0040 - 57 de 4f 50 52 c2 95 12-73 f6 91 10 63 85 37 a4   W.OPR...s...c.7.
        0050 - e2 e9 dd cc d9 c4 f6 d1-55 5e 3e 8b ed 28 0f d8   ........U^>..(..
        0060 - 80 8e 9d 91 b6 ab fb 78-e4 3c 02 4b 6b 98 fc 74   .......x.<.Kk..t
        0070 - 8f 34 18 76 ed 58 3c 81-e3 da 48 5f 0e 10 3f 51   .4.v.X<...H_..?Q
        0080 - f7 ca 21 ae 2c 89 4f 6f-c8 e7 56 1f 5a 3f 8f d0   ..!.,.Oo..V.Z?..
        0090 - a2 6e dd d6 c6 07 7e d4-e5 d3 2c 14 82 13 cd c0   .n....~...,.....
        00a0 - 36 0d 00 3a 1e c9 05 c2-38 91 c3 c1 ed 84 87 d0   6..:....8.......
        00b0 - a3 9c 90 4b be 46 5b 71-5a 5b e8 08 15 af 37 e1   ...K.F[qZ[....7.

        Start Time: 1591853317
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)
    ---
    read:errno=0

Before the first certificate, there is a _certificate chain_

The line starting with `s` is the subject name, the line starting with `i` is the issuer.
In our case:

    Certificate chain
    0 s:/CN=fixes.co.za
    i:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    1 s:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
    i:/O=Digital Signature Trust Co./CN=DST Root CA X3

Certificate 0 is the one recieved by `fixes.co.za`. Certificate 1 belongs to the entity that signed certificate 0.
The organisation that issued certificate 1 is Let's Encrypt Authority X3.

CA organisations must ensure to be trustworthy only giving certificates to verified owners and protect their private keys.
Otherwise an attacker could issue certs for `fixes.co.za` on their behalf.

To see what is in a certificate:

    openssl x509 -text -noout <then paste the Server Certificate from above>

The info returned:

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                03:3e:df:79:7f:7d:4a:ab:a0:16:42:14:13:96:06:b3:9d:dc
        Signature Algorithm: sha256WithRSAEncryption
            Issuer: C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
            Validity
                Not Before: May  8 22:48:29 2020 GMT
                Not After : Aug  6 22:48:29 2020 GMT
            Subject: CN=fixes.co.za
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    Public-Key: (2048 bit)
                    Modulus:
                        ...
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
                X509v3 Extended Key Usage: 
                    TLS Web Server Authentication, TLS Web Client Authentication
                X509v3 Basic Constraints: critical
                    CA:FALSE
                X509v3 Subject Key Identifier: 
                    77:33:D9:78:64:C1:31:18:C7:23:7C:FB:F5:68:04:C0:EE:83:1B:21
                X509v3 Authority Key Identifier: 
                    keyid:A8:4A:6A:63:04:7D:DD:BA:E6:D1:39:B7:A6:45:65:EF:F3:A8:EC:A1

                Authority Information Access: 
                    OCSP - URI:http://ocsp.int-x3.letsencrypt.org
                    CA Issuers - URI:http://cert.int-x3.letsencrypt.org/

                X509v3 Subject Alternative Name: 
                    DNS:blog.how-to-trade.co.za, DNS:fixes.co.za, DNS:how-to-trade.co.za, DNS:matomo.fixes.co.za, DNS:number1.co.za, DNS:synergysystems.co.za, DNS:www.fixes.co.za, DNS:www.how-to-trade.co.za, DNS:www.number1.co.za, DNS:www.synergysystems.co.za
                X509v3 Certificate Policies: 
                    Policy: 2.23.140.1.2.1
                    Policy: 1.3.6.1.4.1.44947.1.1.1
                    CPS: http://cps.letsencrypt.org
        Signature Algorithm: sha256WithRSAEncryption
            ...

`openssl` knows how the certificate is structured and can give us relevant info.

### The Record Protocol

All data exchange is done through TLS records, the data packets used by TLS.
The TLS Record Protocol is essentially a transport protocol agnostic of the transported data's meaning - making TLS suitable for any application.

It is used to carry data exchange during the handshake.
Once handshake is complete both parties share a secret key, application data is fragmented into chunks as part of TLS records.

#### Structure of a TLS Record

* Chunk of data at most 16 kb.
* first byte is type of data (`ContentType`): `22` - handshake, `23` - encrypted data, `21` - alerts
* second and third byte set the `ProtocolVersion`
* fourth and fifth bytes - encode the length of the data
* the rest of the bytes is the data to transmit - `payload`

TLS record header has only 3 fields. The IPv4 packet includes 14 fields before payload, TCP has 13.

When the ContentType is 23, its payload contains of ciphertext and an authentication tag.
You know the cipher and key, because they are established in the handshake.

#### TLS 1.3 Cryptographic Algorithms

TLS 1.3 uses Authenticated encryption, key derivation function (hash from key) and a Diffie-Hellman operation.

Authenticated Ciphers: `AES-GCM`, `AEC-CCM` and `ChaCha20`
Key derivation: `HKDF` based on `HMAC`
Diffie-Hellman operation: Elliptic Curve Cryptography

### TLS 1.3 improvements over TLS 1.2

Gets rid of weak algorithms: `MD5`, `SHA-1`, `RC4` and `AES in CBC mode`

**More in the book**

### The Strength of TLS

Forward secrecy - an attacker getting a session key can only decrypt from the current session not previous sessions.
Ensure to erase keys from memory.

### How Things can go Wrong

#### Compromised Certificate Authorities

Root CA's are organisations trusted by browsers to validate certificates served by remote hosts

The assumption is that the CA has verified the legitimacy of the certificate owner.
The browser verifies the certificate by checking its CA issued signature.
Since only the CA knows the private key required to create the signature we assume others cannot create valid certificates on behalf of the CA.
Very often a websites certificate won't be signed by a root CA but by an intermediate CA, which is connected to the root CA through a certificate chain.

If the CA's private key is acquired, the attacked can create a certificate for any url without owning it.

This happened in 2011 with the Diginotar hack.

#### Compromised Server

If a server is breached, all is lost. The attacker can view info before it is encrypted and after receiving - decrypted.

> Fortunately, such security disasters are rarely seen in high-profile applications such as Gmail and iCloud, which are well protected and sometimes have their private keys stored in a separate security module

SQL injection and cross site scripting are mostly independent of TLS and can be done over a secure TLS connection

#### Compromised Client

An attacked could install a rogue CA certificate in the client’s browser to have it silently accept otherwise invalid certificates, thereby letting attackers intercept TLS connections

## 14. Quantum and Post Quantum 

**Lots of info in the book**

## Source

* [Serious Cryptography - Jean-Philippe Aumasson](https://nostarch.com/seriouscrypto)