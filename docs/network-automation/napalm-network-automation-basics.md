---
author: ''
category: Network-Automation
date: '2019-04-30'
summary: ''
title: Napalm Network Automation Basics
---
# Napalm Netowrk Automation Basics

## Getting Started

Install the prerequisites

* Python
* Virtualbox
* Vagrant

Install napalm

    pip install napalm

## Getting Facts from a device

Import napalm

    import napalm

Get the network driver

    driver = napalm.get_network_driver("junos")

> You would want to get this from cmdb rather

Use the driver like a function to get a handle on a specific device

    device = driver(hostname="vqfx1", username="antidote", password="antidotepassword")

Initiate the connection with:

    device.open()

Get facts of the device:

    device.get_facts()

## Get Interfaces on a device

    interfaces = device.get_interfaces()

print the interfaces

    print(interfaces)

You can loop through this response to see which interfaces are up or down:

    for if_name, if_properties in interfaces.items():
        if if_properties['is_up']:
            print("Interface %s is UP" % if_name)
        else:
            print("Interface %s is DOWN" % if_name)

Get layer 3 information with:

    layer3 = device.get_interfaces_ip()

See a full list of functions supported by [napalm](https://napalm.readthedocs.io/en/latest/support/index.html#getters-support-matrix)

## Command Line Utility

You can create an alias for brevity

    alias napalm="napalm --user=antidote --password=antidotepassword --vendor=junos"

Then you can run all napalm functions directly from the cli

    napalm vqfx1 call get_interfaces

Use bash utilities to pipe response and find a specific interface

    napalm vqfx1 call get_interfaces | jq .em4

Execute a ping (reacability test):

    napalm vqfx1 call ping --method-kwargs="destination='10.0.0.15'"

## Commiting configurations

        import napalm

        vqfx1_config = """
        <configuration>
            <interfaces>
                <interface>
                    <name>em0</name>
                    <unit>
                        <name>0</name>
                        <description>This is em0, and it connects to something.</description>
                    </unit>
                </interface>
            </interfaces>
        </configuration>
        """

        driver = napalm.get_network_driver("junos")
        device = driver(hostname="vqfx1", username="antidote", password="antidotepassword")
        device.open()

        # Load device config
        device.load_merge_candidate(config=vqfx1_config)

        # Compare the device config
        print(device.compare_config())

        # Discard the config
        # device.commit_config()

        # Commit config
        device.commit_config()

        # Roll back an update
        device.rollback()


#### Source

* [Read the Docs Napalm](https://napalm.readthedocs.io/en/latest/index.html)
* [NRE Labs](https://labs.networkreliability.engineering/labs/?lessonId=13&lessonStage=1)

