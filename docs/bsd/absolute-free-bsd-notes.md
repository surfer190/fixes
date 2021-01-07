---
author: ''
category: BSD
date: '2020-12-14'
summary: ''
title: Absolute FreeBSD Notes
---

# Absolute FreeBSD Notes

FreeBSD is a freely available Unix-like operating system

Started in 1979 with BSD

AT&T wasn't allowed to compete in the computer industry - so it couldn't sell its software.
It instead licensed software to universities at low prices.
The best known software distributed under this license was _unix_

Professors give projects to their students to fix bugs.

Additional software added became known as the Berkeley Standard Distribution

In 1992 BSD code was released to the general public under the BSD licence

### The BSD Licence

Summarised as:

* Don't claim you wrote this
* Don't blame us if it breaks
* Don't use our name to promote your product

Meaning you can do anything else.

AT&T started selling Unix to enterprises - a lawsuit - it was proved most of AT&T Unix was taken from BSD and AT&T had violated the licence by stripping the copyright.

IOnce the dust settled a new version of BSD: BSD 4.4-Lite2 was created - the grandfather of FreeBSD.

Some big companies run FreeBSD - Netflix, Juniper, NetApp, Sony, DELL EMC
If a company needs to pump serious internet bandwidth it is probably running FreeBSD.

FreeBSD development structure:

* 500 commiters - read and write access.
* Contributors - Submit patches
* User

> Apple’s macOS? That’s right. Apple incorporates large chunks of FreeBSD into its macOS on an ongoing basis. If you’re looking for a stable operating system with a friendly face and a powerful core, macOS is unquestionably for you.

### FreeBSD Strengths

* Portability
* Power
* Simplified Software Management
* Customizable Builds
* Advanced Filesystems 

Who should use FreeBSD:

* Famous for strength as an internet server
* Strong for web, mail and file

To learn FreeBSD running it on your desktop is the best way...raw FreeBSD

> Unix’s underlying philosophy is many small tools, each of which does a single job well.

### Pipes

Small programs work together provide flexibility and power

Unix programs have 3 channels of communication.

* standard input - source of input keyboard, network, a file or program
* standard output - where the output goes: screen, network, file etc.
* stanard error - where the program sends error messages

### Everything is a file

Unix has no Windows-style registry. If you backup the files you backup the whole system.

Hardware is also dentified as files: `dev/cd0` is a cd-ROM drive.

> Everything is a file

# 1. Getting More Help

The freeBSD attitude: Yes, you are in school. The information technology business is nothing but lifelong, self-guided learning. Get used to it or get out. Burnt offerings, on the other hand, are difficult to transmit via email and aren’t quite so useful today.

> There is no toll-free number to call and no vendor to escalate within. No, you may not speak to a manager and for a good reason: you are the manager. Congratulations on your promotion!

## Manual Pages

Primordial (existing from the begging of time) - quite friendly for C Programmers.

> The skill level required for system administrators has dropped - you no longer need to be a programmer

The FreeBSD manual is divided into sections:

1. General user commands
2. System calls and error numbers
3. C programming libraries
4. Devices and device drivers
5. File formats
6. Game instructions
7. Miscellaneous information
8. System maintenance commands
9. Kernel interfaces

a reference to `reboot(8)` means see system maintenance commands of the manual of `reboot`

Navigating:

* `space` goes down
* `b` goes up

# 3. Installing FreeBSD

Hierachy info:

    man hier

Manual info:

    man man




## Source

* Absolute FreeBSD®, 3rd Edition. - Michael W. Lucas



