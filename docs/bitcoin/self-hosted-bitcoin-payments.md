---
author: ''
category: Bitcoin
date: '2022-01-31'
summary: ''
title: Self-Hosted Python Based Bitcoin Payment Processors
---

# A Guide on Self Hosted Python Based Bitcoin Payment Processors

From what I have seen the go to payment processor is:

* [BTC Pay Server](https://btcpayserver.org/) **3.2k**

Python based processors I found:

* [Bitcart CC](https://bitcartcc.com/) **122** stars
* [SatSale](https://github.com/nickfarrow/SatSale) **101** stars
* [CypherpunkPay](https://cypherpunkpay.org/) **27** stars

Naturally these providers are:

* Open-source
* Do not rely on a third party

#### Don't want to Run your Own?

These devices were recommended if you don't want to run your own:

* [lightning in a box](https://lightninginabox.co/product/lightning-in-a-box/)
* [hack(0)](https://www.dglab.com/en/works/hack0)
* [nodl.it](https://www.nodl.it/)

## Bitcart CC

Read up for yourself [Bitcart CC Docs](https://docs.bitcartcc.com/)

Uses:

* Process payments as a merchant
* A full invoicing system
* Can also just do ad hoc stuff with the [Bitcart CC SDK](https://sdk.bitcartcc.com/en/latest/)

Features:

* The invoice is a fresh address from your wallet that wasn't used before
* Uses the [Electrum wallet](https://electrum.org/#home) protocol and it's SPV (Simple Payment Verification)
* Highly modular - just use the parts you need

### How it keeps funds secure

1. For each invoice, BitcartCC generates a new address, belonging to the xpub entered, and this address is presented to the user.
2. As this address is your wallet's address, you receive the funds directly.
3. BitcartCC just watches the payments, it can't modify anything along the way, as when configuring the wallet - you enter a watch-only master public key.

### Manual Deployment

I deployed a Ubuntu 20.04 VM with:

* 1 vCPU
* 1 GB RAM
* 25 GB Disk

As per the [installation docs](https://docs.bitcartcc.com/deployment/manual#typical-manual-installation):

Encounted 2 issues where `python-gino` needs:

    sqlalchemy<=1.4

As per [this discussion](https://github.com/python-gino/gino/discussions/765)

Also a more recent version of node is required - higher than that installed by the OS package manager:

    error eslint-plugin-jest@25.7.0: The engine "node" is incompatible with this module. Expected version "^12.13.0 || ^14.15.0 || >=16.0.0". Got "10.19.0"
error Found incompatible module.

Also there is a requirement for [secp256k1](https://github.com/bitcoin-core/secp256k1#build-steps) not mentioned in the docs

### Docker Deployment

Decent setup...takes about 10 minutes.

I got an error:

    Creating letsencrypt-nginx-proxy-companion ... 

    ERROR: for letsencrypt-nginx-proxy-companion  UnixHTTPConnectionPool(host='localhost', port=None): Read timed out. (read timeout=180)

Just testing it out required the HTTPS cert setup and it was just complaining.

Interesting that the docker deployment is almost exactly how the BTCpayServer works...similar wording and flow.

#### Verdict

* A few too many features I think
* Heavy weight - lots of dependencies
* Takes about 30 minutes to stand up at the shortest - if everything goes smoothly - unfortunately not the case.
* Still growing
* Worth using BTCPayServer until Bitcart CC gains more stability

## Satsale

* More lightweight
* You must have a full node and must open it directly to satsale - a security concern for me.
* 

## Cypherpunk Pay

* Full node recommended
* Easier to install - debian/ubuntu packages
* 


## Sources

* [Awesome list of bitcoin payment processors](https://github.com/alexk111/awesome-bitcoin-payment-processors)