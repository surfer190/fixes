---
author: ''
category: Bitcoin
date: '2021-08-12'
summary: ''
title: Learning Bitcoin from the Command Line Notes
---

# Notes on Learning-Bitcoin-from-the-Command-Line

The [github repo](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line) is the correct starting place for this.

These are just my notes.

## 3.1: Verifying Your Bitcoin Setup

### Get Testnet Blockheight

    $ http https://blockstream.info/testnet/api/blocks/tip/height
    HTTP/1.1 200 OK
    Access-Control-Allow-Origin: *
    Access-Control-Expose-Headers: x-total-results
    Alt-Svc: clear
    Content-Length: 7
    Content-Type: text/plain
    Date: Thu, 12 Aug 2021 16:38:34 GMT
    Server: nginx
    Via: 1.1 google
    cache-control: public, max-age=10

    2064516

### Get Mainnet Blockheigh

    $ http https://blockstream.info/api/blocks/tip/height
    HTTP/1.1 200 OK
    Access-Control-Allow-Origin: *
    Access-Control-Expose-Headers: x-total-results
    Age: 5
    Alt-Svc: clear
    Cache-Control: public, max-age=10
    Content-Length: 6
    Content-Type: text/plain
    Date: Thu, 12 Aug 2021 16:43:42 GMT
    Server: nginx
    Via: 1.1 google

    695439

Which corresponds to my node:

    ubuntu@btc:~$ bitcoin-cli getblockcount
    695439

## 3.2: Knowing Your Bitcoin Setup

### Know Your Bitcoin Directory

Everything is in `~/.bitcoin`:

    ubuntu@btc:/mnt/btc/bitcoin$ ls 
    banlist.dat   chainstate  fee_estimates.dat  peers.32fd     wallet.dat
    bitcoin.conf  database    indexes            peers.39ca
    bitcoind.pid  db.log      mempool.dat        peers.dat
    blocks        debug.log   mytestwallet       settings.json

* `blocks` and `chainstate` contains the blockchain data

Config for testnet is in `~/.bitcoin/testnet3` and regtest is in `~/.bitcoin/regtest`

### Know your bitcoin info

    $ bitcoin-cli getblockchaininfo
    $ bitcoin-cli getmininginfo
    $ bitcoin-cli getnetworkinfo
    $ bitcoin-cli getnettotals
    $ bitcoin-cli getwalletinfo

## 3.3: Setting Up Your Wallet

### Create an Address

There are 3 types: `legacy`, `p2sh-segwit` and the default `bech32`

    Example:

    $ bitcoin-cli getnewaddress -addresstype legacy
    moKVV6XEhfrBCE3QCYq6ppT7AaMF8KsZ1B

A mainnet address would start with a "1" (for Legacy), "3" (for P2SH), or "bc1" (for Bech32).

A testnet address would start with "m" (or sometimes an "n") (for Legacy), "2" (for P2SH) or "tb1" (for Bech32)

    ubuntu@btc:~$ bitcoin-cli help getnewaddress
    getnewaddress ( "label" "address_type" )

    Returns a new Bitcoin address for receiving payments.
    If 'label' is specified, it is added to the address book 
    so payments received with the address will be associated with 'label'.

    Arguments:
    1. label           (string, optional, default="") The label name for the address to be linked to. It can also be set to the empty string "" to represent the default label. The label does not need to exist, it will be created if there is no label by the given name.
    2. address_type    (string, optional, default=set by -addresstype) The address type to use. Options are "legacy", "p2sh-segwit", and "bech32".

    Result:
    "str"    (string) The new bitcoin address

    Examples:
    > bitcoin-cli getnewaddress 
    > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "getnewaddress", "params": []}' -H 'content-type: text/plain;' http://127.0.0.1:8332/

> What is a Bitcoin address? A Bitcoin address is literally where you receive money. It's like an email address, but for funds. Technically, it's a public key, though different address schemes adjust that in different ways. However unlike an email address, a Bitcoin address should be considered single use: use it to receive funds just once.

> What is a Bitcoin wallet? By creating your first Bitcoin address, you've also begun to fill in your Bitcoin wallet. More precisely, you've begun to fill the `wallet.dat`. The `wallet.dat` file contains data about preferences and transactions, but more importantly it contains all of the key pairs that you create: both the public key (which is the source of the address where you receive funds) and the private key (which is how you spend those funds). For the most part, you won't have to worry about that private key: bitcoind will use it when it's needed. However, this makes the wallet.dat file extremely important: if you lose it, you lose your private keys, and if you lose your private keys, you lose your funds!

### Sign a Message

Prove that you control the private key linked to an address (in quotes below), creating a digital signature:

    bitcoin-cli signmessage "moKVV6XEhfrBCE3QCYq6ppT7AaMF8KsZ1B" "Hello, World"
    HyIP0nzdcH12aNbQ2s2rUxLwzG832HxiO1vt8S/jw+W4Ia29lw6hyyaqYOsliYdxne70C6SZ5Utma6QY/trHZBI=

The other party can verify the digital signature with:

    $ bitcoin-cli verifymessage "moKVV6XEhfrBCE3QCYq6ppT7AaMF8KsZ1B" "HyIP0nzdcH12aNbQ2s2rUxLwzG832HxiO1vt8S/jw+W4Ia29lw6hyyaqYOsliYdxne70C6SZ5Utma6QY/trHZBI=" "Hello, World"
    true

### Dump your Wallet

Make a backup of your wallet:

    bitcoin-cli dumpwallet ~/mywallet.txt

> The `mywallet.txt` file in your home directory will have a long list of private keys, addresses, key paths and other information. It is a `HD wallet` - hierachical deterministic wallet.

You can recover it with:

    bitcoin-cli importwallet ~/mywallet.txt

> But note this requires an unpruned node!

### View Your Private Keys

Sometimes, you might want to actually look at the private keys associated with your Bitcoin addresses. Perhaps you want to be able to sign a message or spend bitcoins from a different machine. Perhaps you just want to back up certain important private keys.

    $ bitcoin-cli dumpprivkey "moKVV6XEhfrBCE3QCYq6ppT7AaMF8KsZ1B"
    cTv75T4B3NsG92tdSxSfzhuaGrzrmc1rJjLKscoQZXqNRs5tpYhH

You can import a key with:

    bitcoin-cli importprivkey cW4s4MdW7BkUmqiKgYzSJdmvnzq8QDrf6gszPMC7eLmfcdoRHtHh

## 3.4: Receiving a Transaction

Get your balance

    bitcoin-cli getbalance
    0.00000000

> The tranasctions have not been recorded yet

You can get your balance from unconfirmed transactions with:

    bitcoin-cli getunconfirmedbalance
    0.00000000

Check the balance is more than `n` blocks deep:

    bitcoin-cli getbalance * 6

Get wallet info:

    ubuntu@testnet:~/.bitcoin$ bitcoin-cli getwalletinfo
    {
        "walletname": "mytestwallet",
        "walletversion": 169900,
        "format": "bdb",
        "balance": 0.00000000,
        "unconfirmed_balance": 0.00000000,
        "immature_balance": 0.00000000,
        "txcount": 0,
        "keypoololdest": 1629017788,
        "keypoolsize": 0,
        "hdseedid": "a72cd71a3976664fc8cb3959799b26e0f1f0c2b1",
        "keypoolsize_hd_internal": 0,
        "paytxfee": 0.00000000,
        "private_keys_enabled": true,
        "avoid_reuse": false,
        "scanning": false,
        "descriptors": false
    }

Discover transactions:

See how your wallet has received money

    bitcoin-cli listtransactions

Show just your unspect transactions:

    bitcoin-cli listunspent

Examine your transactions (verbosely):

    bitcoin-cli gettransaction <tx_id> false true

## 4.0 Sending Bitcoin Transactions

Options:

* `sendtoaddress`


### 4.1: Sending Coins the Easy Way

It is important to think about the transaction fee before starting your transaction.

In `~/.bitcoin/bitcoin.conf` you can set:

    # Set min fee at 10000 satoshis per kilobyte
    mintxfee=0.0001
    # Confirm floating fees from the last 6 blocks
    txconfirmtarget=6

> restart bitcoin for this to take effect: `bitcoin-cli stop` and `bitcoind -daemon`

Now you jsut need to send the amount:

Use:

    bitcoin-cli sendtoaddress [address] [amount]

It will respond with a `tx_id`, use this with `getrawtransaction` to view the tranasction.

Advantages of `sendtoaddress`:

* It works out the fees for you
* It works out the change address (since you must spend all of your bitcoin at once, then return change to an address you control)

### 4.2: Creating a Raw Transaction

Craft the transaction the exact way you want it.

#### List your unspent transactions

    bitcoin-cli listunspent

To know how much `utxo` you have on hand to spend.

> When you want to spend a UTXO, it's not sufficient to just know the transaction id. That's because each transaction can have multiple outputs! You need to know the `vout` of the transaction.

    txid+vout=UTXO

**WARNING: It is very easy to lose money with a raw transaction.**

#### Write a Raw Transaction with One Output

> If you mess up the recipient, the money is gone. One mistake and it could mean everything gone.

Fee is also calculated based on the size of the transacion...difficult to work out and get right.

Set cli variables for your requirements:

    utxo_txid="61f3b7016bf1ecc3987b8805207e79362e4de8026682e149107999b779426e3a"
    utxo_vout="1"
    recipient="n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi"
    
> double check them

    echo $utxo_txid
    echo $utxo_vout
    echo $recipient

Here is the format:

    bitcoin-cli createrawtransaction
    '''[
        {
        "txid": "'$your_txid'",
        "vout": '$your_vout'
        }
    ]'''
    '''{
    "'$your_recipient'": bitcoin_amount
    }'''

Create the transaction (as hex):

    rawtxhex=$(bitcoin-cli createrawtransaction '''[ { "txid": "'$utxo_txid'", "vout": '$utxo_vout' } ]''' '''{ "'$recipient'": 0.0004 }''')
    echo $rawtxhex

Verify the transaction:

    bitcoin-cli decoderawtransaction $rawtxhex

#### Sign the transaction

    bitcoin-cli signrawtransactionwithwallet $rawtxhex

#### Send the transaction

    bitcoin-cli sendrawtransaction $signedtx

> You'll immediately see that the UTXO and its money have been removed from your wallet with `bitcion-cli listunspent`

> Soon `bitcoin-cli listtransactions` should show the confirmed transaction

Using [JQ](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/04_2__Interlude_Using_JQ.md)

### 4.3 Creating a Raw Transaction with Named Arguments

More on this at [Creating a Raw Transaction with Named Arguments](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/04_3_Creating_a_Raw_Transaction_with_Named_Arguments.md)

### 4.4 Sending Coins with Raw Transactions

More on this at [Sending Coins with Raw Transactions](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/04_4_Sending_Coins_with_a_Raw_Transaction.md)

### 4.5 Sending Coins with Automated Raw Transactions

More on this at [Sending Coins with Automated Raw Transactions](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/04_5_Sending_Coins_with_Automated_Raw_Transactions.md)


### 4.6 Creating a SegWit Transaction

More on this at [Creating a SegWit Transaction](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/04_6_Creating_a_Segwit_Transaction.md)

Everything really gets too complex from here....

## 14. Using Tor

#### What is Tor?

Tor is a low-latency anonymity and overlay network based on onion routing and path-building design for enabling anonymous communication. It's free and open-source software with the name derived from the acronym for the original software project name: "The Onion Router".

#### Why Use Tor for Bitcoin?

The Bitcoin network is a peer-to-peer network that listens for transactions and propagates them using a public IP address. When connecting to the network not using Tor, you would share your IP address, which could expose your location, your uptime, and others details to third parties — which is an undesirable privacy practice. To protect yourself online you should use tools like Tor to hide your connection details. Tor allows improve your privacy online as your data is cryptographically encoded and goes through different nodes, each one decoding a single layer (hence the onion metaphor).

### Understand Tor

* When a user wants to connect to an Internet server, Tor tries to build a path formed by at least three Tor nodes relays, called Guard, Middle, and Exit.
* While building this path, symmetric encryption keys are negotiated; when a message moves along the path, each relay then strips off its layer of encryption. In this way, the message arrives at the final destination in its original form, and each party only knows the previous and the next hop and cannot determine origin or destination.
* Tor encrypts your data in such a way that it hides your origin, your destination, and what services you're using, whereas a standard encryption protocol like TLS only protects what your data contains.

### Tor Architecture

* _Tor Client_ (OP or Onion Proxy). A Tor client installs local software that acts as an onion proxy. It packages application data into cells that are all the same size (512 bytes), which it then sends to the Tor network. A cell is the basic unit of Tor transmission.
* _Onion Node_ (OR or Onion Router). An onion node transmits cells coming from the Tor client and from online servers. There are three types of onion nodes: input (Guard), intermediate nodes (Middle), and output nodes (Exit).
* _Directory Server_. A Directory server stores information about onion routers and onion servers (hidden services), such as their public keys.
* _Onion Server_ (hidden server). An onion server supports TCP applications such as web pages or IRC as services.

### Tor Limitations

* Tor isn't a perfect tool. Because information from the Tor network is decrypted at the exit nodes before being sent to its final destinations, theoretically an observer could collect sufficient metadata to compromise anonymity and potentially identify users.

I am not convinced at this stage that I need it.
