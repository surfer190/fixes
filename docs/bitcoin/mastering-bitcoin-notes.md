---
author: ''
category: Bitcoin
date: '2020-11-02'
summary: ''
title: Mastering Bitcoin Notes
---
# Mastering Bitcoin Notes

## 1. Introduction

* Bitcoin - collection of concepts and technology forming the basis of digital money
* Units of currency called _bitcoin_ are used to store and transmit value on the bitcoin network.
* Communicate primarily with the internet
* Users transfer bitcoin on the network - to buy, sell, send money and extend credit.
* Can be purchased and sold for other currencies at exchanges

> Perfect form of money for the internet - entirely virtual, fast, secure and borderless

* The coins are just implied transactions
* Users own _private keys_ that allow them to prove ownership of bitcoin in the bitcoin network
* The keys are used to sign transactions and transfer them to other participants
* Possession of the key is the only prerequisite - putting control in the hands of the owner - their own bank. **No trusted third party is required**
* No central point of control

### Mining

* Bitcoin are created through mining - competing to find solutions to a mathematical problem while processing bitcoin transactions
* Any participant in the bitcoin network (i.e., anyone using a device running the full bitcoin protocol stack) may operate as a miner, using their computer’s processing power to verify and record transactions.
* Bitcoin mining decentralizes the currency-issuance and clearing functions of a central bank and replaces the need for any central bank
* The bitcoin protocol includes built-in algorithms that regulate the mining function across the network - on average someone succeeds every 10 minutes.
* Halves rate at which new coins are created every 4 years
* Amount in circulation follow a curve that approaches 21 million by the year 2140

    21,000,000 * 10 = 210,000,000 minutes / 60 = 3,500,000 hours / 24 = 145,833 days ~= 400 years

* Due to bitcoin’s diminishing rate of issuance, over the long term, the bitcoin currency is deflationary
* Bitcoin is also the name of the protocol - the peer-to-peer network

Bitcoin consists of 4 parts:

* Decentralised peer-to-peer network (bitcoin protocol)
* A public transaction ledger (blockchain)
* A set of rules for independent transaction validation and currency issuance (consensus rules)
* Mechanism for reaching global decentralized consensus on the valid blockchain (proof-of-work algorithm)

### Digital Currencies

3 basic questions for those accepting digital money:

1. Can I trust it is not counterfeit and authentic?
2. Can I trust it can only be spent once?
3. Can no one else claim this money belongs to them?

> For digital money - cryptography for the basis of the legitimacy of a user's claim to value

Digital signatures enable a user to sign a transaction proving the ownrship of that asset.

Centralisation of early currencies made them fail.
Parent companies and governments regulated and litigated them out of existence.

### History of Bitcoin

Invented in 2008 with the publication of _Bitcoin: A Peer-to-Peer Electronic Cash System_ - under the alias "Satoshi Nakamoto".
Used prior inventions `b-money` and `HashCash` to create a decentrlaised currency issuance and validation system.

The _Key innovation_ was the proof-of-work algorithm to conduct a global election every 10 minutes - allowing the network to arrive at a consensus every 10 minutes about the state of transactions.

Solving the `double spend` problem needing a central clearing house.

The bitcoin network started in 2009 based on a reference implementation by nakamoto.

The implmentation of the proof-of-work algorithm (mining) has increased in power exponentially.

Satoshi Nakamoto withdrew from the public in April 2011.

> See: Byzantine Generals’ Problem

### Bitcoin uses, users and their stories

> At its core, money simply facilitates the exchange of value between people

## Getting Started

Bitcoin is a protocol that can be accessed using a client application that speaks the protocol.
A `bitcoin wallet` is the most common interface into the bitcoin protocol.

Just like a web browser is the most common interface into the HTTP protocol.

There are many implementations of wallets, just like browsers (firefox, brave, safari etc.)
Bitcoin wallets vary in quality, performance, privacy adn reliability.
There is also a reference implementation called `Bitcoin Core`.

### Types of Wallets

* Desktop wallet - Running on desktop OS
* Mobile wallet - iOS or Android
* Web wallet - Accessed through web browser, wallet is stored by third party. Take control of bitcoin keys.
* Hardware wallet - secure self-contained bitcoin wallet. Considered secure and suitabel for storing large amounts.
* Paper wallet - keys are printed for long term storage. 

Another way to categorise clients:

* Full node: client that stores the entire hsitory of bitcoin transactions, can intiiate transactions directly on the bitcoin network. Handles all aspects of the protocol and can independently validate the entire blockchain.
* Lightweight client: SPV (Simple payment verification) connects to full nodes for access to transaction history - but stores the user wallet locally. Indepently creating, validating and transmitting transactions.
* Third party API client: Interacts with bitcoin through a third party API rather than connecting to the network directly.

Most important information is the _bitcoin address_...a QR code contains the same information.

Example bitcoin address: `1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK`

> Bitcoin addresses start with `1` or `3`. There is nothing sensitive about a bitcoin address. It can be posted anywhere and you can create new addresses as often as you like. All of which will direct funds to your wallet.
Many modern wallets create a new address for every transaction to maximise privacy.

_a wallet is collection of addresses and the keys that unlock the funds within_

Each address has a corresponding private key.

> Until the moment this address is referenced as the recipient of value in a transaction posted on the bitcoin ledger, the bitcoin address is simply part of the vast number of possible addresses that are valid in bitcoin

### Getting your first Bitcoin

_Bitcoin transactions are irreversable_

> For someone selling bitcoin, this difference introduces a very high risk that the buyer will reverse the electronic payment after they have received bitcoin, in effect defrauding the seller. To mitigate this risk, companies accepting traditional electronic payments in return for bitcoin usually require buyers to undergo identity verification and credit-worthiness checks, which may take several days or weeks.

Methods for getting bitcoin:

* From a friend
* [Local calssified](https://localbitcoins.com/) for cash in area
* Earn bitcoin by selling a product or service
* Use a [bitcoin ATM](https://coinatmradar.com) - accepts cash and sends bitcoin
* Use a bitcoin exchange

> One advantage of bitcion is the enhanced privacy. Acquiring, holding and spending does not require giving personal information to 3rd parties.

Where bitcoin touches traditional systems - exchanges - regulations apply.

> Users should be aware that once a bitcoin address is attached to an identity, all associated bitcoin transactions are also easy to identify and track.

This is one reason many users choose to maintain dedicated exchange accounts unlinked to their wallets.

**mistakes are irreversable**

When sending money:

1. A transaction is made and signed with the sender's private key
2. the transaction is transmitted via P2P protocol - propagating around the network nodes within seconds.
3. The receiver is constantly listening to published transactions on the ledger - looking for any transactinos that match her wallet.

> Confirmations - Inital transactions show as `unconfirmed`. Meaning transaction has been propagated to the network but not recorded in the ledger - the blockchain. Transactions must be included in a block - this is done every 10 minutes.

# 2. How Bitcoin Works

* Based on decentralised trust. Not a central authority.

The bitcoin system consists of:

* wallets - keys and addresses
* transactions - propagated over the network
* miners - produce the consensus blockchain through competitive computation

Bitcoin explorers:

* [https://live.blockcypher.com/](https://live.blockcypher.com/)
* [https://www.blockchain.com/explorer](https://www.blockchain.com/explorer)
* [https://bitpay.com/insight/#/ALL/mainnet/home](https://bitpay.com/insight/#/ALL/mainnet/home)

A business will present a payment request QR code.
That contains:

* destination bitcoin address
* payment amount
* generic description

Helps the wallet to prefill information.

Eg.

```
bitcoin:1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA?
amount=0.015&
label=Bob%27s%20Cafe&
message=Purchase%20at%20Bob%27s%20Cafe
```

> A 1/100,000,000 of a bitcoin is called a `satoshi`

Transactions to that wallet can be seen at: [https://live.blockcypher.com/btc/address/1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA/](https://live.blockcypher.com/btc/address/1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA/)

I could not find the exact transaction on that page.

## Bitcoin Transactions

In simple terms the owner of some bitcoin authorizes the transfer to another owner. A chain of ownership.

Inputs and outputs to a transaction are not always equal. Outputs are slightly less than input due to a transaction fee.
A small payment that a _miner_ receives.

The transaction also contains a proof of ownership of the amount being spent in the form of a digital signature.
Spending is _signing_ a transaction - from a previous owner to a specific bitcoin address.

If you only had an existing 20 bitcoin tranasction, trying to buy an item costing 5 bitcoin.
Then you would pay 20 bitcoin - 5 bitcoin to the store owner - 15 bitcoin back to yourself (less the transaction fee).

This _change address_ does not have to be the same address as the input, for privacy reasons it is often a new address from the owner's wallet.

Wallets create the aggregate amount in different ways - some take many small transactions to make the exact amount.
The transaction will generate change - similar to how you get change at a shop.

> Transactions move value from _transaction inputs_ to _transacton outputs_

### Common Transactions

A purchase with change.

    Input 0 (from Alice signed by Alice) -> Output 0 (To bob) 
                                         -> Output 1 (To alice - change)

Aggregates many transactions into a single one - piling up coins.

    Input 0 -> Output 0
    Input 1 ->
    Input 2 ->
    Input 3 ->

One input to multiple participants (payroll)

    Input 0 -> Output 0
               Output 1
               Output 2
               Output 3
               ...
               Output n

## Constructing a Transaction

Alice just sets a destination and an amount - the wallet does the rest.

A wallet application can construct transactions even if it is completely offline.

A transaction does not need to be constructed and signed while connected to the bitcoin network

Most wallets keep track of available outputs belonging to addresses in the wallet.

> A bitcoin wallet application that runs as a full-node client actually contains a copy of every unspent output from every transaction in the blockchain

Lightweight clients only track the user's own unspect outputs.

If a wallet does not keep the transactions - it can query the network

Lets look up the inspent outputs from Alice's bitcoin address:

    http https://blockchain.info/unspent?active=1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK
    
    {
        "notice": "",
        "unspent_outputs":
        [
            {
                "confirmations": 378773,
                "script": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
                "tx_hash": "f2c245c38672a5d8fba5a5caa44dcef277a52e916a0603272f91286f2b052706",
                "tx_hash_big_endian": "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2",
                "tx_index": 0,
                "tx_output_n": 1,
                "value": 8450000,
                "value_hex": "0080efd0"
            },
            {
                "confirmations": 323156,
                "script": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
                "tx_hash": "0365fdc169b964ea5ad3219e12747e9478418fdc8abed2f5fe6d0205c96def29",
                "tx_hash_big_endian": "29ef6dc905026dfef5d2be8adc8f4178947e74129e21d35aea64b969c1fd6503",
                "tx_index": 0,
                "tx_output_n": 0,
                "value": 100000,
                "value_hex": "0186a0"
            },
            {
                "confirmations": 315315,
                "script": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
                "tx_hash": "d9717f774daab8d3dd470853204394c82e3c01097479575d6d2ee97d7b3bdfa1",
                "tx_hash_big_endian": "a1df3b7b7de92e6d5d57797409013c2ec8944320530847ddd3b8aa4d777f71d9",
                "tx_index": 0,
                "tx_output_n": 0,
                "value": 1000000,
                "value_hex": "0f4240"
            },
            ...
        ]
    }

[View the transaction of Joe to Alice](https://www.blockchain.com/btc/tx/7957a35fe64f80d234d76d83a2a8f1a0d8149a41d81de548f0a65a8a999f6f18)

### Creating Outputs

Alice's transaction says: This output is payable to whoever can present a signature from the key corresponding to Bob’s public address.

Only Bob has the corresponding keys for that address, only Bob's wallet can present a a signature to redeem it.

Alice will _encumber_ the output value with a demand for a signature from Bob.

Alice's change payment is created by her wallet.

For a transaction to be processed in a timely fashion the wallet will add a small fee.
The fee is not explicit - it is implied. It is the remainder of the outputs - the _transaction fee_

The transaction from Alice to Bob's cafe can be seen [here](https://www.blockchain.com/btc/tx/0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2)

### Adding the Transaction to the Ledger

The transaction created is 258 bytes long.
Now the transaction msut be transmitted to the bitcoin network.

The transaction must become part of a block, the block must be mined and the new block must be added to the blockchain.

The bitcoin network is peer-to-peer - so blocks are propagated to all participants.

The transaction can be sent to any bitcoin node - a computer speaking the bitcoin protoocol.

Any bitcoin node receiving a valid transaction it has not seen before will forward it to all other nodes it is connected to...called _flooding_. The transaction reaches a large percentage of nodes in a few seconds.

Bob's wallet can confirm:

* transaction is well formed
* uses previously unspent inputs
* contains sufficient transaction fees to be included in the next block

> Bob can assume that the transaction will be inlcuded in the next block - you know what they say about _assumptions_

A common misconception is that bitcon transactions must be confirmed by waiting 10 minutes for a new block or up to 60 minutes for 6 full confirmations.
Confirmations ensure the transaction has been accepted by the whole network.
This shouldn't be needed for small purchases - same as credit card these days.

## Bitcoin Mining

A transaction does not become part of the blockchain until it is verified and included in a block called: _mining_.

Bitcoin trust is based on computation. Transactions are bundled into blocks - which require an enormous amount of computation to prove but a small amount to verify.

Mining has 2 purposes:

* Validate transactions by reference to bitoin's _concensus rules_
* Mining creates new bitcoin in each block - dminishing amount of bitcoin

> Mining achieves a fine balance between cost and reward. Mining uses electricity to solve a mathematical problem. A successful miner will collect a reward in the form of new bitcoin and transaction fees - only if validated based on a consensus.

A good way to describe mining is like a giant competitive game of sudoku that resets every time someone finds a solution and whose difficulty automatically adjusts so that it takes approximately 10 minutes to find a solution.
Sodoku can be verified quickly.

The solutions to a block of transactions called _proof-of-work_.
The algorithm involves repeatedly hashing the header of a block and a random number with `SHA256` hashing until a solution matching the pattern emerges.

The first miner to find the solution wins and publishes it to the blockchain.

It is profitable only to mine with application-specific integrated circuits (ASICs) - hundreds of mining algorithms, printed in hardware - running on a silicon chip. 

### Mining transactions in Blocks

Once a new block is published all work moves to the new block.
Each miner adds unverified transactions to the block - along with the block reward and sum of the transaction fees for the block sent to his bitcoin address.
If his solutions is accepted the payment to his bitcoin address is validated and added to the blockchain.

A _candidate_ block is the enw block.

The block containing a transaction is a single confirmation.
Each block on top of Alice's transaction is another confirmation.
Harder to reverse == more trusted.

By conventino more than 6 confirmations is irrevocable.

### Spending the Transaction

Full node clients can track the moment of generation in a block until reaching a certain address.

SPV (Simple payment verification) nodes check that a transaciton exists in the blockchain and has a few blocks added after it.

> Transactions build a chain

## 3. Bitcoin Core: The reference implementation

Bitcoin is an open source proejct and is available under the [MIT license](https://opensource.org/licenses/MIT).

The software was completed before the whitepaper was written.

The _satoshi client_ has evolved into _bitcoin core_.
Bitcoin core is the reference implementation of the bitcoin system.

Bitcoin coin implements all aspects of bitcoin:

* wallet
* transaction and block validation engine
* full network node in peer-to-peer network

**Bitcoin core's wallet is not meant to be used as a production wallet**

Application developers are advised to build wallets with modern standards such as BIP-39 and BIP-32.

A `BIP` is a Bitcoin improvement proposal.

![Bitcoin core architecture](/img/bitcoin-core-architecture.png){: class="img-fluid" }

At time of writing (November 2020) most recent version was `v0.20.1`.

### Running a Bitcoin core node

> By running a node, you don’t have to rely on any third party to validate a transaction

Bitcoin core keeps a full record of all transactions - the blockchain - since inception in 2009.

Why would you want to run a node:

* Developing - a node for API access to the network
* Building applications that must validate transactions according to concensus rules
* To support bitcoin - more robust network
* If you do not want to rely on a third party to validate your transactions

It starts getting deep...more reading in the book

# 4. Keys and Addresses

* Cryptography - secret writing
* Digital signature - prove knowledge of a secret without revealing the secret
* digital fingerprint - prive the authenticity of data

Ironically, the communication and transaction data are not encrypted and do not need to be encrypted to protect funds.

Ownership of bitcoin:

* Keys are not stored in the network - they are created and stored by users in a file (wallet)
* The keys are independent of the bitcon protocol - they can be generated and managed without being connected to the internet
* Bitcoin transactions require a valid signature to be included in the block chain - signatures can only be created with a secret key
* Keys come in pairs - a private and public key
* The public key is the bank account number - the secret key is the PIN
* The keys are rarely seen and are managed by the wallet software
* In a transaction the recipients public key is presented by its digital signature - called a bitcoin address.
* A _bitcoin address_ is generated from and corresponds to a public key
* Not all bitcoin addresses represent public keys - they can represent scripts

> Bitcoin addresses - abstract the recipient of funds

## Public Key Cryptography and Cryptocurrency

> Since the invention of public key cryptography, several suitable mathematical functions, such as prime number exponentiation and elliptic curve multiplication, have been discovered

These mathematical functions are practically irreversible, meaning that they are easy to calculate in one direction and infeasible to calculate in the opposite direction

Bitcoin uses elliptic curve multiplication as the basis for its cryptography

> In bitcoin, we use **public key cryptography** to create a key pair that controls access to bitcoin

* The public key is used to receive funds
* The private key is used to sign transactions and spend funds

The relationship between the private key and public key allows the private key to generate signatures on messages.
The signature can be validated against a public key without revealing the private key.

Spending bitcoin:

* public key and signature is presented
* the signature is different every time - but created from the same private key
* Everyone can verify a transaction is valid with just those 2 items

> In most wallet implementations, the private and public keys are stored together as a key pair for convenience. However, the public key can be calculated from the private key, so storing only the private key is also possible.

## Private and Public Keys

A bitcoin wallets consists of many key pairs.
A private key (k) is a number -> picked at random. From the private key we use elliptical curve multiplication - a one way cryptographic function - to generate a public key (K).
From the public key (K) we use a one way cryptographic function to generate a bitcoin address (A)

Asymmetric cryptography - the digital signature can only be created by someone that knows the private key, anyone with access to the public key and transaction fingerprint can verify it.

The private key is used to spend (and prove ownership) - it must be kept as secret and safe as possible.
It must remain secret at all times - giving control to a third party gives them control over that bitcoin.

> The private key must be backed up and protected from loss - a loss is a loss forever.

A private key can be picked at random - 256 bit.

Creating a bitcoin is essential pick a number from 1 to 2^256.
It is important to have entropy - randomness - to generate a private key.

More precisely a number:

    between 1 and (1.158 * 10^77) - 1

So produce a number from putting a string through `SHA256` hashing function and ensuring is it less than 1.158 * 10^77

I'm going to stop the notes here, as I have found a book that is a few less pages and will let me maybe get to my goal of learning the fudnementals faster [grokking bitcoin](https://www.manning.com/books/grokking-bitcoin)


## Source

* [Mastering Bitcoin - Andreas M. Antonopoulos](https://aantonop.com/)
