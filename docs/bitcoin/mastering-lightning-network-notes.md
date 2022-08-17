---
author: ''
category: Bitcoin
date: '2022-02-08'
summary: ''
title: Mastering Lightning Network Notes
---
# Mastering Lightning Network Notes

## Preface

The lightning network is a second layer perr-to-peer network allowing for bitcoin payments "off chain".
The Lightning network gives cheaper, faster and more private payments.

The lightning network was proposed in 2015 by “The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments” by Joseph Poon and Thaddeus Dryja.
In 2017 the test Lightning Network was running.
In 2018 the Lightning Network went live.

## 1. Introduction

### Lightning Network Basics

* Blockchain - A cryptographically verified link of blocks - an open distributed as a ledger. Where each block refers to the previous block. Each block also contains transactions and metadata about the block. The lightning network is not a blockchain and does not produce one - it merely uses the bitcoin blockchain.
* Digital signature - A non-repudable proof of ownership (via mathematics) and authenticity of digitally created data. It is the proof of ownership and that it was not altered in transit.
* Hash function - one-way algorithm mapping data of a variable size into a fixed size.
* Node - A computer that participates in a network.
* On-chain - a transaction that has been included in the transactions in the bitcoin blockchain
* Off-chain - second layer transactions that are not recorded in the bitcoin blockchain.
* Transaction - a datastructure recording the transfer of control of funds.

### Trust in decentralised Networks

Trustless is the abiltiy to operate without requiring the trust of a third party.
You are not forced to trust anyone - although you are free to choose to trust a third party.
Fiat - force you to trust - you cannot verify.

> If the bank violates your trust, you may be able to find some recourse from a regulator or court, but at an enormous cost of time, money, and effort.

The system prevents cheating - so you can transact with people you don't trust.

### Fairness without Central Authority

Ensuring fair outcomes:

* Require trust - only deal with people that have proven trust
* Rule of law - Rules inforced by an institution by force
* Trusted 3rd parties - Put an intermediary to enforce trust
* Game theory - Internet and cryptography

Bitcoin prevents unfair outcomes by using a system of incentives and disincentives
Trust the protocol - the set of rules.

Splitting a plate of chips.
One sibling splits - the other chooses.
Naturally inventive to divide it equally - only the cheater will lose.

The rules must be that splitting happens before the choosing.
Commitment without repudiation - splitter and chooser must commit to their roles.

### Proof of Work

Forcing miners to do work - with electricity - incentivises them to not cheat.
As their block would be rejected if they do and they would not get a reward.

The fairness protocol also exists in the lightning network:

* Channel funders have the refund transaction signed before publishing the funding transaction
* When a channel is moved to a new state, the old state is revoked - anyone trying to broadcast it loses the entire balance.
* Commiters of funds know that can get a refund

### Motivating for the Lightning Network

Bitcoin records every transaction in a node - generating a lot of data that is difficult to scale.
A block can only hold a certain number of tranactions (1MB) and are created every 10 minutes.
More competition for getting your transaction in - increases transaction fees.
Increasing the block size or frequency of blocks - will affect abiltiy for regular people to run nodes.
More networking bandwidth required.

> Simply put: you can’t scale a blockchain to validate the entire world’s transactions in a decentralized way

Lightning allows for offchain bitcoin transactions.
Only the intial loading and final settlement transactions needing to be validated on bitcoin nodes.

Lightning Network are cheaper for users because they do not need to pay blockchain fees, and more private for users because they are not published to all participants of the network and furthermore are not stored permanently.

### Lightning Network Defining Features

* Route payments to each other for low cost and in real time
* Do not need to wait for confirmation
* Payments cannot be reversed - can only be refunded by the recipient
* Routed payments are only visible to those nodes
* Lightning transactions do not need to be held permanently
* The lightning network uses Onion routing
* Lightning uses the Bitcoin network

### Use Cases

* Consumer - buying coffee
* Merchant - accept bitcoin payments instantly
* Software services business - Sells lightning and bitcon info and provides liquidity renting inbound channel capacity
* Gamer - selling virtual items for bitcoin on lightning

## 2. Getting Started

Choosing software.

Alice chooses the mobile Eclair wallet - an open source non-custodial wallet.

[List of lightning wallets](https://lightningwiki.net/index.php/Wallets#List)

Open source, self-custody and work on linux:

* [Zap Wallet](https://docs.zaphq.io/)
* [Lightning Labs app](https://github.com/lightninglabs/lightning-app) - Not in dev
* [Fulmo](https://github.com/marzig76/fulmo) - Not updated in a while
* [Spark wallet](https://github.com/shesek/spark-wallet) - Beta
* [Sparko](https://github.com/fiatjaf/sparko)

Work on MacOS:

* [lnd-gui](https://github.com/alexbosworth/lnd-gui) - Not in dev
* [Blue wallet](https://github.com/bluewallet/bluewallet)

### Lightning Nodes

Attributes:

* wallets
* peer-to-peer network
* access to the bitcoin blockchain

> Lightning nodes can also use a lightweight Bitcoin client, commonly referred to as simplified payment verification (SPV)

### Lightning Explorers

* [1ML Lightning explorer](https://1ml.com/)
* [Visualised lightning nodes](https://explorer.acinq.co/)
* [HashXP](https://hashxp.org/)

> As always the truly rely on data you must run your own node

### Lightning Wallets

A wallet can contain any of the following components:

* A keystore - holding private keys
* A LN node communicating with the peer-to-peer network
* A bitcoin node
* A database map of channels announced on lightning
* A channel manager to open and close
* close-up system that can find a path from source to destination

- custodial wallet - Any wallet that outsources management of keys. A third party acting as custodian has control of the user’s funds, not the user.
- A noncustodial or self-custody wallet - is one where the keystore is part of the wallet, and keys are controlled directly by the user.

> Only if a lightning wallet is using its own LN node - does the option of using a full node or a third party node exist.

Bitcoin wallets android based [`Neutrino`](https://neutrino.cash/) and [`Electrum`](https://electrum.org/#documentation) do not operate a full node and rely on someone elses.
[`Bitcoin core`](https://bitcoin.org/en/bitcoin-core/) and [`btcd`](https://github.com/btcsuite/btcd) are full node implementations.

Always test using `testnet` not `mainnet`

Some wallets allow using `testnet`

You can get testnet BTC _tBTC_ from a faucet - search online

### Tradeoff Complexity and Control

Those that give the most control have the highest privacy, most independence and are the most complex to operate.

Some wallets rely on a _hub node_ to remove the burden of channel management - but at the expense of privacy and robustness. It introduces a single point of failure.

> Be careful downloading a wallet - there are many fakes out there.

### Creating a New Wallet

Eclair is a non-custodial wallet - Alice has full custody of the keys to control her bitcoin.
Alice is responsible for protecting and backing up the keys

> If you lose the keys you lose the bitcoin

Mnemonic words - the seed phrase 24 words (BIP39) not implemented by bitcoin core.
The phrase can be used to backup and store the wallet.

It is recommended to write down the phrase (numbered) twice. 
Store it in a locked desk drawer or fireproof safe.

> Never attempt a “DIY” security scheme that deviates in any way from the best practice recommendation in “Storing the Mnemonic Safely”. Do not cut your mnemonic in half, make screenshots, store it on USB drives or cloud drives, encrypt it, or try any other nonstandard method

### Acquiring Bitcoin

* Exchange for Fiat on a bitcoin exchange
* Buy from a friend of acquintance
* Use a bitcoin ATM
* Sell a product or service fot BTC
* Ask employer or clients to pay her in BTC

With a bitcoin ATM you put in fiat bills and then present a qr code of your bitcoin address.
The Eclair wallet will receive the transaction in a few seconds but you should wait for 6 confirmations (1 hour).

To receive money she could:

* Send an email with the bitcoin address
* Send the QR code to the client
* Print the QR code on a piece of paper

So far Eclair has only been a Bitcoin wallet.

### Lightning Channels

* A channel is a financial relationship.
The channel a wallet open a channel with is called a _channel peer_

Not all channel peers are _good_. Well connected peers can route payments over shorter paths - increasing the chance of success. Some channels cannot handle large payments.

A direct channel can be opened.

Open a new channel:

* Paste node uri
* Scan node uri
* Random node
* ACINQ node

> Choosing ACINQ is reliable but lacks privacy and introduces a single point of failure

How much she wants to allocate is added.
A transaction fee is required to open a channel.

When she clicks open - a lightning channel funding transaction is created.
It is on-chain and sent to bitcoin network for confirmation.
She must wait for 6 confirmations.

### Buying a Cup of Coffee with the Lightning Network

It takes a bit of time to get to this point.
It is faster than opening a bank account and getting a card though.

Bob uses BTCPayServer as the point of sale system.

BTCPayServer contains:

* A bitcoin node on bitcoin-core
* A lightning node using c-lightning
* A simple POS applciation for a tablet

On the counter is a tablet with all the products.

Alice selects the option and is presented with a lightning invoice (a payment request) - a QR code and an amount to pay.

Alice opens her app and selects "Send".
Alice selects "Scan a payment request" and is prompted to confirm her payment.
She gets prompted for the payment accepts and sends the money to bob.

Lightning payments are received instantly without having to wait for an onchain confirmation.

## 3. How the Lightning Network Works

> The Lightning Network is a peer-to-peer network of payment channels implemented as smart contracts on the Bitcoin blockchain as well as a communication protocol that defines how participants set up and execute these smart contracts.

### Payment Channel

* A financial relationship between 2 nodes on the lightning network - channel partners.
* The financial relationship allocates a balance of funds in millisatoshis between 2 channel partners.
* A cryptographic protocol prevents one channel partner cheating the other.
* A _2-of-2 multisignature address_ prevents a channel partner from spending the funds unilaterlly.

### Payment Channel Basics

The core is a _2-of-2 multisignature address on the Bitcoin blockchain_ for which you hold a key adn your partner holds a key.

You and your channel partner neogtiate a sequence of transactions.
The latest transaction in the sequence records the balance of the channel - defining how the balance is divided.

The sequence uses bitcoin's scripting language - therefore a _bitcoin smart contract_

> The ability to hold a partially signed transaction, offline and unpublished, with the option to publish and own that balance at any time, is the basis of the Lightning Network.

### Routing Payments across Channels

If there is a route in the network then a payment can be made.

All the trust needed to operate lightning comes from the trust in the decentralised bitcoin network.

* Communication protocol - peers to exchange lightning messages to transfer bitcoin - how messages and encrypted and sent.
* Gossip protocol - Distribute public information about channels to participants.

Lightning network is just an application on top of bitcoin - there is no lightning blockchain or lightning coin.

### Payment Channels

A channel is limited by:

* The time it takes for the internet to transfer a few hundred bytes of data to move funds between channels
* The capacity of the channel - the amount of bitcoin commited
* Number of incomplete payments at a time in the channel

Useful properties:

* Speed of a transaction is limited by the speed of the internet - instant
* Once open - no more interaction is required
* Little or no trust needed between you and your channel partner
* Payments made in the channel are only known by the channel - gaining privacy - only the balance is on bitcoin blockchain

There are 3 types of channels:

* Poon-dryja channels
* Duplex micropayment channels
* Eltoo channels

#### 2-of-2 Multisignature Addresses

Bitcoin is locked to require 2 signatures to unlock it.

#### Funding Transaction

One of the channel partners funds the channel by sending bitconi to the multisignature address.
It won't be obvious it is a lightning channel unless it is closed or announced.

> Channels are typically publicly announced by routing nodes that wish to forward payments

Channel capacity - amount deposited.

> Lightning channel funds are more liquid than funds on the Bitcoin blockchain, as they can be spent faster, cheaper, and more privately

There are some disadvantages to moving funds into the Lightning Network (such as the need to keep them in a “hot” wallet)

#### Poor Channel Opening Procedure

What if the channel partner refuses to sign the transaction, are the funds locked forever?

1. They construt a multi-sig address through public key exchange
2. Alice sends some mBTC into the address
3. If Alice just broadcasts the transaction - she has to trust that Bob will sign
4. To prevent this Alice must create an additional transaction that spends from the multisig address - refunding her mBTC.
5. Alice has Bob sign the refund transaction before broadcasting her funding transaction to the Bitcoin network.
6. This way Alice can get the refund even if Bob fails to cooperate.

The refund transaction is the first of a _commitment transaction_

#### Commitment Transaction

Commitment transactions allow participants to get their funds.
Each participant can always get their funds - so no trust is required.

More often commitment transactions split the funds of the payment channel.
As funds flow now commitment transactions are signed.

Opening a channel:

1. Alice creates a `open_channel` message in the LN protocol
2. Bob creates a new agrees to accept with a `accept_channel`
3. Alice creates a funding transactions to the multisig address with a locking script: `2 <PubKey Alice> <PubKey Bob> 2 CHECKMULTISIG`
4. Alice does not broadcast yet but sends the transaction ID in a `funding_created` message.
5. Both Alice and Bob create versions of teh funding transaction - to spend the bitcoin back to Alice
6. They both create the same transaction but need to exchange signatures
7. Bob provides the signature and sends a `funding_signed`
8. Now alice broadcasts the funding message to the network

If Bob stops responding to Alice - her only costs will be the fees for the onchain transaction.

Commitment transactions are created each time the channel balance changes.

> Commitment transactions are the means by whih a payment is sent across a channel.

#### Cheating

Nothing is stopping Alice from broadbasting a prior commitment transaction.
A mechanism is needed to stop Alice from publishing a prior commitment transaction.
Commitment transaction are constructed in a way that if the other party cheats - they can be punished.
By making the penalty large enough there is a strong incentive against cheating.

The cheater loses everything.
If Alice drains her balance - she could try cheating with little risk.
To prevent this Lightning requires to keep a minimum balance in the channel.

Channel contruction with penalty:

1. Alice creates a channel with Bob and puts 100k satoshis into it
2. Alice sends 30k satoshis to Bob
3. Alice tries to cheat Bob by publishing an old commitment transaction claiming the 100k satoshis
4. Bob detects the fraud and punishes Alice by taking the 100k himself
5. Bob ends up with 100K - gaining 70k for catching Alice cheating
6. Alice ends up with 0 satoshis

A commitment transaction has 2 outputs - paying each channel partner.
We change this to add a _timelock delay_ and _revocation secret_

* timelock delay - prevents the owner of the output from spending it immediately
* recovation secret - allows either party to immediately spend that payment - bypassing the timelock

> Bob holds a commitment transaction that pays Alice immediately, but his own payment is delayed and revocable. Alice also holds a commitment transaction, but hers is the opposite: it pays Bob immediately but her own payment is delayed and revocable.

> The two channel partners hold half of the revocation secret, so that neither one knows the whole secret. If they share their half, then the other channel partner has the full secret and can use it to exercise the revocation condition.

> In simple terms, Alice signs Bob’s new commitment transaction only if Bob offers his half of the revocation secret for the previous commitment. Bob only signs Alice’s new commitment transaction if she gives him her half of the revocation secret from the previous commitment.

> With each new commitment, they exchange the necessary “punishment” secret that allows them to effectively revoke the prior commitment transaction by making it unprofitable to transmit.

Essentially, they destroy the ability to use old commitments as they sign the new ones

> The timelock is set to a number of blocks up to 2,016 (approximately two weeks).

> If either channel partner publishes a commitment transaction without cooperating with the other partner, they will have to wait for that number of blocks (e.g., two weeks) to claim their balance.

> Furthermore, if the commitment they published was previously revoked, the channel partner can also immediately claim the cheating party’s balance, bypassing the timelock and punishing the cheater.

The timelock is adjustable - shorter for smaller channels.

For every new update of the channel balance, new commitment transactions and new revocation secrets have to be created and saved

As long as a channel remains open, all revocation secrets ever created for the channel need to be kept because they might be needed in the future.

Due to a smart derivation mechanism used to derive revocation secrets, we only need to store the most recent secret

> Nevertheless, managing and storing the revocation secrets is one of the more elaborate parts of Lightning nodes that require node operators to maintain backups.

Note: Technologies such as watchtower services or changing the channel construction protocol to the eltoo protocol might be future strategies to mitigate these issues and reduce the need for revocation secrets, penalty transactions, and channel backups.

Alice can close the channel at any time if Bob does not respond, claiming her fair share of the balance. After publishing the last commitment transaction on-chain, Alice has to wait for the timelock to expire before she can spend her funds from the commitment transaction.

Easier way to close a channel is to close with the correct balance allocation.

#### Announcing the channel

Channels partners can announce to the entire lightning network - making it a public channel.
The lightning network uses the gossip channel to tell other nodes about existence of channels, capacity and fees.

Public channels allows payment routing and routing fees.

By contrast a channel can be unannounced.
The existance of an unannounced channel will be known at final settlement.
That is why it is not called `private`.

Accounced channels by the gossip protocol will expose the routing fees and timelock duration.

New nodes get gossip announcements and build a map - the routing between nodes.

BGP?

#### Closing the Channel

The best way to close a channel is to not close it.
The channel can always be rebalanced - if balance is low in one direction.

When is closing a channel desirable:

* Reduce your balance on lightning and move funds to cold storage
* Your channel partner becomes unresponsive
* Your channel is not being used often and there are other opportunities
* Your channel partner has breached the protocol

3 ways to close a payment channel:

* Mutual close (the good way)
* Force close (the bad way)
* Protocol breach (the ugly way)

##### Mutual Close

You inform channel partner of wanting to close.
No new routing attempts are accepted, ongoing routing are settled or removed.
A closing transaction is made - closing transactions do not have a timelock.

The on-chain transaction fees are paid by the partner that opened the channel.
Channel partners agree on the fee and sign the closing transaction.
Once broadcast and confirmed to the bitcoin network. The channel is then closed.

##### Force Close

Closing without the other channel partner's consent.

To initiate a force close, you can simply publish the last commitment transaction your node has.
It will be confirmed on the bitcoin network and create 2 spendable outputs.
The bitcoin network does not know if this is the most recent commitment transaction or an old one.
THe partner initiated the force close will have their funds in a timelock - whereas the other partner can spend immediately.
The timelock delay - gives time for the partner to dispute the transaction with the revocation secret - but only before the timelock delay expires.

The on-chain fees will be higher than a mutual transaction:

1. when the commitment transaction is negotiated the partners dont know the required fees in the future - the commitment transaction fee is more generous. It cna be upto 5 times higher than that suggested by the estimator.
2. The commitment transaction contains additional timelocks for pending routing attempts, Hash time locked contracts (HTLC), making the commitment transaction larger in bytes - therefore larger in fees.
3. Any pending routing attempts must happen on chain.

HTLC - Hash time locked contracts - payments routed across lightning instead of direct channel payments.

Sometimes it is best to contact the person - or open channels with reliable people.

##### Protocol Breach

A dishonest force close - previous commitment transaction.
Your node must be watching new blocks and transactions to detect it.

If your bitcoin node has been corrupted - a problem.

If detected you publish a punishment transaction before the timelock expires.
You receive all the funds.

You will have to pay the onchain transaction fees - honos is on you to detect - if you fail to detect your funds are forfeit.

Game theory makes it infeasible to cheat.
Watchtowers becoming widely available can counteract it.

You need a bitcoin full node and watchtower or lightning node to find corresponding channels.
Timeout period maximum is 2016 blocks  - 14 days.

### Invoices

Most payments start with an invoice.
An invoice has a payment hash (payment identifier)
Allows for an atomic tranasction - either successful or not at all. No state in between.

Invoices are communicated out-of-band.
QR code, email or any message.

Invoices are usually a bech32-encoded string.
The amount requested and the signature of the recipient.

The sender uses the signature to extract the public key (node ID) of the recipient so the payer knows where to send the transaction.

Bitcoin is based on an address - in lightning is based on an invoice.
In bitcoin we create a transaction - in lightning we send a payment.

#### Payment Hash and Pre-Image

The most important part of the invoice is the _payment hash_.

1. Bob chooses a random number - the _preimage secret_
2. Bob uses SHA256 to calcuate the Hash of R

#### Additional Metadata

Invoices can optionally have additional data.
Some incoices also have routing hints to unannounced channels or public channels.
Invoices optionally include a bitcoin address as a fallback.

> If you have to incur on-chain fees to make a payment, you might as well incur those fees to open a channel and make the payment over Lightning.

> Lightning invoices contain an expiry date. Since the recipient must keep the preimage r for every invoice issued, it is useful to have invoices expire so that these preimages do not need to be kept forever. Once an invoice expires or is paid, the recipient can discard the preimage.

### Delivering the Payment

#### Peer-to-peer Gossip Protocol

Channel announcements made over the gossip protocol.
Nodes are peers.

Uses a `channel_announcement` message.
Annoucements about known nodes: `node_announcement`.

Nodes changing metadata: `channel_update`.

The precise topology and channel balance is not shared to:

* protect privacy
* to scale payments
* dynamic system - info is only valid for a short amount of time

#### Pathfinding and Routing

Pathfinding - getting a route between source and destination
Routing - using the path

Lightning uses a source based path for pathfinding and a onion-routed protocol for payments.

#### Source based pathfinding

If we knew the exact channel balance - we could use a standard computer science class pathfinding algorithm.
However balance information of all channels is imperfect.
Pathfinding is a major criticism - as it is not solved.

Pathfinding is equivalent to the NP-complete travelling salesman problem.

Iteratively try paths until one is found with enough liquidity.
It does not returna path with the lowest fees.

Unlike the internet protocol lightning transactions are atomic and channel balances must remain private.
Channel capacity changes frequently on lightning but rarely on the internet.

#### Onion Routing

Similar to the Tor onion router.
It uses the SPHINX Mix format.
On the route from payer to payee - the payer constructs an onion.
The payment is created for the final recipient and is encrypted - so only the payee can decrypt.
Then the payer wraps that layer in instructions for the node preceding the final recipient.
The sender gives the onion to the first node.
Each node peels off layers until the next node.
Padding is added at each node - to keep the onion the same size.


* An intermediary node can only see the channel it received and where it must forward an onion
* The onions are small enough to fit into a TCP/IP packet and even a link layer (eg. Ethernet) frame - traffic analysis made harder.
* The onions will always have the same length independent of their position in the chain
* Onions have an HMAC (Hash-based Message Authentication Code) - manipulation made impossible
* Onions can have up to 26 layers
* Each layers encryption key is ephemeral and not reused
* Errors can be sent back with the same protocol - indisitinguishable from normal onion

#### Payment Forwarding Algorithm

Each intermediary node received a `update_add_htlc` message with a payment hash and onion.

The intermediary node executes a series of steps - the _payment forwarding algorithm_:

1. Node decrypts outer layer and checks message integrity
2. Confirms it can fulfill the routing hints based on channel fees and capacity.
3. Works with channel partner to update state
4. Adds padding to the onion to maintain the size
5. It follows the routing hints to forward to the next channel by sending a `updated_add_htlc`
6. It works with channel partner on outgoing channel to update the channel state.

I find lightning very comple - and prefer to use onchain bitcoin for right now.
There are too many moving parts and it lacks simplicity.

I am 3 chapters in and I still haven't got a lightning client up and running.
This is certainly something to be handled by third parties.

More reading in the book...

## 4. Lightning Node Software

There is no reference implementation (unlike bitcoin)

There is only BOLT (Basis of Lightning Technology) and the [lightning rfc repo](https://github.com/lightning/bolts)

There is no consensus - different projects approach different development features.

### Lightning Development Environment

#### C-lightning: Lightning Node Project

* Developed by blockstream
* [c-lighting repo](https://github.com/ElementsProject/lightning)

Installing c-lightning from source:

[Instructions to install from source](https://github.com/ElementsProject/lightning/blob/master/doc/INSTALL.md)

> You must have bitcoin core installed locally.

    sudo apt-get update
    sudo apt-get install -y \
    autoconf automake build-essential git libtool libgmp-dev libsqlite3-dev \
    python3 python3-mako python3-pip net-tools zlib1g-dev libsodium-dev \
    gettext
    pip3 install --user mrkd mistune==0.8.4

Clone the repo:

    git clone --recurse https://github.com/ElementsProject/lightning
    cd lightning

Configure and compile

    ./configure
    make
    sudo make install

Verify it has been installed:

    lightningd --version
    lightning-cli --version


> I am struggling to get it up and running on ubuntu 20.04 on a raspberry pi. I think I will give it a bit more time before continuing.

Even with [LND - Lightning Network Daemon](https://github.com/lightningnetwork/lnd/) a go based lightning node there is an inclination to use docker.














 





