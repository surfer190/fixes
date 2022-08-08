---
author: ''
category: Bitcoin
date: '2022-01-31'
summary: ''
title: Self-Hosted Python Based Bitcoin Payment Processors
---

# A Guide on Self-hosted Python Based Bitcoin Payment Processors

From what I have seen the _go to_ payment processor is:

* [BTC Pay Server](https://btcpayserver.org/) **3.7k stars on github**

Python based processors I found:

* [Bitcart CC](https://bitcartcc.com/) **158** stars
* [SatSale](https://github.com/nickfarrow/SatSale) **142** stars
* [CypherpunkPay](https://cypherpunkpay.org/) **46** stars - no longer active

All these providers are:

* Open-source
* Do not rely on a third party

#### Don't want to Run your Own?

These devices were recommended if you don't want to run your own:

* [lightning in a box](https://lightninginabox.co/product/lightning-in-a-box/)
* [hack(0)](https://www.dglab.com/en/works/hack0)
* [nodl.it](https://www.nodl.it/)

## Bitcart CC

Read up for yourself [Bitcart CC Docs](https://docs.bitcartcc.com/)

* Process payments as a merchant
* A full invoicing system
* Consists of: Bitcart API, Bitcart admin and bitcart store front
* Can also just do ad hoc stuff with the [Bitcart CC SDK](https://sdk.bitcartcc.com/en/latest/)
* Has a bitcart-cli
* Supports various crypto shitcoins and Bitcoin (I am bitcoin only)
* Wallet you use must support `xpub` (Full BIP32). Bitcoin-core does not support `xpub` and hence you cannot use that wallet with BitcartCC
* Notifications for payments received on various platforms, intergration with ecommerce
* Hard to add a donate button
* Lots of good documentation
* Lead developer is always available and on telegram
* Works! (I tested on bitcoin testnet)

Features:

* The invoice is a fresh address from your wallet that wasn't used before
* Uses the [Electrum wallet](https://electrum.org/#home) protocol and it's SPV (Simple Payment Verification)
* Highly modular - just use the parts you need

### How it keeps funds secure

1. For each invoice, BitcartCC generates a new address, belonging to the xpub entered, and this address is presented to the user.
2. As this address is your wallet's address, you receive the funds directly.
3. BitcartCC just watches the payments, it can't modify anything along the way, as when configuring the wallet - you enter a watch-only master public key.

### Manual Deployment

I deployed it on a Debian 9 (stretch) VM with:

* 1 vCPU
* 2 GB RAM
* 40 GB Disk

I followed the [manual installation docs](https://docs.bitcartcc.com/deployment/manual#typical-manual-installation)

### Docker Deployment

BitcartCC recommends the [docker deployment](https://docs.bitcartcc.com/deployment/docker) as it is easier and more consistent. You can give it a whirl.

There is also a [bitcartCC configurator](https://configurator.bitcartcc.com) for those that don't know what deployment method to use.

#### Verdict

* The project is fairly active and has a full-time dev working on it
* Architected in a modular way
* Does not require private keys or seed
* Still growing
* Gaining more stability

## Satsale

* Lightweight
* Bitcoin Only
* You must run a full node that satsale can connect to - a security concern for me mitigated by the use of SSH tunneling
* Docs are sparse - it is pretty much the readme on github
* Supports `xpub` but prefers use of your own bitcoin-core node
* No notification - must check bitcoin wallet
* No concept of an invoice - linking products to a bitcoin address
* It works (Tested with bitcoin testnet)

### Deployment

* Deployment is manual
* Will take longer and require a lot more understanding: setting up your own node, networking, ensuring security and knowledge of python
* Do it yourself - manual deploymeny.

### Verdict

* The project is gaining momentum
* Good solution for a donation only site
* Easy to link to on your website
* Sticks to bitcoin-core reference
* For the bitcoin maxi's
* No community channels to talk and get info

## Bonus Section: What is wrong with using a single static bitcoin address

* It links a bitcoin address to a real world identity (your website or portal receiving donations)
* You harm the privacy of people donating to you

> The internet is forever. Once an address is posted it will forever be linked to you. There are surveillance companies and security analysts always watching. An example is [OXT](https://oxt.me/notes)

An attacker can then know what you are spending the donations on.

Also people who have had their addresses exposed - donating to you will also have that information add to their profile.

## Sources

* [Awesome list of bitcoin payment processors](https://github.com/alexk111/awesome-bitcoin-payment-processors)
* [Why Bitcoin Static Addresses are Bad...](https://www.ministryofnodes.com.au/bitcoin-static-donation-addresses-suck)