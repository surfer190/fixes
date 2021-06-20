---
author: ''
category: Bitcoin
date: '2021-01-04'
summary: ''
title: Grokking Bitcoin Notes
---

Bitcoin prevents cheating - making it impossible, impractical or less profitable than honest behaviour

If no one can cheat there is no need for banning - no need for a trusted authority - therefore everyone can participate

> Bitcoin will give people an opportunity to opt out of the system that’s holding them hostage

## History

* October 2008: Satoshi Nakamoto publishes [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/en/bitcoin-paper)
* January 2009: Nakamoto publishes the first program

Bitcoin is a _complex_ system.

## 1. Introduction to Bitcoin

### What is Bitcoin?

* Digital cash system - without a bank or trusted third party
* Has free-floating exchange rate with other currencies - can be bought on exchanges
* bitcoin network are collectively run by anyone who runs a node
* No special permission is needed to participate

**Bitcoin** capital **B** is the network.

_bitcoin_ small _b_ is the currency unit

Its stock market ticker is `BTC`

Participants:

* End users - day-to-day users savings, shopping, speculation and salaries
* Corporate users - paying wages
* Merchants - those accepting bitcoin payments
* Bitcoin services - anonymisation, remitance or tipping
* Exchanges - entities uses can use to exchange bitcoin to fiat or shitcoins
* Protocols - payment network, decentralised exchanges
* Bitcoin developers - contributors to the open source code that runs the network

Bitcoin network:

* processes payments
* secures the ledger from unauthorized modifications
* get new bitcoin into circulation at a predetermined rate

### Sending bitcoin

Alice creates the transaction locally and then sends it to the bitcoin network.

1. Alice gets Bob's wallet address - transaction is created by signing it with alice's digital signature
2. Sent to the network
3. Bitcoin nodes verify and pass the transaction on
4. One nodes sends a block of new transactions to the network - each node verifies and adds it to the blockchain
5. When the node bob is connected to updates the ledger that includes alices transaction - bob's wallet will have the money in

> Alice does not actually send anything - she simply says to the network should verify a movement of funds (transaction)

The `blockchain` is a database of all transactions ever made

A transaction contains:

* The amount to move
* The bitcoin address to move to
* A digital signature (made by alice's private key)

The digital signature is created from the transaction and a huge secret number (called a private key - that only alice has access to)

Alice sends the transaction to one or more Bitcoin nodes.
The nodes verify that:

* the bitcoin that alice spends exists
* alice's digital signature is valid

> Invalid transactions are dropped - they won't reach further than the first node

If checks pass the nodes `relay` the transactions to peers.

Many transactions are happening at a time - so to coordinate one node has to take the lead and say what order the transactions are in - forming a _block_.
Other nodes verify this block.

> The blockchain is append only

The node that takes the lead is rewarded with newly minted bitcoin and transaction fees of the transactions in that block.

Why wouldn't ever node want to take the lead? The node has to solve a hard problem - consuming considerable time and energy.

The problem is so hard that most nodes do not try - nodes that do try are called _miners_

A typical bitcoin wallet will:

* manage keys
* watch incoming and outgoing bitcoin
* send bitcoin

The private key:

* creates digital signatures
* generates the bitcoin address(es)

> Bitcoin would not be this widespread if it did not solve real world problems

### Problems

* `Segregation` - Banking services can be denied to people with certain political views or those conducting certain business
* `Privacy` problems - trace, censor, freeze and seize. Cash is being phased out - someone will always be recording a transaction. Smart shopper.
* `Inflation` - purchasing power of currency decreasing. Debasement. Zimbabwe 2007-2008 hyper-inflation. Yugoslavia and Ukraine (1992 - 1994), Peru (1990), Venezuela (2012 - current)
* `Borders` - Moving fiat money across borders is expensive and sometimes forbidden


> You might say you are happy for government and companies to see your private data - but you don't know who will run these organisations in the future and what else they are doing with the data.

> We have seen free speech platforms being cancelled from receiving online payments . Cyprus seized 47.5% of all transactions over 100k euros

Governments (central banks and commercial banks) increase money supply as a tool to extract value from a population and pay for expenses such as national debt.

### Major Differences of Bitcoin vs Traditional

* Decentralised - control is distributed among nodes (the service is not controlled by a single entity) - all users are treated equally - changing the rules are impossible without concensus
* Savings - keep money safe by securly storing the private keys
* Shopping - currently your details are saved - vulnerable to hackers.
* Speculation - alluring price volatility. Its deflationary properties will emerge over time.
* Ownership - bitcoin lets you embed certain bits of information with payments
* Proof of existence - prove a document existed prior a certain point. A digital document has a _fingerprint_, a cryptographic hash that anyone can calculate from the document - _higher grade stuff_

> A simple way to save is create a private key and write it down on a piece of paper - the piece of paper is now your account - your _wallet_

There are different ways to store your account - security vs convenience

* Bitcoins money supply is limited to 21 million bitcoin - you will maintain your percentage of moey supply. Money supply increase will stop around 2140.
* supply increases half every 4 years
* You need 60 minutes to be sure of a transaction
* bitcoin payments are tied to _public keys_, you show ownership by showing that you own the private key for that specific public key.

Bitcoin exchanges in venezuela have less supply and higher demand - therefore the price may be higher there.

As at 15 February 2021:

    ubuntu@btc:~$ bitcoin-cli gettxoutsetinfo
    {
        "height": 670767,
        "bestblock": "00000000000000000009f8b52fdc812be467e20c49d3495a9367e8d280013324",
        "transactions": 43829187,
        "txouts": 71323024,
        "bogosize": 5348040799,
        "hash_serialized_2": "ebec41c496b8653a696a9b91b681a0af92a8d7752369ede1dd4430117bf32e51",
        "disk_size": 4346605121,
        "total_amount": 18629601.20017421
    }

There have been `18,629,601` BTC mined.

### When to not use Bitcoin

* tiny payments - processing fee is relative to the transaction size in bytes - not number of satoshis. The fee for higher value transactions is the same for low value transactions. The fee also depends on the available space in the blockchain - it can only handle 12MB transactions as hour. Miners sometimes have to prioritise transactions paying a higher fee. Sometimes the fee might be higher than the amount you want to send.
* security - you are in charge of the security of your bitcoin - only you!
* instant payments - bitcoin payments take time to confirm



> The end of mining rewards and what transactions are included in the block will be determined by the **free market**. If you do not pay enough of a transaction fee - your transaction will not be added to the blockchain.

The lightning network is built on top of bitcoin and is supposed to fix the tiny payment problem

A sender can double spend a transaction - sending the same transaction to different addresses. The confirmation time of 20 minutes (not 60?) could add friction to seamless transactions.

Security risks:

* You lose your private keys
* Your private keys are stolen
* The government bans and imprisons bitcoiners
* Price of bitcoin swings dramatically
* Software bugs make bitcoin insecure
* Weakness arises in the cryptography

### AltCoins

Cryptocurrencies other than bitcoin are called `alt-coins`

Anyone can create an alt-coin derived from any other open source crypto.
The trick is convincing people to use it.

Bitcoin is sometimes compared to the internet.
Imagine someone creating a new internet using a different protocol. By using that protocol you are no longer connected to the internet. The strength of the internet arises from everyone using it.

> Imagine someone coming up with a different internet (using a different protocol but no superior technology). No one would use it. The current internet is the chosen one and so heavily adopted - that only new technology is intergrated with it. For example IPv6 integrates with IPv4 seemlessly.

_network effect_ people tend to go where other people are

## 2. Cryptographic hash functions and digital signatures

* The spreadsheet is append only
* The reward for seuring and verifying the spreadsheet is halved every 4 years - approaching 0
* Total tokens in circulation will approach 21 million
* You can buy stuff with the tokens, sell tokens for dollars or save them for later

### Cryptographic Hashes

* fingerprints - it is hard to find one the same as another
* the fingerprint does not disclose anything about the person
* Digital information also has fingerprints - the file is sent into a cryptographic hash function - matching this fingerprint ensures that the file has not been modified
* A 256-bit number (32 byte) stores the fingerprint - SHA256 Secure Hash Algorithm
* A hash is also commonly referred to as a _digest_

> bitcoin uses hash functions a lot. On average every 10 minutes - a new hash of the entire payment history is created.

Example:

Hexadecimal is base 16

    a1 02 12 6b c6 7d
    
    a1 = 10 * 16^1 + 1 * 16^0
    a1 = (10 * 16) + (1 * 1)
    a1 = 160 + 1
    a1 = 161
    
    a1 02 12 6b c6 7d = 161 + 2 + 18 + 107 + 198 + 125
    a1 02 12 6b c6 7d = 99
    
    99 / 16 = 6 remainder 3
    
    59 = 93 (base 16)

Hashing with the above has 256 possible outcomes - since the hash function outputs a single byte (8 bit)

The SHA256 has so many possible outcomes - a duplicate is virtually impossible

Properties of a hash function:

* slightly different inputs produce very different hashes
* The same inputs always produce the same hash
* The hash produced is always the same size
* You cannot reverse engineer a hash, they are one way and require brute force trial and error

Suppose you want to find a preimage that results in teh same hash as `hello!` - the only way to find this is one-on-one until all inputs are exhausted checking the output against the original hash.

### How big is 2^256?

It is about 10^77 - almost the number of atoms inthe universe

Finding a preimage of SHA256 is like picking an atom in the universe.

A desktop can calculate 60 million hashes a second. The expected number of tries needed to find a solutions is 2^255.

    = 2^255 / (60 * 10^6)
    = 10^68 seconds
    = 3 * 10^61 years

Some well known hash functions:

* SHA256 - 256 bits - secure - used in bitcoin
* SHA512 - 512 bits - secure - some wallets
* RIPEMD160 - 160bits - secure - yes
* SHA-1 - 160 bits - not secure (a collision has been found) - not used in bitcoin
* MD5 - 128 bits - collisions can be trivally created - not used in bitcoin

### Digital Signatures

* Signature is derived from a random number (called a private key)
* Much harder to forge than a human signature

Private keys create signatures, public keys verify signatures.
You give your public key to the verifier to verify your digital signature has not been modified

1. You generate a private- public key pair. The public key is calcualted from the private key. You give the public key to your friend.
2. You digitally sign your file with the private key
3. Your friend uses the public key to verify the signature

Deriving a public key from a private key is one-way. Running the same private key through a derivation function always produces the same public key.

The public key is `33 bytes` (66 hex digits long) where a private key is `32 bytes` (63 hex digits)

The public key can be used to encrypt messages that only the private key can decrypt. **Bitcoin does not use this property of key pairs at all**.

The private key can encrypt messages that only the public key can decrypt. Not usually done - as teh public key can decrypt it - but it is useful if you want it to be publicly verifiable.

To make a payment now:

1. John writes the message of how much he is sending and to who
2. The message is SHA256 hashed
3. The hash (fingerprint) is encrypted with John's private key. This signature is sent with the message.

> An encrypted hash is the _signature_

To verify the payment:

1. Lisa sees a message claiming to be from John (she looks up Johns public key)
2. Lisa decrypts the signature with John's public key. The result of that should be a SHA256 hash of the message john sent.

It proves that John's key was used to sign this transaction.

> This only works if both Lisa and John used the same signature verifying scheme

### Private Key Security

John is in control of his tokens because he owns the private key.
If the private key is stolen he can lose all his tokens.

A theft happens - Lisa tells John that he transferred 90 tokens to Melissa.

1. Melissa managed to access Jon's private key
2. Melissa sent Lisa a message notifying her that she is new and gave her - her public key
3. Melissa used John's private key to create the signature for the transfer

> John requests a refund - Lisa cannot do it as it is a perfectly valid transaction. His failure to secure his private key is his problem.

**You are responsible - you have full responsibility for your private keys**

Lisa stops caring about faces and names - and starts only caring about public keys.

> No one can restore your private key if you lose it

* Storing your private key in cleartext on a shared device means anyone can use it
* Storing the private key in an encrypted file with a password only john knows is better

If however you have a large amount linked to a private key - you would want to use even more secure strategies.
There is a tradeoff between security and convenience.

* Offline vs Online - offline is stored on a device with no network access (more secure the private key can only be taken physically)
* Cleartext vs Encrypted - even with access to the key they need a password to decrypt it
* Whole key vs split key - if your private key is split into 3 parts - then an attacker needs access to all 3 parts

> The greater the security against attackers - the greater the risk of loss

## 3. Addresses

Using hashes public keys instead of names is important to retain privacy.

* Lisa no longer needs to track names.
* A typing error - could leave the money digitally burned

An insurance company asks for the spreadsheet to adjust premiums based on the cookie buying habits of the company staff.

Messages now consists of:

* amount
* senders public key
* recipients public key
* signature made by the sender's private key

A new person joins - she must first create a key pair.
She gives her public key to the company - the person paying her. She needn't give it to Lisa.

Lisa received the payment from the company, she:

1. verifies the message was signed using the sender's private key
2. verifies that the sender has the amount it is sending (calculating the balance from prior transactions)

This example used email (which has a from field) so we know the originator of the transaction. The bitcoin network uses peer-to-peer.

### Shortening the Public Key

Replacing public key with the RIPEMD60 hash of the SAH256 hash of a public key

33 bytes -> SHA256 -> 32 bytes -> RIPEMD160 -> 20 bytes

The final hash is the PKH _public key hash_

Most bitcoin transactions use this method: `p2pkh` - pay to public key hash

> Using PKH's does not hide personal information any more than public keys

If you send money to a public key hash - for which there is no private key - the money is basically burnt.

A _bitcoin address_ is a converted PKH, written in a way more suitable for humans and safe against spelling errors.

Encoding a PKH with a `Base58check` is more human readable - and only work between users.
The block chain uses only the `pkh`. It is just another way of representing a _pkh_

`base64` is an encoding scheme that each character represents 6 bits of data

Some characters look similar ie. `1` and `l`. Or `O` and `0`. we also want to exclude characters that are hard to type like `+` and `/`

All token addresses will start with `1` (as the version is 0 - encoded to `1`)

You can get the `pkh` from the `Base58Check` while simulataneously checking for typing errors.

The chance that the checksum fails is 1 in (2^32) 4.3 billion 

The pkh can be used by forensics to recognise who the owner is.

> Users can create as many addresses as they like - one for each incoming payment

## 4. Wallets

Wallets are not part of the bitcoin network

What do wallets do?

* Create new addresses
* store private keys
* transfer payment details between users
* keep track of funds
* automate the payment process
* backup private keys

Popular wallets:

* Bitcoin core
* Electrum
* Greenbits
* BRD (Bread)

> wallets do not actually contain money - it contains the key to spend money - the money is stored in the spreadsheet

### QR Codes

QR - Quick Response

1. Cafe asks wallet to create a new address and requests a certain amount to it - a QR is created
2. John points his phone camera at the QR code to scan the payment details (uri) - Universal resource locator. `ct:19wZ...?amount=10`
3. John's wallet displays the payment details to him
4. He verifies and teh wallet creates the transaction

[Bitcoin improvement proposals](https://github.com/bitcoin/bips/blob/master/README.mediawiki)

BIP21: Sending bitcoin with a `url` - `bitcoin:zs3d...?amount=10`

The transaction is pending until it shows in the spreadsheet

_unconfirmed_ means the payment has been created and sent to the Bitcoin network but isn't yet part of the blockchain.

### Private Key Backups

Your keys hold your momney. If you lose your keys you lose your money.

You should not ever backup or send private keys via email - any system in the middle can get the data..
Doing backups for each new key becomes tiresome for the user.

Encrypt the private keys with a password.

entropy means disorder or uncertainty

If you select 8 characters from a set of 64 possible your entropy is:

    2^6 (6 bits) == 64 
    6 * 8 = 48 bits of entropy

for the same entropy from words selected from 2048 words you need:


    2^11 = 2048 bits
    4 * 11 = 44 bits
    5 * 11 = 55 bits

> Choosing 1 word is equivlant to 48 coin flips

The more an attacker knows about the password the less the entropy

If she knows the password is 8 characters long chosen from a possible 64 and that the third letter is `3`, the entropy is `6 * 7 = 42 bits`

if John cherry picks a password, say 100,000 common words and names come in 100,000 variations.
That is **100 billion** passwords corresponding to 37 bits of entropy.
A high end pc will take a few days to perform the brute force.

If a truly random password is chosen: it would take around 2000 days to crack.

Password encrypted backups have issues:

* More things to secure - backup file and password
* Forgotten passwords - rarely used passwords will be forgotten
* Technology advances - passwords can be cracked faster
* Randomness is hard for a human

### Hierachical Deterministic Wallets

BIP 32 

If all private keys generated were generated from a single random number - called a _random seed_ - the whole wallet could be backed up by writing down the seed phrase and store it in a safe place.

BIP 44

Organising keys based on their purpose. A _master private key _ is the key that all others are derived from.

The _master extended private key_ is derived from the seed

> An `xprv` _extended prviate key_ contains 2 items: private key and chain code

A random seed 128 or 256 bits - is hashed with `HMAC-SHA512` is split into the left 256 bits - the master private key and the right 256 bits - the chain code.

HMAC - Hash-based Message Authentication Code

You have created an HD wallet - the minimum you need to back it up is the `seed`
The key paths are standardised if you know the seed apparently.

The seed is 16 bytes (128 bit) - 32 hex digits

Write down the seed once and lock it in a safe.
Problem again is if you make a mistake.

BIP39 - Mnemonic sentences

You can display the seed as a sequence of 12 words

```
Seed: 16432a207785ec5c4e5a226e3bde819d
Mnemonic: bind bone marine upper gain comfort defense dust hotel ten parrot depend
```

This encodes the seed in a more readable way. All private keys can be regenerated from the seed.

There are 2048 words in a wordlist

More info in the book about seeds

### Extended Public Keys

It gets hectic now but this is how addresses can be created for online stoes...I think.

### Public key math

It gets hectic...elliptic curve etc

## 5. Transactions

Transactions must replace the email system - so anyone can view transactions and verify them.

Lisa prevents cheatings by:

* verifying digital signatures
* checking public key hash balances before confirming a payment

Problems:

* Ledger is growing - each check becomes more time consuming
* 2 seperate addresses must be combined to make bigger payments
* Trust in Lisa is dropping

### Minimise the Need for Trust

Allow anyone to verify transactions.
Wallets will now create transactions - instead of sending emails.

John scans the payment QR code and the wallet creates the transaction.

Transaction contains:

* where to send the money
* what money to spent (UTXO's) - unspent transaction outputs

3 phases:

1. Create
2. Confirm
3. Verify

### Creating the Transaction

John has 2 UTXO's with 8CT and 5CT.
A transaction input referencing the 2 transactions - a _txid_.
The txid - is it's double SHA256 hash - to apparently prevent a _length extension attack_.

The 2 inputs:

* txid of transaction 1, index of the output of transation 1 to spend, signature
* txid of transaction 2, index of the output of transaction 2 to spend, signature

The 2 output:

* pays 10CT to PKH (of cookie shop)
* pays 3 CT back to John (the change)

Change is needed as you cannot partly spend a transaction output

#### Transaction Fee

Sum of the input must be greater or equal to the sum of the outputs - the difference is called a transactino fee.

Anyone could have created this transaction - it is public information.
But only john can sign the transaction as he has the private keys for the inputs.

Signatures need to be made for the inputs - different keys must sign money sent to different addresses.

The signature will hash the entire transaction - except the signatures.

The public key must also be added to the transaction

### Confirming the Transaction

* Transaction spends outputs that actually exist - and aren't already spent
* Total value of output does not exceed the inputs
* The signatures are correct

How do you know if the output has already been spent? **UTXO set**

All nodes maintain a private UTXO set to speed up transaction verification

A UTXO entry consists of: a txid, an index (indx) and the actual transaction output

If the outputs do not exist - John is trying to spent money that never existed or is already spent.
Double Spend - spending the same output twice.

The confirmed transaction is added to the spreadsheet.
The newly spent outputs are removed from the UTXO set.

The UTXO set can be created from anyone with access to the spreadsheet.
Start with an empty UTXO set and apply transactions one by one.

### Verify the Transaction

Anyone can verify that the transaction is legit and comply with the agreed upon rules.

Full nodes == verifying node

If Lisa tries to modify the transaction in the spreadsheet to sent the 10CT to Lisa instead of the cafe - the transaction signatures will no longer be valid.

The public signatures mean anyone can verify the transaction.

**The public key is revealed in the spending actions input when an output is spent**

> Don't reuse addresses

If John has other unspent outputs to PKH1 - they are now less secure. They are no longer protected by the cryptographic hash - only the public-key derivation.

Most wallets will create unique addresses for all incoming payments.

### Account-based System to a Value-based System

An account based system keeps track of how much money each account has.
A value based system keeps track of the currency instead.
Specific unspent currency (UTXOs)

A transaction output does not actually show the public key hash (PKH) - only a part of a program - a _pubkey script_.
The input that spends the output contains the other part of the program - _signature script_

Written in the `Script` programming language

book goes into detail about the Script commands...

Payment types:

* p2pkh - pay to public key hash
* pay-to-hash
* multisignature - allow for multiple people to have a quorum on payment (charity and fundraising)
* pay-to-script

### More Transaction stuff

* _version_ - Either 1 or 2
* _sequence number_ - FFFFFFFF - old disabled feature
* _lock time_ - a point in time before which the transaction cannot be added to spreadsheet

### Rewards and Coin Creation

A special transaction, a _coinbase_ transaction - coin creation reward.
Index is `-1` and input is all zeroes.

Rewards in bitcoin are paid every 10 minutes.

**All transactions can be traced back to coinbase transactions** - by following the `txid` references in transaction inputs.

Transaction to transactions - at agreed upon time. One huge transaction with the existing UTXO set as outputs.

### Censoring and Reverting

Lisa can still censor transactions from a specific person's UTXO set.
Maining that person cannot spend their money.

Lisa can also remove a transaction where the outputs are unspent.
Verifiers starting after the reversion will not notice.

It will be unnoticed until John tries to spend the output of John's transaction.
Now if the Cafe accepts - Veras will reject the spreadsheet.

However - it is one word against someone else's.

## 6. The Blockchain

The blockchain makes transactions secured from tampering through hasing and signing the set of transactions in a clever way.

Cryptographic proof of fraud.

All verifiers keep their own copy of the blockchain.

We need to make it provable that the history has been changed.

Blockchain - a chain of blocks that contain transactions and each block references its predecessor.

The bitcoin clockchain contains many blocks. You can get the count with bitcoin-cli.

    bitcoin-cli getblockcount
    675769

Each block references teh previous block and has an implicit height - distance from the first block (height 0).
The _chain tip_ is the last block.

Each block contains transactions but also contains a _block header_ - to protect the integirty of the contained transactions and the blockchain before it.

block header consists of:

* The double SHA256 hash of the previous block's header
* combined hash of the transactions in the block - the _merkle root_
* a timestamp of the block's creation time
* Lisa's signature of the block header

### Creating the Block

Lisa creates the block every 10 minutes containing unconfirmed transactions.
Lisa writes the file to a shared folder - everyone can creat and read but not change or delete.

Bitcoin uses a peer-to-peer network instead of the shared folder

An unsigned block template is created.

#### Block Rewards

The block reward contains newly created money and transaction fees.
Newly created money in a block is called the _block subsidy_.

Bitcoin blocks are signed with _proof of work_

If anything in the previous block changes the new block will have to change - as it links to a hash of the previous block header.

Once the block is signed it is made available to verifiers - the peer-to-peer network / shared folder.

Any unconfirmed transactions can be selected - the transaction order isn't important - as long as all transactions spend outputs already present in the blockchain.

Verifying a block:

* block header signature is valid
* the previous block id exists
* all transactions in the block are valid, using the UTXO set
* combined hash of all transactions match the merkle root
* the timestamp is within reasonable limits

2 different signed versions of a block exist - proving she cheated.

Why use a blckchain at all? 
why not just sign all transactions that have ever happened.

- as the number of transactions grow - it will take longer to sign the transactions
- time it takes to verify will increase
- maintaining the utxo set is harder for verifiers - as it is hard to know what is new

### Lightweight Wallets

A full node knows about every transaction in history - since block 0 - the genesis block.
No trust is needed with financial information - it is all in the blockchain.

A lightwieght wallet is also known as a SPV - simplified payment verification.

Full nodes let lightweight wallets get specific information from them over the internet (BIP37)

More info in the book...

### Markle Trees

Intense...more in the book.






























