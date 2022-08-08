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
* [Local classified](https://localbitcoins.com/) for cash in area
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

### Setting up a node on Raspberry Pi

I wrote a post on setting up a [bitcoin full node with a raspberry pi on ubuntu 20.04](https://number1.co.za/raspberry-pi-dedicated-bitcoin-node-with-ubuntu-arm-istructions/) - the instuctions may have become outdated and I cannot gaurantee the security or configuration settings.

### Configuring your Node

To disable the reference wallet implementation, in your `~/.bitcoin/bitcoin.conf` file set:

    disablewallet=1

You can check where the binaries are with:

    $ which bitcoind
    /usr/local/bin/bitcoind
    
    $ which bitcoin-cli
    /usr/local/bin/bitcoin-cli

### Running a bitcoin node

Bitcoin's peer to peer network is run by volunteers and businesses.
Those running nodes have a **direct and authoritive view of the bitcoin blockchain** - a local copy of all transactions independently validated by the node.

> By running a node you do not need to rely on a third party to validate a transaction

The bitcoin block chain - all transactions - is about 370GB as of July 2021.

You can run a `testnet` node which is only 17GB as of July 2021 with setting in `bitcoin.conf`:

    testnet=1

Why would you want to run a node:

* developing bitcoin software using local node api
* Support bitcoin - making the network more robust
* If you do not want to rely on a third party to validate transactions

#### Running a node the first time

The first time you run a node it will ask you to create a strong password for `JSON RPC` - the bitcoin api.

    $ bitcoind
    Error: To use the "-server" option, you must set a rpcpassword in the configuration file:
    /home/ubuntu/.bitcoin/bitcoin.conf
    It is recommended you use the following random password:
    rpcuser=bitcoinrpc
    rpcpassword=2XA4DuKNCbtZXsBQRRNDEwEY2nM6M4H

> I think the `rpc` config is deprecated now in favour of something else

#### Configuring the bitcoin code node

You can see config options with:

    $ bitcoind --help
    Bitcoin Core version v0.21.0

    Usage:  bitcoind [options]                     Start Bitcoin Core

    Options:

    -?
        Print this help message and exit

    -alertnotify=<cmd>
        Execute command when a relevant alert is received or we see a really
        long fork (%s in cmd is replaced by message)

    -assumevalid=<hex>
        If this block is in the chain assume that it and its ancestors are valid
        and potentially skip their script verification (0 to verify all,
        default:
        0000000000000000000b9d2ec5a352ecba0592946514a92f14319dc2b367fc72,
        testnet:
        000000000000006433d1efec504c53ca332b64963c425395515b01977bd7b3b0,
        signet:
        0000002a1de0f46379358c1fd09906f7ac59adf3712323ed90eb59e4c183c020)

    -blockfilterindex=<type>
        Maintain an index of compact filters by block (default: 0, values:
        basic). If <type> is not supplied or if <type> = 1, indexes for
        all known types are enabled.

    -blocknotify=<cmd>
        Execute command when the best block changes (%s in cmd is replaced by
        block hash)

    -blockreconstructionextratxn=<n>
        Extra transactions to keep in memory for compact block reconstructions
        (default: 100)

    -blocksdir=<dir>
        Specify directory to hold blocks subdirectory for *.dat files (default:
        <datadir>)

    -blocksonly
        Whether to reject transactions from network peers. Automatic broadcast
        and rebroadcast of any transactions from inbound peers is
        disabled, unless the peer has the 'forcerelay' permission. RPC
        transactions are not affected. (default: 0)

    -conf=<file>
        Specify path to read-only configuration file. Relative paths will be
        prefixed by datadir location. (default: bitcoin.conf)

    -daemon
        Run in the background as a daemon and accept commands

    -datadir=<dir>
        Specify data directory

    -dbcache=<n>
        Maximum database cache size <n> MiB (4 to 16384, default: 450). In
        addition, unused mempool memory is shared for this cache (see
        -maxmempool).

    -debuglogfile=<file>
        Specify location of debug log file. Relative paths will be prefixed by a
        net-specific datadir location. (-nodebuglogfile to disable;
        default: debug.log)

    -includeconf=<file>
        Specify additional configuration file, relative to the -datadir path
        (only useable from configuration file, not command line)

    -loadblock=<file>
        Imports blocks from external file on startup

    -maxmempool=<n>
        Keep the transaction memory pool below <n> megabytes (default: 300)

    -maxorphantx=<n>
        Keep at most <n> unconnectable transactions in memory (default: 100)

    -mempoolexpiry=<n>
        Do not keep transactions in the mempool longer than <n> hours (default:
        336)

    -par=<n>
        Set the number of script verification threads (-4 to 15, 0 = auto, <0 =
        leave that many cores free, default: 0)

    -persistmempool
        Whether to save the mempool on shutdown and load on restart (default: 1)

    -pid=<file>
        Specify pid file. Relative paths will be prefixed by a net-specific
        datadir location. (default: bitcoind.pid)

    -prune=<n>
        Reduce storage requirements by enabling pruning (deleting) of old
        blocks. This allows the pruneblockchain RPC to be called to
        delete specific blocks, and enables automatic pruning of old
        blocks if a target size in MiB is provided. This mode is
        incompatible with -txindex and -rescan. Warning: Reverting this
        setting requires re-downloading the entire blockchain. (default:
        0 = disable pruning blocks, 1 = allow manual pruning via RPC,
        >=550 = automatically prune block files to stay under the
        specified target size in MiB)

    -reindex
        Rebuild chain state and block index from the blk*.dat files on disk

    -reindex-chainstate
        Rebuild chain state from the currently indexed blocks. When in pruning
        mode or if blocks on disk might be corrupted, use full -reindex
        instead.

    -settings=<file>
        Specify path to dynamic settings data file. Can be disabled with
        -nosettings. File is written at runtime and not meant to be
        edited by users (use bitcoin.conf instead for custom settings).
        Relative paths will be prefixed by datadir location. (default:
        settings.json)

    -startupnotify=<cmd>
        Execute command on startup.

    -sysperms
        Create new files with system default permissions, instead of umask 077
        (only effective with disabled wallet functionality)

    -txindex
        Maintain a full transaction index, used by the getrawtransaction rpc
        call (default: 0)

    -version
        Print version and exit

    Connection options:

    -addnode=<ip>
        Add a node to connect to and attempt to keep the connection open (see
        the `addnode` RPC command help for more info). This option can be
        specified multiple times to add multiple nodes.

    -asmap=<file>
        Specify asn mapping used for bucketing of the peers (default:
        ip_asn.map). Relative paths will be prefixed by the net-specific
        datadir location.

    -bantime=<n>
        Default duration (in seconds) of manually configured bans (default:
        86400)

    -bind=<addr>[:<port>][=onion]
        Bind to given address and always listen on it (default: 0.0.0.0). Use
        [host]:port notation for IPv6. Append =onion to tag any incoming
        connections to that address and port as incoming Tor connections
        (default: 127.0.0.1:8334=onion, testnet: 127.0.0.1:18334=onion,
        signet: 127.0.0.1:38334=onion, regtest: 127.0.0.1:18445=onion)

    -connect=<ip>
        Connect only to the specified node; -noconnect disables automatic
        connections (the rules for this peer are the same as for
        -addnode). This option can be specified multiple times to connect
        to multiple nodes.

    -discover
        Discover own IP addresses (default: 1 when listening and no -externalip
        or -proxy)

    -dns
        Allow DNS lookups for -addnode, -seednode and -connect (default: 1)

    -dnsseed
        Query for peer addresses via DNS lookup, if low on addresses (default: 1
        unless -connect used)

    -externalip=<ip>
        Specify your own public address

    -forcednsseed
        Always query for peer addresses via DNS lookup (default: 0)

    -listen
        Accept connections from outside (default: 1 if no -proxy or -connect)

    -listenonion
        Automatically create Tor onion service (default: 1)

    -maxconnections=<n>
        Maintain at most <n> connections to peers (default: 125)

    -maxreceivebuffer=<n>
        Maximum per-connection receive buffer, <n>*1000 bytes (default: 5000)

    -maxsendbuffer=<n>
        Maximum per-connection send buffer, <n>*1000 bytes (default: 1000)

    -maxtimeadjustment
        Maximum allowed median peer time offset adjustment. Local perspective of
        time may be influenced by peers forward or backward by this
        amount. (default: 4200 seconds)

    -maxuploadtarget=<n>
        Tries to keep outbound traffic under the given target (in MiB per 24h).
        Limit does not apply to peers with 'download' permission. 0 = no
        limit (default: 0)

    -networkactive
        Enable all P2P network activity (default: 1). Can be changed by the
        setnetworkactive RPC command

    -onion=<ip:port>
        Use separate SOCKS5 proxy to reach peers via Tor onion services, set
        -noonion to disable (default: -proxy)

    -onlynet=<net>
        Make outgoing connections only through network <net> (ipv4, ipv6 or
        onion). Incoming connections are not affected by this option.
        This option can be specified multiple times to allow multiple
        networks.

    -peerblockfilters
        Serve compact block filters to peers per BIP 157 (default: 0)

    -peerbloomfilters
        Support filtering of blocks and transaction with bloom filters (default:
        0)

    -permitbaremultisig
        Relay non-P2SH multisig (default: 1)

    -port=<port>
        Listen for connections on <port>. Nodes not using the default ports
        (default: 8333, testnet: 18333, signet: 38333, regtest: 18444)
        are unlikely to get incoming connections.

    -proxy=<ip:port>
        Connect through SOCKS5 proxy, set -noproxy to disable (default:
        disabled)

    -proxyrandomize
        Randomize credentials for every proxy connection. This enables Tor
        stream isolation (default: 1)

    -seednode=<ip>
        Connect to a node to retrieve peer addresses, and disconnect. This
        option can be specified multiple times to connect to multiple
        nodes.

    -timeout=<n>
        Specify connection timeout in milliseconds (minimum: 1, default: 5000)

    -torcontrol=<ip>:<port>
        Tor control port to use if onion listening enabled (default:
        127.0.0.1:9051)

    -torpassword=<pass>
        Tor control port password (default: empty)

    -upnp
        Use UPnP to map the listening port (default: 0)

    -whitebind=<[permissions@]addr>
        Bind to the given address and add permission flags to the peers
        connecting to it. Use [host]:port notation for IPv6. Allowed
        permissions: bloomfilter (allow requesting BIP37 filtered blocks
        and transactions), noban (do not ban for misbehavior; implies
        download), forcerelay (relay transactions that are already in the
        mempool; implies relay), relay (relay even in -blocksonly mode,
        and unlimited transaction announcements), mempool (allow
        requesting BIP35 mempool contents), download (allow getheaders
        during IBD, no disconnect after maxuploadtarget limit), addr
        (responses to GETADDR avoid hitting the cache and contain random
        records with the most up-to-date info). Specify multiple
        permissions separated by commas (default:
        download,noban,mempool,relay). Can be specified multiple times.

    -whitelist=<[permissions@]IP address or network>
        Add permission flags to the peers connecting from the given IP address
        (e.g. 1.2.3.4) or CIDR-notated network (e.g. 1.2.3.0/24). Uses
        the same permissions as -whitebind. Can be specified multiple
        times.

    Wallet options:

    -addresstype
        What type of addresses to use ("legacy", "p2sh-segwit", or "bech32",
        default: "bech32")

    -avoidpartialspends
        Group outputs by address, selecting all or none, instead of selecting on
        a per-output basis. Privacy is improved as an address is only
        used once (unless someone sends to it after spending from it),
        but may result in slightly higher fees as suboptimal coin
        selection may result due to the added limitation (default: 0
        (always enabled for wallets with "avoid_reuse" enabled))

    -changetype
        What type of change to use ("legacy", "p2sh-segwit", or "bech32").
        Default is same as -addresstype, except when
        -addresstype=p2sh-segwit a native segwit output is used when
        sending to a native segwit address)

    -disablewallet
        Do not load the wallet and disable wallet RPC calls

    -discardfee=<amt>
        The fee rate (in BTC/kB) that indicates your tolerance for discarding
        change by adding it to the fee (default: 0.0001). Note: An output
        is discarded if it is dust at this rate, but we will always
        discard up to the dust relay fee and a discard fee above that is
        limited by the fee estimate for the longest target

    -fallbackfee=<amt>
        A fee rate (in BTC/kB) that will be used when fee estimation has
        insufficient data. 0 to entirely disable the fallbackfee feature.
        (default: 0.00)

    -keypool=<n>
        Set key pool size to <n> (default: 1000). Warning: Smaller sizes may
        increase the risk of losing funds when restoring from an old
        backup, if none of the addresses in the original keypool have
        been used.

    -maxapsfee=<n>
        Spend up to this amount in additional (absolute) fees (in BTC) if it
        allows the use of partial spend avoidance (default: 0.00)

    -mintxfee=<amt>
        Fees (in BTC/kB) smaller than this are considered zero fee for
        transaction creation (default: 0.00001)

    -paytxfee=<amt>
        Fee (in BTC/kB) to add to transactions you send (default: 0.00)

    -rescan
        Rescan the block chain for missing wallet transactions on startup

    -spendzeroconfchange
        Spend unconfirmed change when sending transactions (default: 1)

    -txconfirmtarget=<n>
        If paytxfee is not set, include enough fee so transactions begin
        confirmation on average within n blocks (default: 6)

    -wallet=<path>
        Specify wallet path to load at startup. Can be used multiple times to
        load multiple wallets. Path is to a directory containing wallet
        data and log files. If the path is not absolute, it is
        interpreted relative to <walletdir>. This only loads existing
        wallets and does not create new ones. For backwards compatibility
        this also accepts names of existing top-level data files in
        <walletdir>.

    -walletbroadcast
        Make the wallet broadcast transactions (default: 1)

    -walletdir=<dir>
        Specify directory to hold wallets (default: <datadir>/wallets if it
        exists, otherwise <datadir>)

    -walletnotify=<cmd>
        Execute command when a wallet transaction changes. %s in cmd is replaced
        by TxID and %w is replaced by wallet name. %w is not currently
        implemented on windows. On systems where %w is supported, it
        should NOT be quoted because this would break shell escaping used
        to invoke the command.

    -walletrbf
        Send transactions with full-RBF opt-in enabled (RPC only, default: 0)

    ZeroMQ notification options:

    -zmqpubhashblock=<address>
        Enable publish hash block in <address>

    -zmqpubhashblockhwm=<n>
        Set publish hash block outbound message high water mark (default: 1000)

    -zmqpubhashtx=<address>
        Enable publish hash transaction in <address>

    -zmqpubhashtxhwm=<n>
        Set publish hash transaction outbound message high water mark (default:
        1000)

    -zmqpubrawblock=<address>
        Enable publish raw block in <address>

    -zmqpubrawblockhwm=<n>
        Set publish raw block outbound message high water mark (default: 1000)

    -zmqpubrawtx=<address>
        Enable publish raw transaction in <address>

    -zmqpubrawtxhwm=<n>
        Set publish raw transaction outbound message high water mark (default:
        1000)

    -zmqpubsequence=<address>
        Enable publish hash block and tx sequence in <address>

    -zmqpubsequencehwm=<n>
        Set publish hash sequence message high water mark (default: 1000)

    Debugging/Testing options:

    -debug=<category>
        Output debugging information (default: -nodebug, supplying <category> is
        optional). If <category> is not supplied or if <category> = 1,
        output all debugging information. <category> can be: net, tor,
        mempool, http, bench, zmq, walletdb, rpc, estimatefee, addrman,
        selectcoins, reindex, cmpctblock, rand, prune, proxy, mempoolrej,
        libevent, coindb, qt, leveldb, validation.

    -debugexclude=<category>
        Exclude debugging information for a category. Can be used in conjunction
        with -debug=1 to output debug logs for all categories except one
        or more specified categories.

    -help-debug
        Print help message with debugging options and exit

    -logips
        Include IP addresses in debug output (default: 0)

    -logtimestamps
        Prepend debug output with timestamp (default: 1)

    -maxtxfee=<amt>
        Maximum total fees (in BTC) to use in a single wallet transaction;
        setting this too low may abort large transactions (default: 0.10)

    -printtoconsole
        Send trace/debug info to console (default: 1 when no -daemon. To disable
        logging to file, set -nodebuglogfile)

    -shrinkdebugfile
        Shrink debug.log file on client startup (default: 1 when no -debug)

    -uacomment=<cmt>
        Append comment to the user agent string

    Chain selection options:

    -chain=<chain>
        Use the chain <chain> (default: main). Allowed values: main, test,
        signet, regtest

    -signet
        Use the signet chain. Equivalent to -chain=signet. Note that the network
        is defined by the -signetchallenge parameter

    -signetchallenge
        Blocks must satisfy the given script to be considered valid (only for
        signet networks; defaults to the global default signet test
        network challenge)

    -signetseednode
        Specify a seed node for the signet network, in the hostname[:port]
        format, e.g. sig.net:1234 (may be used multiple times to specify
        multiple seed nodes; defaults to the global default signet test
        network seed node(s))

    -testnet
        Use the test chain. Equivalent to -chain=test.

    Node relay options:

    -bytespersigop
        Equivalent bytes per sigop in transactions for relay and mining
        (default: 20)

    -datacarrier
        Relay and mine data carrier transactions (default: 1)

    -datacarriersize
        Maximum size of data in data carrier transactions we relay and mine
        (default: 83)

    -minrelaytxfee=<amt>
        Fees (in BTC/kB) smaller than this are considered zero fee for relaying,
        mining and transaction creation (default: 0.00001)

    -whitelistforcerelay
        Add 'forcerelay' permission to whitelisted inbound peers with default
        permissions. This will relay transactions even if the
        transactions were already in the mempool. (default: 0)

    -whitelistrelay
        Add 'relay' permission to whitelisted inbound peers with default
        permissions. This will accept relayed transactions even when not
        relaying transactions (default: 1)

    Block creation options:

    -blockmaxweight=<n>
        Set maximum BIP141 block weight (default: 3996000)

    -blockmintxfee=<amt>
        Set lowest fee rate (in BTC/kB) for transactions to be included in block
        creation. (default: 0.00001)

    RPC server options:

    -rest
        Accept public REST requests (default: 0)

    -rpcallowip=<ip>
        Allow JSON-RPC connections from specified source. Valid for <ip> are a
        single IP (e.g. 1.2.3.4), a network/netmask (e.g.
        1.2.3.4/255.255.255.0) or a network/CIDR (e.g. 1.2.3.4/24). This
        option can be specified multiple times

    -rpcauth=<userpw>
        Username and HMAC-SHA-256 hashed password for JSON-RPC connections. The
        field <userpw> comes in the format: <USERNAME>:<SALT>$<HASH>. A
        canonical python script is included in share/rpcauth. The client
        then connects normally using the
        rpcuser=<USERNAME>/rpcpassword=<PASSWORD> pair of arguments. This
        option can be specified multiple times

    -rpcbind=<addr>[:port]
        Bind to given address to listen for JSON-RPC connections. Do not expose
        the RPC server to untrusted networks such as the public internet!
        This option is ignored unless -rpcallowip is also passed. Port is
        optional and overrides -rpcport. Use [host]:port notation for
        IPv6. This option can be specified multiple times (default:
        127.0.0.1 and ::1 i.e., localhost)

    -rpccookiefile=<loc>
        Location of the auth cookie. Relative paths will be prefixed by a
        net-specific datadir location. (default: data dir)

    -rpcpassword=<pw>
        Password for JSON-RPC connections

    -rpcport=<port>
        Listen for JSON-RPC connections on <port> (default: 8332, testnet:
        18332, signet: 38332, regtest: 18443)

    -rpcserialversion
        Sets the serialization of raw transaction or block hex returned in
        non-verbose mode, non-segwit(0) or segwit(1) (default: 1)

    -rpcthreads=<n>
        Set the number of threads to service RPC calls (default: 4)

    -rpcuser=<user>
        Username for JSON-RPC connections

    -rpcwhitelist=<whitelist>
        Set a whitelist to filter incoming RPC calls for a specific user. The
        field <whitelist> comes in the format: <USERNAME>:<rpc 1>,<rpc
        2>,...,<rpc n>. If multiple whitelists are set for a given user,
        they are set-intersected. See -rpcwhitelistdefault documentation
        for information on default whitelist behavior.

    -rpcwhitelistdefault
        Sets default behavior for rpc whitelisting. Unless rpcwhitelistdefault
        is set to 0, if any -rpcwhitelist is set, the rpc server acts as
        if all rpc users are subject to empty-unless-otherwise-specified
        whitelists. If rpcwhitelistdefault is set to 1 and no
        -rpcwhitelist is set, rpc server acts as if all rpc users are
        subject to empty whitelists.

    -server
        Accept command line and JSON-RPC commands

You can also set options in you `bitcoin.conf` file:

* `alertnotify` - run a script to alert node owner of events
* `conf` - alternate lcoation of config file
* `datadir` - directory for bitcoin data
* `maxconnections` - set max number of connections to prevent excess data use
* `maxmempool` - maximum amount of memory for the node to use
* `minrelaytxfee` - minimum fee transaction you will relay. Used to reduce the size of the in memory transaction pool.
* 

Transaction database options:

By default bitcoin core builds a database of transactions only relating to the user's wallet

If you want to use `getrawtransaction` you need to build a complete transaction index:

    txindex=1

> You then need to restart `bitcoind` with the `reindex` option to rebuild the index

On a dedicated raspberry pi with 8GB you might want to set with a constained internet:

    maxmempool=3000
    maxconnections=20
    minrelaytxfee=0.0001
    
To run the daemon with messages in the foreground:

    bitcoind -printtoconsole

To monitor info of your node:

    bitcoin-cli getinfo

    bitcoin-cli -getinfo
    {
    "version": 210000,
    "blocks": 94967,
    "headers": 236557,
    "verificationprogress": 0.0003050917592975576,
    "timeoffset": -1,
    "connections": {
        "in": 11,
        "out": 10,
        "total": 21
    },
    "proxy": "",
    "difficulty": 8078.195257925088,
    "chain": "main",
    "keypoolsize": 1000,
    "paytxfee": 0.00000000,
    "balance": 0.00000000,
    "relayfee": 0.00001000,
    "warnings": ""
    }

### Bitcoin Core API

Bitcoin core implements a json RPC (remote procedure call) interface.
It can be accessed with `bitcoin-cli`

To get available options use:

    ubuntu@btc:~$ bitcoin-cli help
    == Blockchain ==
    getbestblockhash
    getblock "blockhash" ( verbosity )
    getblockchaininfo
    getblockcount
    getblockfilter "blockhash" ( "filtertype" )
    getblockhash height
    getblockheader "blockhash" ( verbose )
    getblockstats hash_or_height ( stats )
    getchaintips
    getchaintxstats ( nblocks "blockhash" )
    getdifficulty
    getmempoolancestors "txid" ( verbose )
    getmempooldescendants "txid" ( verbose )
    getmempoolentry "txid"
    getmempoolinfo
    getrawmempool ( verbose mempool_sequence )
    gettxout "txid" n ( include_mempool )
    gettxoutproof ["txid",...] ( "blockhash" )
    gettxoutsetinfo ( "hash_type" )
    preciousblock "blockhash"
    pruneblockchain height
    savemempool
    scantxoutset "action" ( [scanobjects,...] )
    verifychain ( checklevel nblocks )
    verifytxoutproof "proof"

    == Control ==
    getmemoryinfo ( "mode" )
    getrpcinfo
    help ( "command" )
    logging ( ["include_category",...] ["exclude_category",...] )
    stop
    uptime

    == Generating ==
    generateblock "output" ["rawtx/txid",...]
    generatetoaddress nblocks "address" ( maxtries )
    generatetodescriptor num_blocks "descriptor" ( maxtries )

    == Mining ==
    getblocktemplate ( "template_request" )
    getmininginfo
    getnetworkhashps ( nblocks height )
    prioritisetransaction "txid" ( dummy ) fee_delta
    submitblock "hexdata" ( "dummy" )
    submitheader "hexdata"

    == Network ==
    addnode "node" "command"
    clearbanned
    disconnectnode ( "address" nodeid )
    getaddednodeinfo ( "node" )
    getconnectioncount
    getnettotals
    getnetworkinfo
    getnodeaddresses ( count )
    getpeerinfo
    listbanned
    ping
    setban "subnet" "command" ( bantime absolute )
    setnetworkactive state

    == Rawtransactions ==
    analyzepsbt "psbt"
    combinepsbt ["psbt",...]
    combinerawtransaction ["hexstring",...]
    converttopsbt "hexstring" ( permitsigdata iswitness )
    createpsbt [{"txid":"hex","vout":n,"sequence":n},...] [{"address":amount},{"data":"hex"},...] ( locktime replaceable )
    createrawtransaction [{"txid":"hex","vout":n,"sequence":n},...] [{"address":amount},{"data":"hex"},...] ( locktime replaceable )
    decodepsbt "psbt"
    decoderawtransaction "hexstring" ( iswitness )
    decodescript "hexstring"
    finalizepsbt "psbt" ( extract )
    fundrawtransaction "hexstring" ( options iswitness )
    getrawtransaction "txid" ( verbose "blockhash" )
    joinpsbts ["psbt",...]
    sendrawtransaction "hexstring" ( maxfeerate )
    signrawtransactionwithkey "hexstring" ["privatekey",...] ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )
    testmempoolaccept ["rawtx",...] ( maxfeerate )
    utxoupdatepsbt "psbt" ( ["",{"desc":"str","range":n or [n,n]},...] )

    == Util ==
    createmultisig nrequired ["key",...] ( "address_type" )
    deriveaddresses "descriptor" ( range )
    estimatesmartfee conf_target ( "estimate_mode" )
    getdescriptorinfo "descriptor"
    getindexinfo ( "index_name" )
    signmessagewithprivkey "privkey" "message"
    validateaddress "address"
    verifymessage "address" "signature" "message"

    == Wallet ==
    abandontransaction "txid"
    abortrescan
    addmultisigaddress nrequired ["key",...] ( "label" "address_type" )
    backupwallet "destination"
    bumpfee "txid" ( options )
    createwallet "wallet_name" ( disable_private_keys blank "passphrase" avoid_reuse descriptors load_on_startup )
    dumpprivkey "address"
    dumpwallet "filename"
    encryptwallet "passphrase"
    getaddressesbylabel "label"
    getaddressinfo "address"
    getbalance ( "dummy" minconf include_watchonly avoid_reuse )
    getbalances
    getnewaddress ( "label" "address_type" )
    getrawchangeaddress ( "address_type" )
    getreceivedbyaddress "address" ( minconf )
    getreceivedbylabel "label" ( minconf )
    gettransaction "txid" ( include_watchonly verbose )
    getunconfirmedbalance
    getwalletinfo
    importaddress "address" ( "label" rescan p2sh )
    importdescriptors "requests"
    importmulti "requests" ( "options" )
    importprivkey "privkey" ( "label" rescan )
    importprunedfunds "rawtransaction" "txoutproof"
    importpubkey "pubkey" ( "label" rescan )
    importwallet "filename"
    keypoolrefill ( newsize )
    listaddressgroupings
    listlabels ( "purpose" )
    listlockunspent
    listreceivedbyaddress ( minconf include_empty include_watchonly "address_filter" )
    listreceivedbylabel ( minconf include_empty include_watchonly )
    listsinceblock ( "blockhash" target_confirmations include_watchonly include_removed )
    listtransactions ( "label" count skip include_watchonly )
    listunspent ( minconf maxconf ["address",...] include_unsafe query_options )
    listwalletdir
    listwallets
    loadwallet "filename" ( load_on_startup )
    lockunspent unlock ( [{"txid":"hex","vout":n},...] )
    psbtbumpfee "txid" ( options )
    removeprunedfunds "txid"
    rescanblockchain ( start_height stop_height )
    send [{"address":amount},{"data":"hex"},...] ( conf_target "estimate_mode" fee_rate options )
    sendmany "" {"address":amount} ( minconf "comment" ["address",...] replaceable conf_target "estimate_mode" fee_rate verbose )
    sendtoaddress "address" amount ( "comment" "comment_to" subtractfeefromamount replaceable conf_target "estimate_mode" avoid_reuse fee_rate verbose )
    sethdseed ( newkeypool "seed" )
    setlabel "address" "label"
    settxfee amount
    setwalletflag "flag" ( value )
    signmessage "address" "message"
    signrawtransactionwithwallet "hexstring" ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )
    unloadwallet ( "wallet_name" load_on_startup )
    upgradewallet ( version )
    walletcreatefundedpsbt ( [{"txid":"hex","vout":n,"sequence":n},...] ) [{"address":amount},{"data":"hex"},...] ( locktime options bip32derivs )
    walletlock
    walletpassphrase "passphrase" timeout
    walletpassphrasechange "oldpassphrase" "newpassphrase"
    walletprocesspsbt "psbt" ( sign "sighashtype" bip32derivs )

    == Zmq ==
    getzmqnotifications

For more specific help use:

    bitcoin-cli help <command_name>

For example:

    ubuntu@btc:~$ bitcoin-cli help getblockchaininfo 
    getblockchaininfo
    Returns an object containing various state info regarding blockchain processing.

    Result:
    {                                         (json object)
    "chain" : "str",                        (string) current network name (main, test, regtest)
    "blocks" : n,                           (numeric) the height of the most-work fully-validated chain. The genesis block has height 0
    "headers" : n,                          (numeric) the current number of headers we have validated
    "bestblockhash" : "str",                (string) the hash of the currently best block
    "difficulty" : n,                       (numeric) the current difficulty
    "mediantime" : n,                       (numeric) median time for the current best block
    "verificationprogress" : n,             (numeric) estimate of verification progress [0..1]
    "initialblockdownload" : true|false,    (boolean) (debug information) estimate of whether this node is in Initial Block Download mode
    "chainwork" : "hex",                    (string) total amount of work in active chain, in hexadecimal
    "size_on_disk" : n,                     (numeric) the estimated size of the block and undo files on disk
    "pruned" : true|false,                  (boolean) if the blocks are subject to pruning
    "pruneheight" : n,                      (numeric) lowest-height complete block stored (only present if pruning is enabled)
    "automatic_pruning" : true|false,       (boolean) whether automatic pruning is enabled (only present if pruning is enabled)
    "prune_target_size" : n,                (numeric) the target size used by pruning (only present if automatic pruning is enabled)
    "softforks" : {                         (json object) status of softforks
        "xxxx" : {                            (json object) name of the softfork
        "type" : "str",                     (string) one of "buried", "bip9"
        "bip9" : {                          (json object) status of bip9 softforks (only for "bip9" type)
            "status" : "str",                 (string) one of "defined", "started", "locked_in", "active", "failed"
            "bit" : n,                        (numeric) the bit (0-28) in the block version field used to signal this softfork (only for "started" status)
            "start_time" : xxx,               (numeric) the minimum median time past of a block at which the bit gains its meaning
            "timeout" : xxx,                  (numeric) the median time past of a block at which the deployment is considered failed if not yet locked in
            "since" : n,                      (numeric) height of the first block to which the status applies
            "statistics" : {                  (json object) numeric statistics about BIP9 signalling for a softfork (only for "started" status)
            "period" : n,                   (numeric) the length in blocks of the BIP9 signalling period
            "threshold" : n,                (numeric) the number of blocks with the version bit set required to activate the feature
            "elapsed" : n,                  (numeric) the number of blocks elapsed since the beginning of the current period
            "count" : n,                    (numeric) the number of blocks with the version bit set in the current period
            "possible" : true|false         (boolean) returns false if there are not enough blocks left in this period to pass activation threshold
            }
        },
        "height" : n,                       (numeric) height of the first block which the rules are or will be enforced (only for "buried" type, or "bip9" type with "active" status)
        "active" : true|false               (boolean) true if the rules are enforced for the mempool and the next block
        },
        ...
    },
    "warnings" : "str"                      (string) any network and blockchain warnings
    }

    Examples:
    > bitcoin-cli getblockchaininfo 
    > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getblockchaininfo", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

At the end of command you will see the HTTP api information

The `bitcoin-cli getinfo` command was removed in `0.16` apparently.

You can however use `bitcoin-cli -getinfo`

### Exploring and decoding transactions

Use `getrawtransaction` with the `txid`

    bitcoin-cli getrawtransaction 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2

> A transaction id is not authorisative until a transaction has been confirmed. Only once confirmed in a block is the transaction immuntable and authoritive.

`getrawtransaction` returns the serialised transaction in hexadecimal to decode it you must input it into `decoderawtransaction`

    {
        "txid": "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2",
        "size": 258,
        "version": 1,
        "locktime": 0,
        "vin": [
            {
            "txid": "7957a35fe64f80d234d76d83a2...8149a41d81de548f0a65a8a999f6f18",
            "vout": 0,
            "scriptSig": {
                "asm":"3045022100884d142d86652a3f47ba4746e”,
                “hex":"483045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1de..."
            },
            "sequence": 4294967295
            }
        ],
        "vout": [
            {
                "value": 0.01500000,
                "n": 0,
                "scriptPubKey": {
                    "asm": "OP_DUP OP_HASH160 ab68...5f654e7 OP_EQUALVERIFY OP_CHECKSIG",
                    "hex": "76a914ab68025513c3dbd2f7b92a94e0581f5d50f654e788ac",
                    "reqSigs": 1,
                    "type": "pubkeyhash",
                    "addresses": [
                        “1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA"
                    ]
                }
            },
            {
                "value": 0.08450000,
                "n": 1,
                "scriptPubKey": {
                    "asm": "OP_DUP OP_HASH160 7f9b1a...025a8 OP_EQUALVERIFY OP_CHECKSIG",
                    "hex": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
                    "reqSigs": 1,
                    "type": "pubkeyhash",
                    "addresses": [
                        "1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK"
                    ]
                }
            }
        ]
    }

This transaction used 1 input - who's input was a previous transaction.
The output is the `15` millibit and an output back to the sender (the change)

### Exploring Blocks

Blocks can be referenced by block height or block hash.

To get the hash of a specific block height:

    bitcoin-cli getblockhash 277316
    0000000000000001b6b9a13b095e96db41c4a928b97

Then we can get the block:

    bitcoin-cli getblock 0000000000000001b6b9a13b095e96db41c4a928b97

    {
        "hash": "0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4",
        "confirmations": 37371,
        "size": 218629,
        "height": 277316,
        "version": 2,
        "merkleroot": "c91c008c26e50763e9f548bb8b2fc323735f73577effbc55502c51eb4cc7cf2e",
        "tx": [
            "d5ada064c6417ca25c4308bd158c34b77e1c0eca2a73cda16c737e7424afba2f",
            "b268b45c59b39d759614757718b9918caf0ba9d97c56f3b91956ff877c503fbe",
            "04905ff987ddd4cfe603b03cfb7ca50ee81d89d1f8",
            ...
        ],
        "time": 1388185914,
        "mediantime": 1388183675,
        "nonce": 924591752,
        "bits": "1903a30c",
        "difficulty": 1180923195.258026,
        "chainwork": "000000000000000000000000000000000000000000000934695e92aaf53afa1a",
        "previousblockhash": "0000000000000002a7bbd25a417c0374cc55261021e8a9ca74442b01284f0569",
        "nextblockhash": "000000000000000010236c269dd6ed714dd5db39d3”
    }

### Accessing functions programmatically

You can use `curl` as the api is HTTP:

    curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/

So you can use the http client of your choice or a package like [bitcoinlib](https://bitcoinlib.readthedocs.io/en/latest/) or [python bitcon lib](https://python-bitcoinlib.readthedocs.io/en/latest/)

The api is more useful when doing many rpc calls in an automated way


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

### Private Keys

The private key is used to spend (and prove ownership) - it must be kept as secret and safe as possible.
It must remain secret at all times - giving control to a third party gives them control over that bitcoin.

    The private key must remain secret at all times.
    The private key must remain secret at all times.
    The private key must remain secret at all times.

> The private key must be backed up and protected from loss - a loss is a loss forever.

A private key can be picked at random - 256 bit.

Creating a bitcoin is essential pick a number from 1 to 2^256.
It is important to have entropy - randomness - to generate a private key.

More precisely a number:

    between 1 and (1.158 * 10^77) - 1

So produce a number from putting a string through `SHA256` hashing function and ensuring is it less than 1.158 * 10^77

> Do not use your own code to generate a random number - use a cryptographically secure pseudo random number generator

The set of private keys is unfathomably large: 2^256 or 10^77

The visible universe is estimated to contain 10^80 atoms

#### Generating a Private Key

    bitcoin-cli getnewaddress
    1J7mdg5rbQyUHENYdx39WVWK7fsLpEoXZy

For security reasons, only the public key is shown.

To expose the private key use:

    bitcoin-cli dumpprivkey 1J7mdg5rbQyUHENYdx39WVWK7fsLpEoXZy
    KxFC1jmwwCoACiCAWZ3eXa96mBM6tb3TYzGmf6Ywgd

> It is not possible for bitcoin to know the private key from the public key - unless it is stored in the wallet.

### Public Keys

Public keys are calculated using irreversible elliptic curve multiplication.

The owner of a private key can generate a public key using elliptical curve cryptography and share it - knowing the private key cannot be acquired from the public key.

It becomes the basis for unforgable secure digital signatures and to prove ownership.

Bitcoin uses a specific elliptic curve: `secp256k1`

You can check that a coordinate is on the `secp256k1` curve if:

    >>> (x ** 3 + 7 - y**2) % p = 0

This is the _point at infinity_ 

#### Generating a public key

The private key `k` is multiplied by a generator point `G` results in a public key `K`

> Most bitcoin implementations use openssl's `EC_POINT_mul()` to derive the public key.

### Bitcoin Addresses

A string of digits and characters that can be shared with anyone to send you money.

Addresses are produced from public keys and begin with the digit `1` on the `mainnet`

    eg: 1J7mdg5rbQyUHENYdx39WVWK7fsLpEoXZy

A bitcoin address can represent the owner of a private/public key pair or it can represent a P2SH (Pay to script Hash).

A `SHA` (Secure Hash Algorithm) and `RIPEMD160` are used to make a bitcoin address.

    A = RIPEME160(SHA256(K))

Where `K` is the public key and `A` is the address

Bitcoin addresses are encoded as `Base58Check` which uses 58 characters to avoid ambiguity

#### Encoding

In order to represent long numbers in a compact way - many computer systems use alphanumeric representations.

* decimal system: 10 numerals
* hexadecimal system: 16 alphanumerics (0 - 10 and A through F)
* Base64 system: 26 lower case, 26 capital, 10 numerals and `+` and `/`

> Base64 is commonly used to attach binary to emails

Base58 excludes characters that are frequently mistaken to each other.
Base58Check adds 4 bytes at the end to validate

It prevents a mistypes bitcoin address to be accepted by the wallet software.

#### Base58Check Prefixes

* Bitcoin address: 1
* P2SH (Pay to script hash): 3
* Bitcoin testnet address: m or n
* Private key WIF: 5, K or L
* BIP-38 encrypted private key: 6P
* BIP-32 extended public key: xpub

### Key Formats

Public keys and private keys can be in various formats.

#### Private Key Formats

* Hex: 64 hexadecimals
* WIF: Base58Check prefix of 5
* WIF Compressed: Base58Check prefix K or L

> Install [bitcoin explorer](https://github.com/libbitcoin/libbitcoin-explorer) for a command line tool with many functions including being able to convert between formats

Convert from one format to other:

    bx wif-to-ec 5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn
    1e99423a4ed27608a15a2616a2b0e9e52ced330ac53

You can decode base58check:

    bx base58check-decode 5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2Jpbnkeyh

#### Public Key Formats

Compressed public keys were introduced to conserve space on nodes (reduce size of transactions).
Each public key requires 520 bits. With several hundred transactions per block.

Only the x co-ordinate is needed.

Uncompressed public keys have a prefix of `04`

Compressed public keys have a prefix of `02` or `03`. `02` if `y` is even, `03` if y is odd.

    (x, y) -> 04 x y    -> 02 x (even)
                        -> 03 x (odd)

Generating an address from the uncompressed public key will be difference from the compressed.

WIF compressed private keys start with a 1 byte suffix `01` - compressed private keys really mean a private key where only compressed public keys should be derived.

### Advanced Keys and Addresses

#### Encrypted Private Keys

Private keys must remain secret. However the confidentiality conflicts with the availability.

Keeping a private key private is harder when you need to store backups.
There are a lot of variables and methods and ways for things to go wrong.

BIP-38 is an encryption scheme that has the prefix `6P` - and requires a password.

The most common case for BIP-38 is for paper wallets - to backup private keys on a piece of paper.

> As long as the user selects a strong passphrase, a paper wallet with BIP-38 encrypted private keys is incredibly secure and a great way to create offline bitcoin storage

Go to [bitaddress.org](https://www.bitaddress.org) and enter wallet details:

    private key: 6PRTHL6mWa48xSopbU1cKrVjpKbBZxcLRRCdctLJ3z5yxE87MobKoXdTsJ
    passphrase: MyTestPassphrase

It should decrypt to:

    5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn

### P2SH pay to script hash and multisig

Bitcoin addresses starting with `3` are pay to script hash.
They designate the beneficiary as a hash of a script instead of a public key.

Unlike transactions that send to a `1` public key called P2PKH (Pay to public key hash),
addresses starting with `3` require more than just the single private key proof of ownership.

### Multisignature Addresses

* Common implementation of P2SH
* 2 out 3 signatures are required to spend (sign the spending)

### Vanity Addresses

Eg: `1LoveBPzzD72PUXLzCkYAtGFYmK5vYNR33`

The process to get them:

1. random private key
2. deriving the bitcoin address
3. check if it matches a desired vaity pattern

Average search time on a desktop pc for vanity address:

* `1K` - 1 in 58: < 1 ms
* `1Kids` - 1 in 11 million: 1 minute
* `1KidsCh` - 1 in 38 billion: 2 days
* `1KidsCharity` - 1 in 23 quintillion: 2.5 million years

Generating a random address is a bruteforce exercise.

Vanity addresses make it harder for others to fool your customers.

It is better to create a dynamic address per donor instead of a fixed one.

### Paper Wallets

Bitcoin private keys printed on paper.
Protection against hard drive failure, theft or accidental deletion.

If they are generated offline they are more secure against threats.

They are just a private key and address printed on a piece of paper.

> Put these paper wallets in a fireproof safe and “send” bitcoin to their bitcoin address, to implement a simple yet highly effective “cold storage” solution.

A better way is to use a BIP-38 encrypted paper wallet.

    Although you can deposit funds into a paper wallet several times, you should withdraw all funds only once, spending everything. This is because in the process of unlocking and spending funds some wallets might generate a change address if you spend less than the whole amount. Additionally, if the computer you use to sign the transaction is compromised, you risk exposing the private key. By spending the entire balance of a paper wallet only once, you reduce the risk of key compromise. If you need only a small amount, send any remaining funds to a new paper wallet in the same transaction.
    
## 5. Wallets

Wallets describe a few different things in bitcoin.

At a high level a wallet is an application that serves as the primary user interface.

* controls access to money
* manages keys and addresses
* creates and signs transactions
* tracking balance

From a programmer's perspective wallets are containers for private keys.

### Wallet Technology

User friendly, secure and flexible bitcoin wallets

Wallets do not contain bitcon, they only contain keys. The bitcoin is recorded on the blockchain in the bitcoin network.

Users control the coins by signing transactions in their wallet.

Types of wallets:

* nondeterministic wallets - Each key is independently generated from a random number. Keys are not related to each other. _Just a bunch of keys_
* deterministic wallets - All keys are derived from a master key - known as a _seed_. There are many key derivation methods - the most common is the tree-link hierachical deterministic wallet (HD wallet).

Deterministric wallets are initilaised from a seed. Seeds are encoded as english words _mnemonic code words_

#### Non deterministic wallets

The first bitcoin wallet - bitcoin core.
Wallets were a collection of randomly generated private keys.

Bitcoin core pregenerated 100 random private keys when first started. More can be generated.

A single key is only used once.

Non deterministic wallets are cumbersome to manage, backup and import.

You need to keep every single key and make backups. If inaccessible all funds are lost forever.

> This conflicts with the prinicple of using a bitcoin address only once.

Address reuse reduces privacy.

A type-0 is a poor choice if you want to avoid address reuse. Bitcoin core however comes with a type-0 wallet.

They are doscouraged for anything other than simple tests. They are too cumbersome to manage.
A HD wallet with mnemonic seed for backup.

> As of bitcoin-core 0.13.0, core uses HD wallets by default.

#### Deterministic Wallets

* Have private keys all derived from a single seed
* The most advanced deterministic wallet is the HD (hierachical deterministic) wallet from BIP-32
* Parent child - tree structure

Two major advangages:

* Structure can convey additional meaning - a specific branch for receiving and one for sending payments and another to receive change from transactions
* Users can create a sequence of public keys without having access to the corresponding private keys - so can be used on insecure servers or in a recieve only capacity issuing a different public key for each transaction. Server will never have the private keys.

### Seeds and Mnemonic Codes (BIP39)

Standardised into a sequence of english words easier to transcribe and export.
Most wallets now allow for import and export of the seed as mnemonics.

> Bitcoin Core contributors don't consider BIP 39 to be secure

For example:

    0C1E24E5917779D297E14D45F14E1A1A
    army van defense carry jealous true
    garbage claim echo media make crunch

Top is the seed in Hex, below in english mnemonics.

### Wallet best practices

* HD Wallets based on BIP-32
* Multipurpose HD wallet structure based on BIP-43
* Multicurrency and multiaccount based on BIP-44

These standards may remain or become obsolete

### Using a Bitcoin Wallet

Trezor - USD device with 2 buttons. Store keys in the form of a HD wallet.
The first use a mnemonic and seed was generated from the built in pseudo random number generator.

A numbered sequence of words - that gabriel wrote down - the backup.
The sequence of words is important.

A 12 word mnemonic is used, some wallets use the more secure 24 word mnemonic.

### Wallet Technolofy Details

Mnemonics are often confused with "brain" wallets.
A brain wallet consists of words chosen by the user.

More info in the books about:

1. Generating mnemonic words
2. Generating the mnemonic from seed 

A seed can also have a passphrase.

The passphrase protects compromise from a thief, gives a form of plausible deniability or duress wallet (give passphrase to wallet of smaller amounts). 
If the wallet owner dies the seed is useless and lost forever.

#### Creating a HD wallet from the seed

HD wallets are created from a root seed.
A 128, 256 or 512 bit random number.

Every key in a HD wallet is deterministically derived from the root seed.

Making it easy to backup, restore, export and import HD wallets containing millions of keys.

The seed is put into a HMAC-SHA512 algorithm to create the master private key and master chain code.
Master private key generates the corresponding master public key.

Child key derivation function. Child keys are derived from parent keys - more info on the book on this...

Child private keys are indistinguishable from nondeterministic random keys.
You cannot find the parent or siblings or children.
You need the child private key and child chain code.

A child private key can therefore be used to make a public key and bitcoin address.
Then it can be used to sign transactions and spend from that address.

#### Extended Keys

The private key and chain code together is called the extended key.
Sharing an extended key gives access to the entire branch.

Extended keys are encoded in Base58Check and start with `xprv` and `xpub`

Public child key derivation

Derive public child keys from public parent keys without access to the private key.
This is what many online shops and payment providers like btc-pay-server and bitcartCC need in order to generate addresses and invoices for sales and donations.

> This shortcut can be used to create very secure public key–only deployments where a server or application has a copy of an extended public key and no private keys whatsoever. That kind of deployment can produce an infinite number of public keys and bitcoin addresses, but cannot spend any of the money sent to those addresses. - perfect for an nline ecommerce store

Uses public key derivation to generate a new bitcoin address

The extended private key is always offline but the extended public key can be used to generate addresses.

It becomes difficult to match orders to transactions using a single bitcoin address.

> Note that hardware wallets will never export private keys—those always remain on the device.

#### Hardened Derivation

> Access to an xpub does not give access to child private keys. However, because the xpub contains the chain code, if a child private key is known, or somehow leaked, it can be used with the chain code to derive all the other child private keys. A single leaked child private key, together with a parent chain code, reveals all the private keys of all the children. Worse, the child private key together with a parent chain code can be used to deduce the parent private key.

To counter this issue some HD wallets use _hardened derivation_

parent private key is used to derive the child chain code.

> Bitcoin core does not support `xpub` extended public key - it uses hardened derivation. Check this answer from [Pieter Wuille](https://bitcoin.stackexchange.com/questions/90135/how-do-i-export-an-xpub-from-bitcoin-core-for-use-in-btcpayserver). You cannot export a `xpub` from bitcoin-core. This functionality is simply not possible; the keys generated by Bitcoin Core cannot be predicted by an xpub. You can use other wallet software, however.

**Note: Bitcoin-core also does not support seed phrases. This is not because bitcoin-core is bare bones and slow. It was decided due to security reasons. Both seedphrases and `xpub` key derivation make bitcoin less cryptographically secure at the moment.

#### Index Numbers for normal and hardened derivation

...more in the book

#### HD Wallet Key Identifiers

Keys are identified using a path naming convention. Each level seperated by a `/`.
Private keys derived from the master private key start with `m`
Public keys derived from the master public key start with `M`

The first child is `m/0`
The second grandchild of the first is  `/m/0/1`

* `m/0` - first child of master private key
* `m/0/0` - first grandchild of master private key
* `m/'0/0` - The first normal child of the first hardened child of the master private key
* `M/23/17/0/0` - public key

#### Navigating the HD Wallet structure

Each parent extended key can have 4 billion children
2 billion harded and 2 billion normal

Each of those can have 4 billion.

That becomes quite hard to navigate.

BIP-43 specified special purpose branches `m/i'/`

BIP-44 specified using only `m/44'/`

for `m /purpose' / coin_type' / account' / change / address_index`

Coin type specified the type or cryptocurrency coin - or rather net?
Since there is only 1 - bitcoin.

* Bitcoin mainnet: `m/44'/0'`
* Bitcion testnet: `m/44'/1'`

The third level is for account.

The fourth level has is change - one for creating receiving addresses and 1 for creating change addresses.
Uses normal derivation - not hardened - to allow exporting of extended public keys in nonsecured environments.

The fifth level is receiving addresses.

## 6. Transactions

Transactions are the most important thing.

Everything else is built to ensure transactions can be created, propagated on the network, validated and added to the global network.

Transactions encode the transfer of value between participants in the bitcon system. 
Every transaction is recorded in the ledger - the blockchain.

We can get alice's transaction:

    ubuntu@btc:~$ bitcoin-cli getrawtransaction 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2 true
    {
        "txid": "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2",
        "hash": "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2",
        "version": 1,
        "size": 258,
        "vsize": 258,
        "weight": 1032,
        "locktime": 0,
        "vin": [
            {
            "txid": "7957a35fe64f80d234d76d83a2a8f1a0d8149a41d81de548f0a65a8a999f6f18",
            "vout": 0,
            "scriptSig": {
                "asm": "3045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e3813[ALL] 0484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adf",
                "hex": "483045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e381301410484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adf"
            },
            "sequence": 4294967295
            }
        ],
        "vout": [
            {
            "value": 0.01500000,
            "n": 0,
            "scriptPubKey": {
                "asm": "OP_DUP OP_HASH160 ab68025513c3dbd2f7b92a94e0581f5d50f654e7 OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a914ab68025513c3dbd2f7b92a94e0581f5d50f654e788ac",
                "reqSigs": 1,
                "type": "pubkeyhash",
                "addresses": [
                "1GdK9UzpHBzqzX2A9JFP3Di4weBwqgmoQA"
                ]
            }
            },
            {
            "value": 0.08450000,
            "n": 1,
            "scriptPubKey": {
                "asm": "OP_DUP OP_HASH160 7f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a8 OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac",
                "reqSigs": 1,
                "type": "pubkeyhash",
                "addresses": [
                "1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK"
                ]
            }
            }
        ],
        "hex": "0100000001186f9f998a5aa6f048e51dd8419a14d8a0f1a8a2836dd734d2804fe65fa35779000000008b483045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e381301410484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adfffffffff0260e31600000000001976a914ab68025513c3dbd2f7b92a94e0581f5d50f654e788acd0ef8000000000001976a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac00000000",
        "blockhash": "0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4",
        "confirmations": 414667,
        "time": 1388185914,
        "blocktime": 1388185914
    }

* Where is alice's address?
* Where is bob's address?
* Where is the 0.1 input sent by Alice?

> In bitcoin, there are no coins, no senders, no recipients, no balances, no accounts, and no addresses. Those are constructed on a higher level.

#### Transaction inputs and outputs

Transaction outputs are indivisible chunks of bitcoin currency, recorded on the blockchain.
Bitcoin full nodes track the UTXO - unspent transaction outputs.

The `utxo set` - every transaction represents a change to the utxo set.

When a wallet has _received_ bitcoin - what we mean is the wallet has detected a UTXO that can be spent with one of the keys controlled by the wallet.

The users's balance is the sum of UTXO.
The wallet creates the balance by scanning the blockchain.

Bitcoin can be divided down to 8 decimal places - satoshis.
Outputs are discrete (interger) indivisible units.

When spent the whole amount must be spent and change must be generated.

Buying something for `1` using an output of `20`, you need to input the entire `20` and set 2 outputs `19` back to your wallet and `1` to the intended receiver.

The wallet will select the UTXO greater or equal to the amount to spend.

There are exceptions to the output and input chain.

#### Coinbase transaction

This is a _coinbase_ transaction - the first transaction is every block.
This is the transaction placed by the winning miner and creates brand new bitcoin payable to the miner as a reward.
It does not consume UTXO.
The input is the coinbase.

This is how bitcoin's _money supply_ is created.

The second blocks `vin`:

    "vin": [
        {
        "coinbase": "04ffff001d0104",
        "sequence": 4294967295
        }
    ]

You cannot get the genesis block transaction, it is not in the database:

    ubuntu@btc:~$ bitcoin-cli getrawtransaction 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
    error code: -5
    error message:
    The genesis block coinbase is not considered an ordinary transaction and cannot be retrieved

New transactions consume the `utxo` set. 

Transaction outputs consist of:

* An amount of bitcoin denominated in satoshis
* A cryptographic puzzle that determines the conditions required to spend the output - known as the `scriptPubKey`, locking or witness script.

    "vout": [
        {
        "value": 50.00000000,
        "n": 0,
        "scriptPubKey": {
            "asm": "0496b538e853519c726a2c91e61ec11600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781e62294721166bf621e73a82cbf2342c858ee OP_CHECKSIG",
            "hex": "410496b538e853519c726a2c91e61ec11600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781e62294721166bf621e73a82cbf2342c858eeac",
            "type": "pubkey"
        }
        }
    ],

Using the bitcoin cli the value is in bitcoin, but in the transaction itself it is in satoshis.
The script is a specific scripting language.

Transaction output serialisation:

* `amount` - 8 bytes - bitcoin vlaue in satoshis
* `locking-script size` - 1 to 9 bytes - locking script
* `locking-script` - a script defining the conditions needed to spend the output

#### Transaction Inputs

Identify:

* utxo to be consumed
* proof of ownership through unlocking script

        "vin": [
            {
            "txid": "7957a35fe64f80d234d76d83a2a8f1a0d8149a41d81de548f0a65a8a999f6f18",
            "vout": 0,
            "scriptSig": {
                "asm": "3045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e3813[ALL] 0484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adf",
                "hex": "483045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e381301410484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adf"
            },
            "sequence": 4294967295
            }
        ],

* `txid` is a pointer to a `UTXO` unspent transaction
* `vout` is the output index from the transaction it is referencing
* `scriptSig` is the unlocking script or conditions, usuallly the digital signature and public key proving ownership of the bitcoin.
* `sequence` is 

The references `utxo` needs to be retrieved...without retreiveing the referenced transactions you know very little.

More info on byte-string representation in the book.

#### Transaction Fees

Fees make it economically infeasible for attackers to flood the network with transactions.

> Most wallets calculate and include transaction fees automatically.

If you are making the transaction manually you need to account for transaction fees.
Transaction fees are also an incentive to (mine) include a transaction into the next block.
Transaction fees are collected by the miner.

Transaction fees are calucated on the size of the transaction in kilobytes - not the value of the bitcoin transacted.

Miners prioritize transactions based on factors:

Transactions with insufficient or no fees might be delayed
Transactions without fees might be processed eventually

Fees fluctuate based on network capacity and transaction volume
Since 2016 - capacity limits creeated competition between transactions
Zero fee transactions rearely get mined and rarely get propagated

You can set fee relay policies on your node with:

    minrelaytxfee=0.00001

> ignored and only relayed if there is space in the mempool

Wallets must implement dynamic fees using a third party fee estimation service.
They estimate the satoshis per bytes that give a high probablity of inclusion in the next block.

    $ http https://bitcoinfees.earn.com/api/v1/fees/recommended
    {
        "fastestFee": 102,
        "halfHourFee": 102,
        "hourFee": 88
    }

* fastestFee: The lowest fee (in satoshis per byte) that will currently result in the fastest transaction confirmations (usually 0 to 1 block delay).
* halfHourFee: The lowest fee (in satoshis per byte) that will confirm transactions within half an hour (with 90% probability).
* hourFee: The lowest fee (in satoshis per byte) that will confirm transactions within an hour (with 90% probability).

**Fees are not explicit**

Fees are calculated from the sum of the inputs minus the sum of the outputs

> If you are constructing your own transactions you must ensure you do not inadvertently include a very large fee by underspending the inputs

Alice wants to spend 0.015 for coffee.
She includes a 0.001 transaction fee.
Her wallet must source a UTXO greater than 0.016.

Using a 0.2 bitcoin utxo, she creates one output 0.015 to bob's cafe. Then 0.184 back to her wallet.
Leaving 0.001 unallocated.

Another example is the kids charity, that has recieved many small donations totalling 50 BTC.
Fow a big purchase many hunders of small UTXO's need to be sourced.
The transaction size may be a kilobyte or several kilobytes - needing a much higher transaction fee.

#### Transaction Script and Script Language

Bitcoin's tranasction script language called `Script`, is a Forth-like reverse-polish notation stack-based execution language. _Quite a mouthful_

> When a transaction is validated, the unlocking script in each input is executed alongside the corresponding locking script to see if it satisfies the spending condition.

Most transactions have a pay-to-public-key-hash (p2pkh) - eg. pay to Bob's wallet

#### Turing Incompleteness

There are no loops or complex flow - ensuring the language is not _turing complete_

Complexity is limited ensuring predicatable execution times

No logic bombs or denial of service

#### Stateless Verification

No state is saved after script execution.
All the information needed to execute the script is contained in the script.

#### Script Construction

A locking script and unlocking script.
A locking script - a spending condition placed on an output.

Historically the locking script was called `scriptPubKey` because it usually contained a public key or bitcoin address. It is also refered to as a `witness script`.

The unlocking script solves the locking script. They are part of the transaction input.
Most of the time they contain a digital signature form the user's private key.

Historically the input script was called `scriptSig`

The validation will copy the unlocking script, retrieve the UTXO referenced by the input and the UTXO locking script. That is then executed in sequence.

Only a valid transaction is spent and removed from the unspent transaction outputs (utxo set).

Eg. pay to public key hash

    <sig> <PubK> + DUP HASH160 <PubKHash> EQUALERIFY CHECKSIG

#### The script execution stack

A stack - allows push and pop.

It is LIFO: Last in, first out

* `OP_ADD`: pop 2 items from the stack, add them and push the results to the stack
* `OP_EQUAL`: pops 2 items from the stack and pushes `TRUE` (1) if they are equal, `FALSE` (0) if they are not equal.
* `DUP`: duplicates the top item onto the stack
* `HASH160`: hashes the top item with `RIPEMD160(SHA256(PukKeyHash))`
* `EQUALVERIFY`: compares hashes if equal - both are removed
* `CHECKSIG`: ensures the signature matches the public key

Example:

    2 3 OP_ADD 5 OP_EQUAL
    Puts 2 and 3 on the stack, adds them and adds that to the stack, then adds 5 and checks if it is equal

Anything resulting in True is valid

If the locking script is `3 OP_ADD 5 OP_EQUAL` then only an input of `2` would allow it to transact

Transactions are invalid if the top value on the stack is false after script execution.

    2 + 7 - 3 + 1
    2 7 OP_ADD 3 OP_SUB 1 OP_ADD 7 OP_EQUAL

#### Seperate execution of locking and unlocking scripts

In 2010 the sequencial parsing was removed as it was a vulernability, allowing corruption of the locking script by the unlocking script.

First the unlocking script is executed, then if there is nothing dangling the main stack is copied and the locking script is executed.

#### Pay to public key hash (P2PKH)

Locking script locks the output to a public key hash - a bitcoin address.
The script can be unlocked by presenting a public key and digital signature created by the corresponding private key.

    OP_DUP OP_HASH160 <Cafe Public Key Hash> OP_EQUALVERIFY OP_CHECKSIG

* `Cafe Public Key Hash` is the bitcoin address without the BASE58Check Encoding

This script can be satisfied with an unlocking script:

    <Cafe Signature> <Cafe Public Key>

Combined:

    <Cafe Signature> <Cafe Public Key> OP_DUP OP_HASH160 <Cafe Public Key Hash> OP_EQUALVERIFY OP_CHECKSIG

### Digital Signatures (ECDSA)

Provide proof of ownership without revealing the private key.
ECDSA - Eliiptical curve digital signature algorithm

Used by `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKFIGMULTISIG`, `OP_CHECKFIGMULTISIGVERIFY`

Three purposes:

* proves the owner has authorized the transaction
* proof of authorizatoin is undeniable
* transaction has not and cannot be modified after being signed

> Each transaction input is signed independently - multiple parties can create transactions

Digital signature - Ensures a digital message or documents were created by a known sender (authnetication), the sender cannot deny having sent the message (nonrepudiation) and the message was not altered (integrity).

How they work:

1. algorithm for creating the signature using the using a private key from a message.
2. allows anyone to verify given the message and public key

In bitcoin's case:

* the "message" being signed is the transaction
* the signing key is the user's private key

#### SIGHASH

THe signature hash indicates what signature signs what part of the transaction

> You likely won't see anything other than `SIGHASH_ALL` used to sign p2pkh

More on ECDSA math...

### Bitcoin Addresses, Balances and other Abstractions

Within the output of the previous transaction is a locking script that locks the UTXO to alice's public key hash.
The application (blockchain explorer) extracts the public key hash and BASE58Check encodes to see the bitcoin address that represents the public key.

The outputs have 2: one to the receipient and the other back to change address.

The application extracts the locking scipt as a public key hash and reencodes as BASE58CHECK.

The "balance" is something that exists outside of bitcoin - it is a concept that lives in wallets.
The final balance needs to check against the UTXO set (unspent).

Other non pay to public key hash transactions can stump bitcoin wallets.

## 7. Advanced transactions and scripting

A bit too much for me today, get the book and read this if you want.

## 8. The Bitcoin Network

### Peer-to-peer architecture

Bitcoin is structured as a peer-to-peer network on top of the internet.

They are peers - they are equal. It is not a client server architecture.
Nodes interconnect in a flat topology.
No centralisation and no hierachy.

Nodes consume and provide services at the same time.

This used to be how the internet was, however it is now more hierachical.

Decentralisation is a core design principle.

Miners use the stratum protocol.

### Node types and roles

Nodes can take on different roles:

* Wallet
* Miner
* Full Blockchain
* Network Routing Node

All nodes include the routing function to participate in the network.

Full nodes maintain a complete and up-to-date copy of the blockchain

> Full nodes can autonomously and authoritatively verify any transaction without external reference

SPV (simplified payment verification) nodes only maintain a subset of the blockchain and rely on other full nodes

Mining nodes compete to create new blocks - running the proof of work algorithm.

### The extended bitcoin network

There are currently 10275 bitcoin nodes running - August 2021.

Various large companies run full node clients based on bitcoin core but without wallet and mining functions.
These nodes act as edge routers - allowing other services to be built on top.
Usually to pool mining nodes and for lightweight wallet clients.

The stratum network pools miners.

### Bitcoin Relay Networks

P2P network has too high a latency for miners.
Miners must minimise the time to propagation of a winning block and the beginning of the next round.
In mining, network latency directly relates to profit margins.

A bitcoin relay network attempts to minimise the latency in transmission between blocks.

The original relay (2015) was on AWS, in 2016 it was replaced with FIBRE (Fast Internet Bitcoin Relay Engine) - a UDP based network. It implements compact block optimisation to reduce data transmitted and network latency.

Falcon is a new relay network using _cut-through-routing_ instead of _store-and-fowrward_ 

Relay networks are overlay networks - to provide a connection between nodes with specialised needs.
Shortcuts between congested routes.

### Network Discovery

When a new node boots up - it must discover other bitcoin nodes to participate.
The geographical location is irrelevant.
Any existing bitcoin node can be selected at random.

To connect to a known peer - nodes connect via TCP to 8333.
To establish a connection a handshake is made - specifying version information and other basic info.

* nVersion - the version the bitcion protocol speaks
* nLocalServices - a list of services supported by the node
* nTime - current time
* addrYou - ip address of remote node
* addrMe - ip address of local node
* subver - subversion of software running on client
* BestHeight - the height of this node's blockchain

If the version is compatible the peer will send a `verack`

How does a new node find peers? It queries them using the dns seeds.
Some DNS seeds are custom implementations of BIND (Berkley Internet Name Daemon)

You can also explicitly set the peer node to use to bootstrap.

A node must connect to a few different peers in order to establigh diverse paths into the bitcoin network.
Only 1 connection is needed to bootstrap (is this why setting up a full node takes so long).

You can get peer connections with:

    ubuntu@btc:~$ bitcoin-cli getpeerinfo
    [
    {
        "id": 16,
        "addr": "129.13.189.202:49794",
        "addrbind": "192.168.0.201:8333",
        "addrlocal": "197.245.40.227:8333",
        "network": "ipv4",
        "services": "0000000000000001",
        "servicesnames": [
        "NETWORK"
        ],
        "relaytxes": true,
        "lastsend": 1627977990,
        "lastrecv": 1627977980,
        "last_transaction": 0,
        "last_block": 0,
        "bytessent": 11703361,
        "bytesrecv": 225811,
        "conntime": 1627560593,
        "timeoffset": -61,
        "pingtime": 0.205491,
        "minping": 0.198333,
        "version": 70002,
        "subver": "/dsn.tm.kit.edu/bitcoin:0.9.99/",
        "inbound": true,
        "startingheight": -1,
        "synced_headers": -1,
        "synced_blocks": -1,
        "inflight": [
        ],
        "permissions": [
        ],
        "minfeefilter": 0.00000000,
        "bytessent_per_msg": {
        "addr": 223812,
        "alert": 192,
        "getheaders": 1053,
        "inv": 11255722,
        "ping": 111104,
        "pong": 111328,
        "verack": 24,
        "version": 126
        },
        "bytesrecv_per_msg": {
        "addr": 3190,
        "getaddr": 24,
        "ping": 111328,
        "pong": 111104,
        "verack": 24,
        "version": 141
        },
        "connection_type": "inbound"
    },
    ]

You can override the automatic management of peers with `-connect=<ip addresses>`

If there is no traffic nodes will periodically send a message to maintain a connection.
If a node does not respond for 90 minutes it is assumed to not exist and is disconnected.

### Full Nodes

Full blockchain nodes.
In the early days all nodes were full nodes.
Bitcoin core is a full node client.

Full nodes maintain the full blockchain which they independently build and verify.
From the first block to the latest.

Running a node ves you the full experience - no reliance or trust in a third party is required.
It is more than 400 GB now (August 2021) and it takes a few days to sync to the network - the price of indepedence and freedom.

The most common is Bitcoin Core - the satoshi client.

### Exchanging Inventory

A full node will first try to construct a complete blockchain.
A brand new node only has the genesis block embedded.
The new node will have to download and syncronise 693986 blocks (August 2021)

Getting the `BestHeight` of a peer lets it compare how many blocks the peer has.
A node with a higher height - will known which blocks older nodes need.

It will identify the first 500 blocks the node needs and will transfer them with the `inv` (inventory) message.

The node missing the blocks with send `getData` messages to retrieve them.
The new node will request the blocks among its peers - spreading the load.

### Simplified Payment Verification nodes (SPV's)

More in the book about these...

Bloom filters...

### Encrypted and Authenticated Connections

Originally all nodes transmitted data in clear text.
For full nodes that is not a problem but for SPV's it is.

There are 2 solutions:
* Tor transport
* P2P Authneticationa nd encryption

#### Tor Transport

Stands for "The Onion Routing" network - offers encryptions and encapsulation of data through randomised network paths that offer anonymity, untraceability and privacy.

As of Bitcoin core 0.12 - a node will offer a hidden Tor service automatically.

Turn on bitcoin core's logging for `tor`:

    bitcoind --daemon --debug=tor

It should say:

    tor: ADD_ONION successful

More info in [doc/tor.md](https://github.com/bitcoin/bitcoin/blob/master/doc/tor.md)

#### Peer to peer authentication and encryption

2 Bitcoin Improvement Proposals: 

* BIP-150 - offers optional peer authentication that allows nodes to authenticate each other’s identity using ECDSA and private keys
* BIP-151 - enables negotiated encryption for all communications between two nodes that support BIP-151

All [bitcoin bips can be viewed at github](https://github.com/bitcoin/bips)

#### Transaction Pools

A temporary list of unconfirmed transactions - called the memory pool or transaction pool.

Keeps track of tranasctions known to the network but not included in the blockchain.
Transactions are relayed to neighbouring nodes.

Orphaned transactions reference tranasctions not yet known by the node.
The utxo pool contains millions of entries of unspent transactions.
UTXO only contains confirmed outputs and varies very little between nodes.

## 9. The Blockchain

An ordered backlinked list of transactions.
Stored as a flat file or simple database.

Bitcoin migrated from using Berkley DB to LevelDB.
Blocks stacked on top of each other created the term - block height.

Each block is identified by a hash using SHA256.
Each block also has a parent block. A chain going back all the way to the first block - genesis block.

Multiple children can arise from a blockchain fork - when different blocks are identified simulataneosly by miners.
Eventually only 1 of the blocks will be added.
Each block can only have 1 parent.

The previous block field is in the header and therefore affects the current block's hash.
If the parent is modified - its hash will change. Changing the pointer to the previous block hash which forces the child hash to change.
The computation required to change it - makes the blockchain's history immutable.
Sometimes the most recent blocks need to be recalculated due to a fork. The top six blocks are like top soil - after about 100 blocks the transactions mined can be spent.

### Structure of a block

Consists of:

* block size (4 bytes)
* a block header (80 bytes)
* transaction counter - number of transactions
* list of transactions (250 bytes each)

> Average block has more than 500 transactions

#### Block Header

* Reference to previous block
* Metadata: difficulty, timestamp, nonce
* Merkle tree root: efficiently summarise all transactions in block

- version (4 bytes)
- previous block hash (32 bytes)
- merkle root (32 bytes)
- timestamp (4 bytes) - estimated creation time of the block
- difficulty target (4 bytes) - proof-of-work difficulty target
- Nonce (4 bytes) - A counter for proof-of-work

#### Block Identifiers: Block Header Hash and Block Height

Primary identifier is cryptographic hash - digital fingerprint - hashing block header twice through SHA256.
Resulting 32 byte hash is called the _block hash_

The block hash is not included inside the blocks data structure - **it is computed by each node as the block is received from the network**

Another way to identify a block is by its position in the blockchain - called the _block height_

Block height on 01 January 2017: 446000

Blockchain forks allow a block height to reference 2 competing blocks

#### The Genesis Block

Encoded in the bitcoin client
Every node always knows the genesis block

A trusted secure root of the blockchain

Get the genesis block hash:

    ubuntu@btc:~$ bitcoin-cli getblockhash 0
    000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    
Get the block with extra verbosity:

    ubuntu@btc:~$ bitcoin-cli getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 2
    {
    "hash": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
    "confirmations": 694180,
    "strippedsize": 285,
    "size": 285,
    "weight": 1140,
    "height": 0,
    "version": 1,
    "versionHex": "00000001",
    "merkleroot": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
    "tx": [
        {
        "txid": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
        "hash": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
        "version": 1,
        "size": 204,
        "vsize": 204,
        "weight": 816,
        "locktime": 0,
        "vin": [
            {
            "coinbase": "04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73",
            "sequence": 4294967295
            }
        ],
        "vout": [
            {
            "value": 50.00000000,
            "n": 0,
            "scriptPubKey": {
                "asm": "04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f OP_CHECKSIG",
                "hex": "4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac",
                "type": "pubkey"
            }
            }
        ],
        "hex": "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"
        }
    ],
    "time": 1231006505,
    "mediantime": 1231006505,
    "nonce": 2083236893,
    "bits": "1d00ffff",
    "difficulty": 1,
    "chainwork": "0000000000000000000000000000000000000000000000000000000100010001",
    "nTx": 1,
    "nextblockhash": "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"
    }

View the secret message:

    ubuntu@btc:~$ echo "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000" | xxd -r -p
    ????M??EThe Times 03/Jan/2009 Chancellor on brink of second bailout for banks?????*CAg????UH'g?q0?\֨(?9	?yb??a޶I???L?8??U???\8M??
                                                    ?W?Lp+k?_?

> The genesis block contains a hidden message within it. The coinbase transaction input contains the text “The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.” This message was intended to offer proof of the earliest date this block was created, by referencing the headline of the British newspaper The Times. It also serves as a tongue-in-cheek reminder of the importance of an independent monetary system, with bitcoin’s launch occurring at the same time as an unprecedented worldwide monetary crisis. The message was embedded in the first block by Satoshi Nakamoto, bitcoin’s creator.

#### Linking blocks in the Blockchain

As a node receives new blocks it validates them.
The `previousblockhash` field contains hash of parent block.

#### Merkle Trees

Summary of all transactions

A binary hash tree - summarising and verifying integrity of large sets of data

Efficient process to verify whether a transaction is included in a block.
Merkle tree is constructed by recursively hashing pairs of nodes until there is only 1.

You can check if any 1 data element is included in the tree with at most: `2log(n)`

    HAB = SHA256(SHA256(HA + HB))

> An even number of leaf nodes is required

More detailed info in the book...

#### Bitcoins Test Blockchains

* `mainnet` - 3rd Jan 2009
* `testnet`
* `segnet`
* `regnet`

Testnet is the name of the test blockchain, network and currency.
It is a fully featured live P2P - wallet, testcoins  and mining.

Testnet mining should remain easy and coins should be worthless

Protecting from monetary loss and protects the network from bugs

Every now and then the testnet gets scraped.

The current iteration is `testnet3`

##### Using testnet

Run it with:

    bitcoind -testnet

or set `testnet=1` in `bitcoin.conf`

#### Segnet: Segregated Witness Testnet

Special purpose: development and testing - single purpose

#### Regtest: The local blockchain

A local blockchain for testing purposes
Intended to be run on local systems

    bitcoind -regtest
    
of

    regtest=1

Can generate blocks with

    bitcoin-cli -regtest generate 500

## 10. Mining and Consensus

The primary incentive for mining is the block reward.
Mining underpins the decentralised clearing house by which transactions are validated.
Mining makes bitcoin special - a decentralised security mechanism which is the basis for P2P digital cash.

> Mining secures the bitcoin network and enabled the emergence of network-wide consensus without a central authority

The reward of newly minted coin and transaction fees - aligns the actions of miners and security.

Miners validate new transactions and record them on the global ledger.
A block is mined every 10 minutes.

Transactions that are part of the block are considered confirmed.

Miners compete to solve a difficult mathemtical problem.
The solution to the problem is called _proof-of-work_ - proof that a miner has expended significant computing effort.

The _mining_ term is used to mimic the diminishing returns from real mining.
The maximum amount of bitcoin mining (coinbase transaction) can add to money supply halves every 4 years (or 210000 blocks)

* January 2009: 50
* November 2012: 25
* July 2016: 12.5
* May 2020: 6.25
* Expected next halving Feb 2024: 3.125

Until 2140 were 20.99999998 million will have been mined

More info on the [halving history](https://cryptoanswers.com/faq/bitcoin-halving-dates-history/)

After 2140 - mining will only be incentivised by transaction fees.

> A miner may intentionally mine a block taking less than a full reward - such blocks have already been mined.

Bitcoin cannot be inflated like central bank (and commercial bank) money printing - credit creation.

> Deflationary money - money has more purchasing power over time.

Inflation is a slow but inevitable debasement of currency.
A hidden tax - punishing savers to bail out debtors.

### Decentralised consensus

> Satoshi Nakamoto’s main invention is the decentralized mechanism for emergent consensus

Emergent as there is no election or fixed moment when consensus occurs.
Consensus arises through asynchronous interaction of thousands of independent nodes - all following simple rules.

Four processes:

* Independent verification by every full node
* Independent aggregation of transactions into new blocks by mining nodes coupled with proof-of-work
* Independent verification of new blocks and assembly into block chain
* Independent selection of the chain with the most cumulative computational proof-of-work

#### Independent Verification of Transactions

Wallet software collects the UTXO, provides the ppropropriate unlocking scripts and constructs the new outputs.
The transaction is sent to neighbouring nodes to propogate across the bitcoin network.

Before propagating - each node verifies the transaction. Invalid transactions are not propagated.

Checklist:

* transaction syntax and data structure must be correct
* neither list of inputs or outputs is empty
* transaction block size is less than `MAX_BLOCK_SIZE`
* each output must be more than `DUST` and less than 21m
* No inputs have `0` or `-1` - coinbase transactions are not relayed
* `nLockime` is equal to `INT_MAX`. `nLocktime` and `nSequence` are satisfied according to `MedianTimePast`
* Transation size in bytes is >= 100 bytes
* ...etc more in the book

#### Mining Nodes

> The competition among miners effectively ends with the propagation of a new block that acts as an announcement of a winner. To miners, receiving a valid new block means someone else won the competition and they lost.

#### Aggregating Transactions into blocks

After validating tranasctions they are added to the memory pool.
Transactions wait until the are included in a block.

The miners after getting confirmed block - will remove the transations in that block from the memory pool.
The miner creates a _candidate block_.

The first transaction in every block is a `coinbase transaction` - containing the reward for mining effort.
Coinbase transactions do not consume utxo as an input.

Sum of transaction fees + block reward

Jing rewarding himself more than 25 btc would result in other nodes not accepting

#### Header

Six fields:

* version (4 bytes) 
* previous block hash (32 bytes)
* merkle root (32 bytes)
* timestamp (4 bytes)
* target (4 bytes) - proof of work algorithm target
* nonce (4 bytes) - counter used for the proof-of-work algorithm

> The miners node votes on the longest-difficulty valid chain by selecting the previous block hash

Add the coinbase transaction as the first transaction and ensure there is an even number of leaf nodes in the tree to construct the merkle root

The miner will add the unix epoch timestamp (number of seconds since 1970..)

The target is then set - the required proof-of-work to make it a valid block.

mantissa-exponent encoding - a 1-byte exponent and a 3-byte coefficinet (mantissa)

The nonce is initialised to 0.

With these fields filled, the mining can begin...

The goal is now to find a value for the nonce that results in a block header hash that is less than the target.
The mining node will have to test billions or trillions of nonces before a nonce is found that satisfies the requirement.

Mining is the process of hashing the block header repeatedly - changing 1 paramter until the resulting hash matches a specific target.
The hash function's result cannot be determined in advance - hashes are one way.
So you have to brute force and try.

Modifying the nonce until the desired hash appears.

> A hash algorithm takes an arbitrary length data input and produces a fixed length deterministic result - a digital fingerprint for the input.

For the same input the result will always be the same.

It is computationally infeasible to find a _collision_ - finding two different inputs that create the same output (fingerprint).

The output of SHA256 is always 256 bits long

Example with python

    import hashlib

    TEXT = "I am Satoshi Nakamoto"
    line = TEXT.encode('utf-8')

    result = hashlib.sha256(line).hexdigest()
    print(result)

Running:

    $ python sha256.py 
    5d7c7ba21cbbcd75d14800b100252d5b428e5b1213d27c385bc141ca6b47989e

Changing the input will create a different hash

Adding a number from 1 to 20 on each line creates:

    I am Satoshi Nakamoto0 => a80a81401765c8eddee25df36728d732acb6d135bcdee6c2f87a3784279cfaed
    I am Satoshi Nakamoto1 => f7bc9a6304a4647bb41241a677b5345fe3cd30db882c8281cf24fbb7645b6240
    I am Satoshi Nakamoto2 => ea758a8134b115298a1583ffb80ae62939a2d086273ef5a7b14fbfe7fb8a799e
    I am Satoshi Nakamoto3 => bfa9779618ff072c903d773de30c99bd6e2fd70bb8f2cbb929400e0976a5c6f4
    I am Satoshi Nakamoto4 => bce8564de9a83c18c31944a66bde992ff1a77513f888e91c185bd08ab9c831d5
    I am Satoshi Nakamoto5 => eb362c3cf3479be0a97a20163589038e4dbead49f915e96e8f983f99efa3ef0a
    I am Satoshi Nakamoto6 => 4a2fd48e3be420d0d28e202360cfbaba410beddeebb8ec07a669cd8928a8ba0e
    I am Satoshi Nakamoto7 => 790b5a1349a5f2b909bf74d0d166b17a333c7fd80c0f0eeabf29c4564ada8351
    I am Satoshi Nakamoto8 => 702c45e5b15aa54b625d68dd947f1597b1fa571d00ac6c3dedfa499f425e7369
    I am Satoshi Nakamoto9 => 7007cf7dd40f5e933cd89fff5b791ff0614d9c6017fbe831d63d392583564f74
    I am Satoshi Nakamoto10 => c2f38c81992f4614206a21537bd634af717896430ff1de6fc1ee44a949737705
    I am Satoshi Nakamoto11 => 7045da6ed8a914690f087690e1e8d662cf9e56f76b445d9dc99c68354c83c102
    I am Satoshi Nakamoto12 => 60f01db30c1a0d4cbce2b4b22e88b9b93f58f10555a8f0f4f5da97c3926981c0
    I am Satoshi Nakamoto13 => 0ebc56d59a34f5082aaef3d66b37a661696c2b618e62432727216ba9531041a5
    I am Satoshi Nakamoto14 => 27ead1ca85da66981fd9da01a8c6816f54cfa0d4834e68a3e2a5477e865164c4
    I am Satoshi Nakamoto15 => 394809fb809c5f83ce97ab554a2812cd901d3b164ae93492d5718e15006b1db2
    I am Satoshi Nakamoto16 => 8fa4992219df33f50834465d30474298a7d5ec7c7418e642ba6eae6a7b3785b7
    I am Satoshi Nakamoto17 => dca9b8b4f8d8e1521fa4eaa46f4f0cdf9ae0e6939477e1c6d89442b121b8a58e
    I am Satoshi Nakamoto18 => 9989a401b2a3a318b01e9ca9a22b0f39d82e48bb51e0d324aaa44ecaba836252
    I am Satoshi Nakamoto19 => cda56022ecb5b67b2bc93a2d764e75fc6ec6e6e79ff6c39e21d03b45aa5b303a

For a challenge find an input that results in a hash starting with 0.

The probabilities is 1 in 16. One out of 16 possible hexadecimal values.

So we want to find a value less than a specific target: `0x100000000000000...`

Decreasing the target makes finding a hash more difficult.

Since SHA256 is deterministic - the inputs themselves provide proof that a certain amount of work has been done.

It only takes 1 hash to verify - it takes many to attempt and find the correct.

Example proof of work code (python 3):

    import hashlib
    import time

    max_nonce = 2 ** 32 # 4 billion

    def proof_of_work(header, difficulty_bits):

        # calculate the difficulty target
        target = 2 ** (256-difficulty_bits)

        for nonce in range(max_nonce):
            line = str(header) + str(nonce)
            line = line.encode('utf-8')
            hash_result = hashlib.sha256(line).hexdigest()

            # check if this is a valid result, below the target
            if int(hash_result, 16)  < target:
                print(f"Success with nonce {nonce}")
                print(f"Hash is {hash_result}")
                return (hash_result,nonce)

        print(f"Failed after {nonce} (max_nonce) tries")

        return nonce


    if __name__ == '__main__':
        nonce = 0
        hash_result = ''

        # difficulty from 0 to 31 bits
        for difficulty_bits in range(32):

            difficulty = 2 ** difficulty_bits
            print(f"Difficulty: { difficulty } ({ difficulty_bits } bits)")

            print("Starting search...")

            # checkpoint the current time
            start_time = time.time()

            # make a new block which includes the hash from the previous”
            # we fake a block of transactions - just a string
            new_block = 'test block with transactions' + hash_result

            # find a valid nonce for the new block
            (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

            # checkpoint how long it took to find a result
            end_time = time.time()

            elapsed_time = end_time - start_time
            print(f"Elapsed Time: { elapsed_time:.4f} seconds")

            if elapsed_time > 0:
                # estimate the hashes per second
                hash_power = float(int(nonce)/elapsed_time)
                print(f"Hashing Power: { hash_power } hashes per second")

Output:

    $ python proof_of_work.py 
    Difficulty: 1 (0 bits)
    Starting search...
    Success with nonce 0
    Hash is ff8253ed10b5f719d52a709a66af8cd5e2054f702e675af4ca0cae70f0988634
    Elapsed Time: 0.0001 seconds
    Hashing Power: 0.0 hashes per second

    Difficulty: 2 (1 bits)
    Starting search...
    Success with nonce 0
    Hash is 22c608547e239faf5c353e7ebd204042760b93891d1d0be9ab488d36c73c077b
    Elapsed Time: 0.0001 seconds
    Hashing Power: 0.0 hashes per second

    ...

    Difficulty: 16 (4 bits)
    Starting search...
    Success with nonce 25
    Hash is 0f7becfd3bcd1a82e06663c97176add89e7cae0268de46f94e7e11bc3863e148
    Elapsed Time: 0.0002 seconds
    Hashing Power: 140559.7855227882 hashes per second

    Difficulty: 32 (5 bits)
    Starting search...
    Success with nonce 36
    Hash is 029ae6e5004302a120630adcbb808452346ab1cf0b94c5189ba8bac1d47e7903
    Elapsed Time: 0.0003 seconds
    Hashing Power: 113958.44830188679 hashes per second

    Difficulty: 64 (6 bits)
    Starting search...
    Success with nonce 0
    Hash is 0083214fa878cea749bd07bd77e92b311be876dd72f3d4924d5ae4ead54febe5
    Elapsed Time: 0.0000 seconds
    Hashing Power: 0.0 hashes per second

    Difficulty: 128 (7 bits)
    Starting search...
    Success with nonce 26
    Hash is 00f7abab177613afc42270e3f5f79ffddd694093030663b32fe26ce2a377a993
    Elapsed Time: 0.0004 seconds
    Hashing Power: 65144.506571087215 hashes per second

    ...

    Difficulty: 4096 (12 bits)
    Starting search...
    Success with nonce 2933
    Hash is 00034d0888fb1cc74a4ee823eae4b71d8949e453da89f24caf3088b557f241c2
    Elapsed Time: 0.0128 seconds
    Hashing Power: 229843.12598322215 hashes per second

    Difficulty: 8192 (13 bits)
    Starting search...
    Success with nonce 2142
    Hash is 00014006170118b30d97b81e4a824357d416866b469dfc56d16db31e5486f5a0
    Elapsed Time: 0.0056 seconds
    Hashing Power: 381397.48548140604 hashes per second

    ...

    Difficulty: 1048576 (20 bits)
    Starting search...
    Success with nonce 237723
    Hash is 000005720acd8c7207cbf495e85733f196feb1e3692405bea0ee864104039350
    Elapsed Time: 0.5729 seconds
    Hashing Power: 414943.95798467955 hashes per second

    Difficulty: 2097152 (21 bits)
    Starting search...
    Success with nonce 687438
    Hash is 000003a6eeee97491a9183e4c57458172edb6f9466377bf44afbd74e410f6eef
    Elapsed Time: 1.5574 seconds
    Hashing Power: 441400.44823243807 hashes per second

    Difficulty: 4194304 (22 bits)
    Starting search...
    Success with nonce 1759164
    Hash is 0000008bb8f0e731f0496b8e530da984e85fb3cd2bd81882fe8ba3610b6cefc3
    Elapsed Time: 3.8199 seconds
    Hashing Power: 460523.1693950422 hashes per second

    Difficulty: 8388608 (23 bits)
    Starting search...
    Success with nonce 14214729
    Hash is 000001408cf12dbd20fcba6372a223e098d58786c6ff93488a9f74f5df4df0a3
    Elapsed Time: 33.4262 seconds
    Hashing Power: 425257.7266276793 hashes per second

    Difficulty: 16777216 (24 bits)
    Starting search...
    Success with nonce 24586379
    Hash is 0000002c3d6b370fccd699708d1b7cb4a94388595171366b944d68b2acce8b95
    Elapsed Time: 57.4016 seconds
    Hashing Power: 428321.8702630346 hashes per second

    Difficulty: 33554432 (25 bits)
    Starting search...
    Success with nonce 8570323
    Hash is 00000009ecccb8289d6f94b3e861804e41c4530b0f879534597ff4d09aaa446d
    Elapsed Time: 19.8435 seconds
    Hashing Power: 431896.1929701366 hashes per second

> Increasing the difficulty by 1 bit doubles the time it takes to find a solution

You decrease the search space by half

We can get the current difficulty with:

    ubuntu@btc:~$ bitcoin-cli getblockcount
    694607
    ubuntu@btc:~$ bitcoin-cli getblockhash 694607
    000000000000000000051c83e30b6237c15eeea0c37a4624af91ccf84c1b9da7
    ubuntu@btc:~$ bitcoin-cli getblock 000000000000000000051c83e30b6237c15eeea0c37a4624af91ccf84c1b9da7
    
        "time": 1628327707,
        "mediantime": 1628322307,
        "nonce": 753841039,
        "bits": "17136aa2",
        "difficulty": 14496442856349.12,

So the `bits` is the target. 

The target that the new hash must meet is below: `387148450` (17136aa2)
The current block nonce was below `0x2ceeb38f` (753841039)

#### Adjustable difficulty

Why is it adjustable and who adjusts it?

> Bitcoin’s blocks are generated every 10 minutes, on average. This is bitcoin’s heartbeat and underpins the frequency of currency issuance and the speed of transaction settlement.

Computer power varies over time (as well as miners forced offline like in China)

To keep the block generation time at 10 minutes - the difficulty of mining must be adjusted

How is it done on a decentralised network: Retargeting occurs automatically and on every node independently

> Every 2,016 blocks, all nodes retarget the Proof-of-Work.

> The equation for retargeting measures the time it took to find the last 2,016 blocks and compares that to the expected time of 20,160 minutes (2,016 blocks times the desired 10-minute block interval). The ratio between the actual timespan and desired timespan is calculated and a proportionate adjustment (up or down) is made to the target. In simple terms: If the network is finding blocks faster than every 10 minutes, the difficulty increases (target decreases). If block discovery is slower than expected, the difficulty decreases (target increases).

    New Target = Old Target * (Actual Time of Last 2016 Blocks / 20160 minutes)

There was an off by 1 error - basing it on the previous 2015 blocks not 2016. Biasing towards a high difficulty by 0.05%.

The adjustment factor maxes out at `4`

Hashing power is independent of transactions and adoption. 

The difficulty of mining is related to the cost of electricity.
The price of 1 kilowatt hour is important.

The nonce entered by the miner - creates a block hash lower than the target.
The block is then propagated to peers.
Dishonest miners will have their blocks rejected.

> The “main chain” at any time is whichever valid chain of blocks has the most cumulative Proof-of-Work associated with it. Under most circumstances this is also the chain with the most blocks in it

In a blockchain fork - the chain with the most cumulative proof-of-work is selected.

> By selecting the greatest-cumulative-work valid chain, all nodes eventually achieve network-wide consensus.

#### Forks

The losing chain is kept. 

> Forks are almost always resolved within 1 block

So the mining power splits. The winning miner of the next block has selected the winner.
The losing miners - will have to reconverge the other blocks in.

> Bitcoin’s block interval of 10 minutes is a design compromise between fast confirmation times (settlement of transactions) and the probability of a fork.

### Mining and the Hashing Race

Very competitive.
* 2010 - 2011: miners moved from CPU to GPU
* 2013: ASIC mining - placing SHA256 on silicon chips

The industry has reached the forefront of Moore's law.

> It’s no longer about how much mining can be done with one chip, but how many chips can be squeezed into a building, while still dissipating the heat and providing adequate power.

The speed of hashing overtook 4GH/s meaning all 4billion possible results of a nonce were tested in less than a second - before the timestamp changed.
The timestamp could be stretched - but could result in blocks becoming invalid.
Miners started sing the coinbase script - as nonce.
Giving miners more room for change within the second.

Mining pools allow offset of costs - with regular payments.

Mining pools set a target higher than bitcoin's - so contributors can prove they are doing work.
Miners pool on a stratum network.

P2Pool - peer-to-peer mining

### Consensus Attacks

There needs to be a majority of miners acting out of self interest.

> It is important to note that consensus attacks can only affect future consensus, or at best, the most recent past (tens of blocks).

With a 51% attack - deliberate forks can be created to double spend or execute denial of service - against specific transactions or requests.

More in the book on consensus, hard forks and soft forks...

## 11. Bitcoin Security

Possession of the keys to unlock the bitcoin is equivalent to possession of cash or a chunk of precious metal. You can lose it, misplace it, have it stolen, or accidentally give the wrong amount to someone. In every one of these cases, users have no recourse, just as if they dropped cash on a public sidewalk.

> However, bitcoin has capabilities that cash, gold, and bank accounts do not. A bitcoin wallet, containing your keys, can be backed up like any file. It can be stored in multiple copies, even printed on paper for hard-copy backup.

### Security Principles

Decentralisation pushes responsibility to the users.

> A bitcoin transaction authorizes only a specific value to a specific recipient and cannot be forged or modified. It does not reveal any private information, such as the identities of the parties, and cannot be used to authorize additional payments. Therefore, a bitcoin payment network does not need to be encrypted or protected from eavesdropping.

Bitcoin’s decentralized security model puts a lot of power in the hands of the users. With that power comes responsibility for maintaining the secrecy of the keys.

In simple terms: don’t take control of keys away from users and don’t take transactions off the blockchain.

#### The Root of Trust

> Traditional security architecture is based upon a concept called the root of trust, which is a trusted core used as the foundation for the security of the overall system or application.

> The more complex a software system becomes, the harder it is to secure

A correctly validated blockchain uses the genesis block as the root of trust, building a chain of trust up to the current block.

#### User security best practices

Human experience with digital security is only 50 years old...

> Modern general-purpose operating systems are not very secure and not particularly suited to storing digital money

Our computers are constantly exposed to external threats via always-on internet connections.

> The level of computer maintenance required to keep a computer virus-free and trojan-free is beyond the skill level of all but a tiny minority of computer users.

#### Physical Bitcoin Storage

Bitcoin keys are nothing more than long numbers. This means that they can be stored in a physical form, such as printed on paper or etched on a metal coin.

> I personally keep the vast majority of my bitcoin (99% or more) stored on paper wallets, encrypted with BIP-38, with multiple copies locked in safes. Keeping bitcoin offline is called cold storage and it is one of the most effective security techniques.

#### Hardware Wallets

Without general-purpose software to compromise and with limited interfaces, hardware wallets can deliver an almost foolproof level of security to nonexpert users.

### Balancing Risk

> In the effort to secure their bitcoin wallets, users must be very careful not to go too far and end up losing the bitcoin. In July 2011, a well-known bitcoin awareness and education project lost almost 7,000 bitcoin. In their effort to prevent theft, the owners had implemented a complex series of encrypted backups. In the end they accidentally lost the encryption keys, making the backups worthless and losing a fortune.

### Multisig

Large amounts should be stored with a multisignature bitcoin address.

Survivability - incapacity or death of the key holder

**Chapter was very short with little to no specific details**

## 12. Bitcoin Applications

Nowadays many people misuse the term _blockchain_

Building blocks:

* No double-spend
* Immutability
* Neutrality
* Secure timestamping
* Authorization - digital signatures
* Auditability
* Accounting - not possible to create or destroy bitcoin outside of coinbase transactions
* Nonexpiration
* Intergrity
* Atomicity - transaction is valid or not. mined or not.
* Indivisible - units of value
* Quorum of control - multisig
* Timelock / Aging
* Replication
* FOrgery Protection
* Consistency
* Preditable issuance - no more than 21 million

### Coloured coins

recording ownership of assets outside of bitcoin

[open assets](https://github.com/OpenAssets)

### Counterparty

The ability to trade in virtual assets

### State Channels

More in the book...

### Routed Payment Channels (Lightning Network)

More in the book...

## 13. TO DO

* Read bitcoin whitepaper








### Using the CLI

Check info

    bitcoind -printtoconsole

Will print your bitcoin version and SSL library you are using.

You can get any transactoin with: `getrawtransaction`

To get the runtime status:

    bitcoin-cli getinfo



## Source

* [Mastering Bitcoin - Andreas M. Antonopoulos](https://aantonop.com/)
