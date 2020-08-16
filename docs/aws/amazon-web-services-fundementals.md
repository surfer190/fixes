---
author: ''
category: Aws
date: '2020-06-14'
summary: ''
title: Amazon Web Services Fundementals
---
# Amazon Web services Fundamentals

> I've tried to avoid the corporate bullshit that still exists cause AWS has to appease the corporate clowns if you don't like it please reword it on the repo

Outsources physical hardware, the human capital and intellectual property is maintained. Operators, architects and designers in the cloud.

- An infrastructure service for the world - don't reinvent the wheel **Service Oriented Infrastructure (SOA)**
- Elastic Computing - growing and shrinking environment
- Storage in the Cloud
- Security and Compliance
- Pricing and availability

[AWS Certification Tracks](https://doolan.pw/certifications/)

## Prerequisites (Requirements)

You must have signed up and used an AWS EC2 instance

## AWS History

In 2002 Amazon web service started, as a method to communicate with partners. In 2006 Jeff Bezos spoke about **EC2** and **S3** as the first two products.

EC2 was for Amazon internal infrastructure first, it served an internal business requirement and was then sold to the rest of the world. _He sold behind the scenes_.

> An infrastructure service for the world - Chris Pinkham

An infrastructure service to help Amazon and developers all over the world

Low margins to discourage competitors and lock-in users

## On premise Datacentre

Costs:

* Security
* Cabling
* Networking hardware
* Cooling
* Servers
* Storage
* Space
* Facilities
* Expertise
* Connectivity

Cost Silos

Don't reinvent the wheel, Amazon has acquired task specialisation in the cloud space.
All the physical aspects are abstracted away.

**Infrastucture-as-a-Service (IaaS)** the explanation was too crap to waste your time

## DIY vs AWS

| Do it yourself  | Amazon Web Services  |
|---|---|
| Scaling up and down is time consuming and expensive  | Scaling is elastic and instantanious  |
| Assume reliable infrastructure (Non-idempotent)  | **Expect infrastructure failures** requires idempotent servers  |
| Diverse technical expertise  | Expertised focused on applications  |
| Application unaware of infrastructure | Application can be aware of infrastructure - request more resources (Manipulate/control infrastructure) |
| High-upfront costs | Usage-based costs |
| Design, build, operate, support | Shared support |

## What is elastic computing

Limit resources to what you need

> the degree to which a system is able to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible

## regions and availability zone

Region - geographical area (10)
Availability zone - data centre in a region
Edge Locations - Places to consume services
GovCloud - Specifically for US government

[Check Amazon global infrastructure **Africa, No chance...**](https://aws.amazon.com/about-aws/global-infrastructure/)

## Security

#### Physical

* Secret Locations
* Controlled physical access
* Datacentre Security
* Video Surveillance

#### Server and hardware

* Hardware refresh cycle
* Properly decommissioned storage
* Always on monitoring

[AWS security certifications and compliance](https://aws.amazon.com/compliance/)

#### Shared Security

Amazon does its part but **you need to secure your environment**

| AWS Responsibilities  | Your responsibilities  |
|---|---|
| Virtual host security | AWS account security |
| Storage security | Operating System |
| Network security | Database |
| Data centre security | Applications |
| | Data encryption |
| | Authentication |
| | Network Integrity |

#### Security Methods and Connectivity

- Security Groups - specify resource access
- Virtual Private Cloud (VPC) - access control lists (additional level of security) [subnets, ip's and ports]
- Direct Connect
- Import/Export - Massive amounts of data imports and exports
- VPN Access - extend on premises network
- Dedicated server - regulatory requirements (No connectivity with anything else on request)

#### IAM (Identity and Access Management)

* User and service management
* Control access to aws resources
* Multi-factor authentication
* API Access

Can be found on the crazily complex console home screen

![Amazon fundamentals IAM icon](/img/aws-iam.png){: class="img-fluid" }

[Brain numbing Amazon IAM shit](http://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

## AWS Free Tier

- Gives a taste
- Credit card is required
- Some services only free for 12 months: EC2, ELB, EBS, S3

[An extensive list of offerings on the Amazon Free Tier Account](https://aws.amazon.com/free/)

**Go ahead and create an account now**

##### Note on the management console screen

The amazon web services' screens on their website are very convoluted. Full of links, videos, and useful FAQ and information. Moreover their are tens of different ways to get to all the places except the place you want to go. Naturally this will annoy you or put you off, sometimes it will inspire you though.

Don't be **daunted** when you login, you will see the below screen when you first log in, full of services...just calm down eventually you might learn a few of them.

![Complicated Management Console Screen Amazon Web Services](/img/aws-console-page.png){: class="img-fluid" }

# Amazon Web Services

## EC2 (Elastic Compute)

Open `EC2` under `Compute`, it will open a screen called `Resources` which feels unnatural coming from [Digital ocean](https://m.do.co/c/fc14942ee702) but it apparently gives you a summary or overview of what is going on. Could be useful if you have > 10 ec2 instances.

It may have automatically selected an availability zone in the top right, you can change it by selecting from the dropdown. It can be annoying as you would expect to have an overview of all instances in all regions, apparently that is not how AWS does stuff. It is **very region specific**.

Create an instance with `Launch Instance`, which is essentially (in my mind anyway) `Launch a server`

You will be asked to choose an `Amazon Machine Image (AMI)` similar to a virtual image. Make sure that you choose a `Free Tier Eligible` machine.

Choose `Ubuntu Server 14.04 LTS (HVM), SSD Volume Type`, otherwise if you choose a windows server, corporate linux or any other junk Linux Distro you're an idiot.

Choose the instance type, best to choose the free tier one `t2.micro`

You can skip through the next few settings: `Configure Instance Details`, `Add Storage`, `Tag Instance`, `Configure Security Group`. Then `review` and `launch`.

You will need to create a new `Key-pair`, select `Create a New Key-pair` then `Download Key-pair`

**Launched**, Now go back to the console (Click the amazon logo in the top right), then select `EC2` and then select `1 Running Instance` it might be in a status of `Initialising`

**...Continue from 05_04**
