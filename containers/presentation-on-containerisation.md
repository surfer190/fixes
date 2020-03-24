Containerization

When people say docker they mean the docker engine - but docker has a lot of components.

ephemeral - last for a very short time
we want our data to persist and last a very long time - our application need not.

History?

Why?

It is just another abstraction - more complexity - more shit to learn for me.
I as scared of it - I had seen all the complaints about kubernetes and the learning curve and all that.

Docker encompasses alot of different things

Be stateless, kill your servers almost every day - isn't this the opposite of stability
Link: https://github.com/goldbergyoni/nodebestpractices#-512-be-stateless-kill-your-servers-almost-every-day

It makes our jobs easier:

What are containers vs VMs?

LXC linux containers difference compared to docker containers

ps -ef

I used to like LXD and VM's...but now I'm kinda thinking otherwise....why?
It requires a mindshift change.
From static and stable to ephemeral - ever changing but even more reliable and scalable.

The application - always the most important thing - derive business value.
Everything revolves around the application - in this business we support other businesses doing businesses and the applications they use.
That all lies on top of the systems, virtualisation, hardware and the network.

How this helps the relationship between developers and sys admins / operations

The ways we support this application - scaling

Docker can be used to build images - Dockerfile.

## Key asepcts

Persistance of data
isolation - seperating responsibilities

## The CI process

## What are our options for deploying our docker images?

## How are we going to offer to customers?

## What can we do to ensure the transition from traditional computing?

* Storage as a service - Offering a CDN for applciation assets, offering Managed database options
* Offering a platform for their applications 
* We must start using docker in production first - and we are...AWX is running on docker, Praeco/Elastalert is on docker and a few of our API's will soon be there
* Get our CI process using containers

oVirt and VMWare and the managemant of VM's.

Ease the transition

## Advtanges and Disadvantages of Different Platforms

One does not simply deploy an image to Openshift OKD - it must be a non root user.
Even if you specify the user it will use a random one anyway.

So you are forced to build specifcally for that platform and many images on dockerhub simply won't work - the dev experience can be kak.

On the flip side, it makes them much more secure and harder to gain root access.
Uneccesary root is the root of all evil.

## Ansible, Puppet and Chef 

Feels like they have taken a hit - config management and using ansible for deployment used to be cool.
But that is now seen as traditional. The idempotency they wanted to achieve doesn't really work in reality.

Ansible is still very much a player in networking and a

## Example of Docker, Getting applications running quick and external persistence

When running Docker, your computer is the hotel.
Without Docker, it’s more like a hostel with open bunk rooms.
In our modern hotel, each container that you launch is an individual room with preferably only 1 guest in it.