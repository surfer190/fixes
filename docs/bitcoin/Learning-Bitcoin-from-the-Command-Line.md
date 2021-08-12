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











