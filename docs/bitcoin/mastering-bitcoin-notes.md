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




## Source

* [Mastering Bitcoin - Andreas M. Antonopoulos](https://aantonop.com/)