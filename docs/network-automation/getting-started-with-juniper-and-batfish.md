---
author: ''
category: Network-Automation
date: '2020-10-15'
summary: ''
title: Getting Started with Juniper and Batfish
---
## Batfish and Juniper

[Batfish](https://github.com/batfish/batfish) and [pybatfish](https://batfish.readthedocs.io/en/latest/index.html) are great tools to **analyse a network** and store the evolution of a network over time.

Batfish is a java based application that does the configuration mangling and storage, while `pybatfish` is the interface to upload config and ask questions about the configuration from the batfish server.

Batfish is most often (only?) deployed as a docker container.
Then you would use `pybatfish` to interface with it.

Batfish uses static configuration dumps **only** from your networking devices and does not connect directly to the devices.

Batfish knows about the concept of a network and a snapshot.

* A _network_ is a logical grouping of devices
* A _snapshot_ is a state of the network at a given time. A network contains many snapshots allowing you to view the evolution of your network.

Batfish supports the [following devices](https://batfish.readthedocs.io/en/latest/supported_devices.html)

## How to use it with Juniper Devices

You need to package and upload snapshot data.

Configuration files are uploaded based on a folder structure:

* `config/`: Configuration of network devices (router1.cfg, router2.cfg)
* `hosts/`: Host configurations eg. pointers to their iptables files (host1.json, host2.json)
* `iptables/`: iptables configuration files (host1.iptables, host2.iptables)
* `batfish/`: supplemental information (isp_config.json)

When packaging the `snapshot` top level folder should be part of the archive.

### Getting the Juniper Configuration

So how do we get the configuration dumps?

I use `junos pyez` so connect to a list of inventory devices and write the config to files.
The `rpc` I use is:

    text_config = dev.rpc.get_config(options={
        'database': 'committed',
        'format': 'text'
    })
    
* [Using junos pyez to connect to devices](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-connection-methods.html)
* Info on [pyez retrieving configuration](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-program-configuration-retrieving.html#id-task-configuration-retrieving-specify-source)
* [List of default pyez Remote Proceddure Calls](https://www.juniper.net/documentation/en_US/junos-pyez/topics/reference/general/junos-pyez-tables-op-predefined.html)

You could of course do it by manually sshing into the machines - but that isn't nice is it:

    ssh user@ip
    show configuration | display text | save config_10_10_2020.txt
    scp user@ip:/var/home/remote/config_10_10_2020.txt .
    
At this point you will have the configuration files.
Make sure to move them into a directory like:

    networks/<network_name>/config/

## Running Batfish

Run the batfish docker container:

    docker pull batfish/allinone
    docker run --name batfish -v $(pwd)/data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone -d

## Uploading the configuration to batfish

Now everything is setup, create a script called `upload.py`:

    from pybatfish.client.commands import (
        bf_session, bf_set_network, bf_init_snapshot
    )

    # Connect to batfish server running locally
    bf_session.host = 'localhost'

    # Set the network you are working with
    bf_set_network('<network_name>')

    # Intialise a snapshot
    SNAPSHOT_DIR = 'networks/<network_name>'
    bf_init_snapshot(SNAPSHOT_DIR, name='snapshot-2020-10-10', overwrite=True)

Then run the file:

    python upload.py

This should start the process of importing the config into batfish, example output:

    status: ASSIGNED
    .... 2020-10-15 09:10:31.629000+02:00 Parse network configs 8 / 74. (00:00:24 elapsed)
    status: ASSIGNED
    .... 2020-10-15 09:10:31.629000+02:00 Parse network configs 8 / 74. (00:00:25 elapsed)
    status: CHECKINGSTATUS
    .... 2020-10-15 09:10:31.629000+02:00 Parse network configs 8 / 74. (00:00:26 elapsed)
    status: ASSIGNED
    .... 2020-10-15 09:10:31.629000+02:00 Parse network configs 8 / 74. (00:00:27 elapsed)

## What now?

Now you can get data, check configuration and run tests on the snapshot.

You do this by asking questions.

Interacting with a batfish service:

* `bfq.<question_name>()` Creates a question (with parameters, if applicable).
* `bfq.<question_name>().answer()` sends a query to Batfish service and returns the results of executing the question
* `bfq.<question_name>().answer().frame()` converts the answer into a Pandas dataframe for easy data manipulation

The best way to interact with batfish is in a data science way...which means getting familiar with [jupyter notebooks](https://jupyter.org/) and [pandas](https://pandas.pydata.org/)

### Installing Jupyter locally

    pip install jupyter
    pip install pandas

Then start the notebook:

    jupyter notbook

### Interacting with batfish

Then you need to import some packages, set the network and snapshot and then sdtart asking questions:

    import pandas as pd
    from pybatfish.client.commands import *
    from pybatfish.datamodel import *
    from pybatfish.datamodel.answer import *
    from pybatfish.datamodel.flow import *
    from pybatfish.question import *
    from pybatfish.question import bfq

    bf_set_network('<network_name>')
    bf_set_snapshot('snapshot-2020-10-10')
    
    load_questions()
    
The you can ask any [questions](https://pybatfish.readthedocs.io/en/latest/questions.html) you need to.

They provide some ideas from their [public notebooks](https://pybatfish.readthedocs.io/en/latest/public_notebooks.html)

### Sources

* [](https://pc.nanog.org/static/published/meetings/NANOG75/1878/20190218_Halperin_Using_Open_Source_v1.pdf)
* [Batfish Introduction](https://sudonull.com/post/32566-Batfish-Introduction)
* [Unleashing the Batfish (Part 1 - Configuration Analysis)](https://www.packetflow.co.uk/unleashing-the-batfish-part-1-configuration-analysis/)
* [Batfish: Cheatsheet](https://www.batfish.org/assets/cheat-sheet.pdf)
