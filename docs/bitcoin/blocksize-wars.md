---
author: ''
category: Bitcoin
date: '2022-03-30'
summary: ''
title: The Blocksize War - Summary Notes
---

## The Blocksize War - Summary Notes

“The Bitcoin XT software was extremely controversial inside the so-called “small block” camp, primarily because it was an incompatible upgrade to the network. What this essentially means is that anyone running a Bitcoin node that validates all the rules would be required to upgrade their software.”

“If everyone did not agree to upgrade, according to the small block world view, this could cause Bitcoin to split into two different coins. This type of upgrade is referred to as a hardfork, the most extreme form of upgrade possible.”

“This type of upgrade can essentially change Bitcoin in any way, from increasing the Bitcoin supply cap above 21 million, to taking away any coins from any holder and giving it to anyone else”

“The letter was signed by the CEOs of BitPay, Blockchain.info, Circle, Kncminer, itBit, Bitnet, Xapo and BitGo.”

“At the time of the supposed handover, the Bitcoin software was published on Sourceforge and, in January 2011, two people were listed as maintainers, Satoshi and Gavin”

“In 2010, Gavin purchased 20,000 Bitcoin for $50. He then created a Bitcoin faucet, or website to give away the Bitcoins.”

“In the early days of Bitcoin, from 2009 to early 2011, the entire ecosystem consisted of just one piece of software, the Bitcoin client. This software existed initially for Microsoft Windows and comprised of the wallet, full node and miner.”

When Bitcoin was released, there was no blocksize limit, although it is likely that larger blocks, perhaps more than 32 MB, would have broken the system. The limit was first introduced by Satoshi in the summer of 2010. On July 15, 2010, Satoshi added the following line of code to the software repository:

    static const unsigned int MAX_BLOCK_SIZE = 1000000;

A month later `Jeff Garzik` created a patched version - removing the block limit.
Theymos chimed in: applying this patch will make you incompatible with other bitcoin clients

“the blocksize limit would prevent fees falling too low, as users would have to bid against each other for space in blocks, which would be full. This blocksize limit would therefore create what economists call a producer surplus, which could incentivise miners once the block subsidy ran out. ”

“A crucial distinction should be made here between this and the blocksize war: the blocksize limit is a part of the Bitcoin protocol, while RBF is only a miner policy. Miners are therefore free to do what they like with respect to RBF and there is no need for consensus.”

* Large blockers prioritised the short term, while small blockers focused on the long term;
* Large blockers prioritised the user experience, while small blockers favoured making the system more resilient;
* Large blockers prioritised growth, while small blockers were more concerned about sustainability;
* Large blockers were more pragmatic and business-focused, while small blockers were more scientific and theoretical, typically highly intelligent computer and cryptography boffins.

Bitcoin core was adopted in February 2013 after a suggestion from Mike Hearn

“SegWit was exceptionally complicated and almost nobody understood it. This was the first major example of the small blockers overestimating the intelligence of their opponents, or at least overestimating the ability of their opponents to understand aspects of computer science. For instance, in hindsight the proposal should have simply been called something like “Increase to 2 MB blocks”. Instead, it had a deeply cryptic and confusing name, which sounded highly suspicious to the large blockers, who wanted something clear and simple they could understand.”

“If people didn’t understand the mechanics of Bitcoin transactions anyway, explaining the mechanics of SegWit was simply impossible.”

“It is also a social system, a live payment system, an economic system, and a financial system”

“lightning network was highly complex, unproven and, in the best-case scenario, many years away from becoming usable”

“However, to the smaller blockers, Bitcoin was not a business, nor a payment system taking on VISA, Paypal and Mastercard. It was a new form of money, something far more ambitious and potentially far more transformational to society and the economy. It was taking on central banks.”

“With the lightning network being highly complex, this of course led to confusion, just as with SegWit. There were false claims that coins locked inside of lightning channels were subject to credit risk and claims that lightning would somehow make credit expansion on Bitcoin more of a problem. ”

“The lightning network also had several other problems compared to on-chain Bitcoin payments, for instance it required the receiver of the transaction to be online and interact with the sender, something on-chain Bitcoin did not require. Lightning also requires users to monitor and manage their channels, to ensure they have sufficient liquidity and prevent theft from their channels.”

“Bitcoin nodes did enforce certain rules; a block had to comply with these rules or it would be ignored. To the small blockers, this was a critical part of how Bitcoin worked. If miners just tried to change the rules like that, it would cause a split in the chain and result in a new coin. The coin following the original rules would continue to be Bitcoin.
 ”

“They were more worried about the idea that not enough end users would be able to run Bitcoin clients which fully validated all the protocol rules, which could undermine the decentralisation of the enforcement of the protocol rules.”

“Coinbase was removed as a recommended wallet on the Bitcoin.org website. This website was one of the main information sources on Bitcoin and the website was originally set up by Satoshi”

January 14, 2016 - Mike Hearn sold all his coins

 “This problem had a simple fix: the activation methodology could require that the first block at the activation point was greater than 1 MB, thereby resulting in a clean split where no chain was vulnerable to a wipeout. However, when discussing this with larger blockers, I was told this wasn't an issue, since support for the larger block side was overwhelming. Large blockers also believed that the hashrate majority defined Bitcoin, and including such a checkpoint undermines this view. It was almost as if the large block ideology made their chain more vulnerable. A prominent smaller blocker however, did discuss this issue with me. He said that it’s best to keep this issue quiet, better to not interrupt an enemy while they are making a major mistake, he explained.”

Bitcoin classic - 2MB blocks

“If there is one thing everyone always agreed on, it was a desire for a higher Bitcoin price.”

“ They never intended to get the miners to commit to SegWit; they just assumed miners would want SegWit anyway.”

2 May 2016 - Gavin's merge access was revoked on bitcoin github.

The book gets this wrong:

> Gavin could encrypt a secret message using Satoshi’s private key, and Craig could decrypt it (if he had the key).

Gavin should encrypt with the public key

Summer 2016 - “The DAO” (Decentralized Autonomous Organization)”

“They were interested in a transformational monetary system; alternative coins claiming to do 40,000 transactions per second didn’t seem relevant to that objective.”

“This is part of the reason they were attracted to Ethereum in the first place. They were bored of the conservative Bitcoiners.”

June 17, 2016 - “The DAO’s Ethereum funds and drain some of it into something called a “child DAO”, over which the hacker potentially had significant control.”

“This is when many people started to realise that a hardfork and contentious split was not just about two issues, hashrate and computer science, but financial markets too”

2016, Bitcoin Unlimited, not only was it highly complex, it was also deeply technically flawed.

“Bitcoin Unlimited was not just a client, but also a formal organisation, with a membership, by-laws, a president and membership voting.”

People just want fame and money - ignoring technical issues.
These people want control and their decisions are often poor.
These people go into governments.
Very important that bitcoin remained small block.

“Bitcoin Unlimited had support from across the large blocker camp, from Brian Armstrong at Coinbase, to Gavin, Jihan Wu and Roger Ver. None of these individuals seemed particularly interested in the nuances and the new parameters involved.”

At the start of 2017, around 15 to 20 percent of the Bitcoin hashrate flagged support for Bitcoin Unlimited. - Jihan Wu controlled

The price of Litecoin then sharply rallied: partly due to excitement over SegWit; partly due to a strategy from some small blockers to buy Litecoin in order to drive the price up and build a positive narrative about SegWit; but mostly due to more funds flowing into the space as the 2017 cryptocurrency bubble began.

Shaoinfry on miners voting: (25 February 2017)

> This situation seems to be against the voluntary nature of the Bitcoin system where participation at all levels is voluntary and kept honest by well balanced incentives.

Segwit was carefully engineered so that older unmodified miners could continue operating _completely_ without interruption after segwit activates.

Older nodes will not include segwit spends, and so their blocks will not be invalid even if they do not have segwit support. They can upgrade to it on their own schedule. The only risk non-participating miners take after segwit activation is that if someone else mines an invalid block they would extend it, a risk many miners already frequently take with spy-mining.

But the fastest support should not be our goal, as a community-- there is always some reckless altcoin or centralized system that can support something faster than we can-- trying to match that would only erode our distinguishing value in being well engineered and stable. - Gregory

> First do no harm." We should use the least disruptive mechanisms available

> It’s important the users not be at the mercy of any one part of the ecosystem to the extent that we can avoid it-- be it developers, exchanges, chat forums, or mining hardware makers. Ultimately the rules of Bitcoin work because they’re enforced by the users collectively-- that is what makes Bitcoin Bitcoin, it’s what makes it something people can count on: the rules aren’t easy to just change.

> We should have patience. Bitcoin is a system that should last for all ages and power mankind for a long time-- ten years from now a couple years of dispute will seem like nothing. But the reputation we earn for stability and integrity, for being a system of money people can count on will mean everything.

> If these discussions come up, they’ll come up in the form of reminding people that Bitcoin isn’t easily changed at a whim, even when the whims are obviously good, and how that protects it from being managed like all the competing systems of money that the world used to use were managed. :)

So have patience, don’t take short cuts. Segwit is a good improvement and we should respect it by knowing that it’s good enough to wait for, and for however its activated to be done the best way we know how. - [Gregory Maxwell](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-April/014152.html)

If the UASF plan was to succeed, small blockers would, ironically, have to run an alternative client with different consensus rules, just as the large blockers had done with Bitcoin XT, Bitcoin Classic and Bitcoin Unlimited.

BIP148

In reality, the smaller blockers were far less powerful than they thought; the main reason for their success in defeating the large blockers up until this point was their superior understanding of Bitcoin, tactical blunders from the large blockers themselves and Bitcoin’s inherent resilience against contentious protocol rule changes.

UASF - User Activated Soft Fork

As well as undermining the core value proposition of Bitcoin, this was also bad tactics. Bitcoin users wanted to feel in control and did not like being told what to do. Therefore, the NYA felt like a repeat of Bitcoin XT, Bitcoin Classic and Bitcoin Unlimited. They had made the same mistakes again, except this time with much more industry support.

Most notable by its absence was Bitfinex, perhaps the most economically significant company at the time. Local Bitcoins (the largest P2P exchange at the time), Poloniex, BitMEX and mining pool Slush were also notably absent.

Also, remarkably, as someone pointed out in an email on June 14, the BTC1 client did not even implement the hardfork blocksize limit increase.[134] The client kept the four million-unit weight cap, which would have prevented a hardfork and ensured the blocksize limit never increased. It appears as if Jeff never understood the new SegWit limit: remember, he had thought SegWit had two limits. Only after this was pointed out, post the release of the first version of BTC1, did it actually implement a hardfork. It was proving too difficult for the NYA supporters to double something that they did not understand.

There are two group of people which have two different visions for Bitcoin. None of these visions is “wrong”. One group values more things like decentralization, lack of government, censorship resistance, anonymity. This group thinks that Bitcoin will transform our world in 20-30 years. To reach this goal, it’s of utter importance to stick to those values. There is no rush. The other group values more things like reaching one billion users in the next 5 years, or serving real unbanked users today, even if that requires a political agreement now. Both visions have their merits. But they are incompatible. Replay protection gives a chance to each of these “bitcoiners” to fully push their own vision. Both visions can co-exists.

As the pressure on Jeff mounted, and it appeared that the NYA hardfork might be more contentious than its promoters had originally thought, he agreed to add wipeout protection. Jihan had encouraged Jeff to add this feature into BTC1 and, on June 20, Jeff complied. Rather than merely allowing blocks to be larger than 1 MB after the hardfork, BTC1 now required the first block to be more than 1 MB, a basic form of wipeout protection.

> These miners told me that they did not trust the BTC1 client and were therefore running Segnet or Bitcoin Core. Those running Bitcoin Core were manually including the NYA flag and bit 4 and/or bit 1. I was informed that this was top secret and that this was shared with me in confidence; in public, it was vital to show support for BTC1 and the NYA, the miners explained.

A few days later, towards the end of July 2017, Bitmain finally flagged for bit 1, just a few days before the deadline. The small blockers were ecstatic. After a grueling campaign, more than 10 months after SegWit was released, the largest miner in the space had finally flagged support for it. Most small blockers had believed that this would never happen. SegWit activation now finally looked likely.

In the true spirit of Bitcoin and its pseudonymous creator, Satoshi, the UASF didn’t emerge from an official, closed-door, roundtable meeting among the big players. Instead, it was released in the open and promoted by a pseudonymous developer, Shaolinfry.

As Bitcoin Cash had expected to be the minority hashrate chain, one of the concerns was that blocks would be too slow at the start and Bitcoin’s two-week difficulty adjustment period would then take too long to have an impact. Bitcoin Cash therefore lowered the difficulty requirement, which had another inadvertent benefit: it meant the Bitcoin Cash block headers were incompatible with Bitcoin, and therefore even Bitcoin light clients and mobile wallets would always know not to follow the Bitcoin Cash chain.

> However, the new difficulty adjustment algorithm later proved to be fundamentally flawed, as it incentivised miners to leave the network and then return when the difficulty adjusted and profitability improved.

The impact of this was that the capacity of the Bitcoin Cash network oscillated in a volatile way, which proved to be a major weakness and impacted the reliability of Bitcoin Cash as a payment network. It also caused blocks to be mined faster, which eventually resulted in Bitcoin Cash being around 10,000 blocks ahead of Bitcoin, with more block subsidy coins mined earlier.

> The last common block between Bitcoin and Bitcoin Cash was at height 478,559, mined at 1.16pm UTC on August 1, 2017 by the BTC.com mining pool.

The first Bitcoin Cash block was not mined for another five hours or so, also by ViaBTC. The message inside the coinbase transaction read: “Welcome to the world, Shuya Yang!” and the size of the block was 1.9 MB.

The third Bitcoin Cash block, mined late in the night Hong Kong time, was produced by an unknown miner and the coinbase message this time was the phrase: “Genesis Block 269-273 Hennessy Road Wan Chai Hong Kong.

> There was also a financial aspect to the split: every holder of Bitcoin before the split now had an equal amount of Bitcoin and Bitcoin Cash. The opposing sides could sell the coin they did not favour and accumulate more of their chosen coin. To the small blockers, Bitcoin Cash was sure to trade at a low price, perhaps around two percent of Bitcoin, indicating the fundamental flaws in the large blocker vision, the lack of investor demand and the technical mistakes the large blockers were sure to make.

I remember speaking to a respected small blocker at the time, with large Bitcoin holdings. Privately, he told me that he was keen not to sell his Bitcoin Cash too quickly. It was “vital to ensure Bitcoin Cash was successful” he explained, adding that if they sold too much too fast, the price would fall and the large blockers would not be optimistic about their new coin. Most small blockers wanted the large blockers to leave Bitcoin and stop causing trouble by promoting dangerous hardforks, advocating for aggressive blocksize limit increases and delaying important upgrades such as SegWit. It was therefore considered important to ensure Bitcoin Cash had sufficient “exit momentum” to make certain that some of these large blockers left for good.

Trading of the token began almost immediately on several exchanges such as Kraken, with Bitcoin Cash trading at around 10 to 12 percent the price of Bitcoin.

Critically, on Kraken, if you were short Bitcoin at the time of the fork, you were then automatically short Bitcoin Cash.

Up until this point, there was no way for the small blockers to sell their Bitcoin Cash, unless they kept their Bitcoin on an exchange pre-fork. This is not something many Bitcoiners liked doing; they preferred to avoid counterparty risk and hold their own private keys.

> The first step was to spend the Bitcoin and send it to a different wallet, and only then import your private key into your new Bitcoin Cash wallet to spend the coins. That way, the Bitcoin were never at risk from security vulnerabilities in the Bitcoin Cash clients.

Finally, as the first blocks were mined that enabled users to trade, the price of Bitcoin Cash instantly plummeted, by almost 20 percent. Traders were so keen to sell Bitcoin Cash that they quickly market sold the coin as soon as their funds had cleared. It went on for hours like this, with the Bitcoin Cash price plummeting every time a block was mined, something the small block camp were keen to exploit and which they joked about on social media.

Messages were going around urging people not to sell Bitcoin Cash for less than seven percent of the price of Bitcoin. The rationale here appeared to be that this was a mechanism to make the large blockers pay up.

Bitcoin Cash had also placed a large administrative burden on exchanges and introduced a whole range of complexities, such as how to handle margin balances and debt markets.

> On August 3, 2017 a pull request was merged into Bitcoin Core, and the new code blocked BTC1 peers from making connections to Bitcoin Core

At much the same time, a number of miners decided to create a bitcoin fork on the basis of the same genesis block as bitcoin, naming this coin “Bitcoin Cash” (“BCH”) – removing Segregated Witness from that chain and implementing changes which included (among others) support for blocks of up to 8MB.

NYA == Segwit2x

mandatory replay protection

Elected to designate the Segwit2x fork as B2X

On October 23, BitMEX’s CEO Arthur Hayes put out a blogpost entitled “Trading ShitCoin2x”.

Jeff Garzik created an altcoin (shitcoin) Metronome.

Coinbase finally abandoned NYA - joining bitfenic and coinmex.

On October 23, BitMEX’s CEO Arthur Hayes put out a blogpost entitled “Trading ShitCoin2x”

The large blockers never really supported SegWit2x, their hearts went to Bitcoin Cash.

> Now, the one pool of support left for SegWit2x, the miners, looked to be fading away. SegWit2x was dead in the water. The small blockers looked set for a sensational victory. It was no longer a question of if, but when.

> On Wednesday, November 8, at 4.58pm UTC, with just one week to go until activation of SegWit2x, an email was sent to the SegWit2x mailing list from Mike Belshe, also signed by the other prominent SegWit2x supporters. The email was essentially an unconditional surrender; phase two of the NYA was officially abandoned. The SegWit2x supporters had little choice: had they gone ahead, it would merely have resulted in a new alternative coin that would have been less popular than Bitcoin Cash. It is at this point, 816 days after the war commenced, that I mark the formal cessation of hostilities.

Segwit2x was a 2x block size increase

When news of SegWit2x’s abandonment was released, it caused a tremendous increase in the value of Bitcoin Cash, which was now the last coin standing as far as the large blockers were concerned.

However, a couple of days later it reached a peak of around 48 percent of the Bitcoin price, before crashing shortly afterwards.

On November 15, when the SegWit2x activation point finally came around, it emerged that the client was full of critical bugs. The hardfork was supposed to occur at block height 494,784, however, for some reason, the BTC1 clients became stuck two blocks early at height 494,782.[177] Due to errors in the implementation, the client implemented some aspects the hardfork two blocks earlier than expected. This could have been a disaster for exchanges, which intended to take snapshots of user balances at the hardfork block height.

On December 20, 2017, there were more Bitcoin Cash trading shenanigans. Coinbase had listed Bitcoin Cash and, in the excitement, the coin traded as high as US$8,500. A record in US dollar terms, but not as high as the November peak in Bitcoin terms. As soon as the coin listed, Coinbase couldn’t handle the demand and the system experienced large delays. This was very much a botched listing, and some of the small blockers, who did not have a favourable view of Coinbase due to its support of Bitcoin XT, Bitcoin Classic and even Bitcoin Unlimited, took a dim view of the situation. They accused Coinbase of insider dealing-related offences, essentially leaking this information to large blockers before Bitcoin Cash was listed.

When this war was ancient history, in August 2018, Bitmain attempted to conduct an IPO in Hong Kong. The listing documents indicated that Bitmain invested more than US$888 million into Bitcoin Cash.[182] This was the majority of the free cash flow the company had generated in the 2017 cryptocurrency bull market. At this point, the price performance of Bitcoin Cash had been weak and the company had experienced heavy mark-to-market losses. Jihan had been a passionate advocate of larger blockers and a relentless warrior in a fight that lasted more than two years. However, he had let this cloud his judgement and made poor investment decisions. Bitmain incurred heavy losses in Bitcoin Cash.

At the time of writing in early 2021, Bitcoin Cash trades at around one percent of the price of Bitcoin and it is widely accepted in the space that the path chosen by the large blockers in the summer of 2017 was not the most effective way forward.

Bitcoin demonstrated that it could be the user-controlled money, that it was always meant to be.

This war may only be dry run for the challenges to come, when the primary beneficiaries of the centrally-controlled monetary systems finally realise the potential of user-driven money and they may not like it.

## Sources

* [The Blocksize War:  The battle for control over Bitcoin’s protocol rules - Jonathon Bier ](https://bitcoin-resources.com/books/the-blocksize-war)
