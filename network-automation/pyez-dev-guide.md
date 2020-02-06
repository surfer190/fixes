# PyEz

Microframework for Python that enables you to manage and automate devices running the Junos operating system (Junos OS)

### About versions

Junos OS: 16.1R3 through 17.3 can use **Junos PyEZ 1.3.1**

Junos OS: 17.4R1 and later can use **Junos PyEZ 2.1.4**

### Modules

`jnpr.junos` contain the modules that handle connectivity, provide operational and configuration utilities.

* `device` - enables to connect and retrieve facts form the device
* `exception` - defines exceptions when using the device
* `factory` - code relating to tables and views including `loadyaml()`
* `facts` - dictionary like read-only facts about the device
* `op` - predifined operational tables and views to filter output
* `resources` - tables and views for specific configuration resources
* `transport` - code to support different connection types
* `utils` - Config utilities, file system utilities, shell utilities and secure copy utilities

The `jnpr.junos.device.Device` class provides access to the device over serial, telnet or SSH.

All connection methods support:
* retrieving device facts
* performing operations
* executing RPCs on demand

Get device info with `facts` and get tables with `op`, `resources` and `factory`

## Installing PyEZ

Install the [prerequisite software](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/installation/junos-pyez-server-installing.html)

Then run:

    pip install junos-eznc

You could also use the [`juniper/pyez` docker image](https://hub.docker.com/r/juniper/pyez/tags/)

## Connecting

PyEz uses `NETCONF` and the `Junos XML APIs`

### Enabling NETCONF over SSH on Devices Running Junos OS

    [edit system services]
    user@host# set netconf ssh
    
These requirements must be met:
* The NETCONF service over SSH is enabled on each device where a NETCONF session will be established.
* The client application has a user account and can log in to each device where a NETCONF session will be established.
* The login account used by the client application has an SSH public/private key pair or a text-based password configured.
* The client application can access the public/private keys or text-based password.

### Configuring Telnet Service on Devices Running Junos OS

    [edit system services]
    user@host# set telnet

Configure rate limit etc.

    [edit system services]
    user@host# set telnet connection-limit connection-limit
    user@host# set telnet rate-limit rate-limit
    user@host# set telnet authentication-order [radius tacplus password]

Commit the config

    [edit]
    user@host# commit

### Connecting with PyEZ

You must use a serial console connection when you are physically connected to the `CONSOLE` port on a device. You can use telnet or SSH to connect to the device’s management interface or to a console server that is connected to the device’s `CONSOLE` port

Specify the connection type with `mode='telnet'` or `mode='serial'`

View the [connection modes on the pyEZ website](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-connection-methods.html)

PyEZ supports context managers `with ... as` otherwise you should explicitly call `open()` and `close()`

#### Device Properties

* `connected`
* `hostname`
* `master` - if the Routing Engine to which the application is connected is the master Routing Engine
* `port`
* `re_name` - Routing Engine name to which the application is connected.
* `timeout` - rpc timeout in seconds
* `uptime` - number of seconds since the current Routing Engine was booted
* `user`

Example:

    from jnpr.junos import Device

    dev = Device(host='router.example.net')

    dev.open()
    print (dev.connected)

    dev.close()
    print (dev.connected)

Connecting with SSH:

    import sys
    from getpass import getpass
    from jnpr.junos import Device
    from jnpr.junos.exception import ConnectError

    hostname = input("Device hostname: ")
    junos_username = input("Junos OS username: ")
    junos_password = getpass("Junos OS or SSH key password: ")

    dev = Device(host=hostname, user=junos_username, passwd=junos_password)

    try:
        dev.open()
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)
        
    print (dev.facts)
    
    dev.close()

or using a context manager:

    import sys
    from getpass import getpass
    from jnpr.junos import Device
    from jnpr.junos.exception import ConnectError

    hostname = input("Device hostname: ")
    junos_username = input("Junos OS username: ")
    junos_password = getpass("Junos OS or SSH key password: ")

    try:
        with Device(host=hostname, user=junos_username, passwd=junos_password) as dev:   
            print (dev.facts)
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)

Give a 6 second timeout:

    import sys
    from getpass import getpass
    from jnpr.junos import Device
    from jnpr.junos.exception import ConnectError

    hostname = input("Console server hostname: ")
    cs_username = input("Console server username: ")
    cs_password = getpass("Console server or SSH key password: ")
    junos_username = input("Junos OS username: ")
    junos_password = getpass("Junos OS password: ")

    try:
        with Device(host=hostname, user=junos_username, passwd=junos_password, 
                cs_user=cs_username, cs_passwd=cs_password, timeout=6) as dev:   
            print (dev.facts)
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)

### Connecting to device with telnet

    import sys
    from getpass import getpass
    from jnpr.junos import Device

    hostname = input("Device hostname: ")
    junos_username = input("Junos OS username: ")
    junos_password = getpass("Junos OS password: ")

    try:
        with Device(host=hostname, user=junos_username, passwd=junos_password, mode='telnet', port='23') as dev:   
            print (dev.facts)
    except Exception as err:
        print (err)
        sys.exit(1)

### Connecting with a serial console connection

    import sys
    from getpass import getpass
    from jnpr.junos import Device
    from jnpr.junos.utils.config import Config

    junos_username = input("Junos OS username: ")
    junos_password = getpass("Junos OS password: ")

    try:
        with Device(mode='serial', port='port', user=junos_username, passwd=junos_password) as dev:
            print (dev.facts)
            cu = Config(dev)
            cu.lock()
            cu.load(path='/tmp/config_mx.conf')
            cu.commit()
            cu.unlock()

    except Exception as err:
        print (err)
        sys.exit(1)

### Authenticating with a Password

    from jnpr.junos import Device
    from getpass import getpass
    import sys

    hostname = input("Device hostname: ")
    junos_username = input("Junos OS username: ")
    junos_password = getpass("Junos OS password: ")

    # login credentials required for SSH connection to console server

    cs_username = input("Console server username: ")
    cs_password = getpass("Console server password: ")


    try: 
        # NETCONF session over SSH
        with Device(host=hostname, user=junos_username, passwd=junos_password) as dev:

        # Telnet connection to device or console server connected to device
        #with Device(host=hostname, user=junos_username, passwd=junos_password, mode='telnet', port='23') as dev:

        # Serial console connection to device
        #with Device(host=hostname, user=junos_username, passwd=junos_password, mode='serial', port='/dev/ttyUSB0') as dev:

        # SSH connection to console server connected to device
        #with Device(host=hostname, user=junos_username, passwd=junos_password, cs_user=cs_username, cs_passwd=cs_password, timeout=5) as dev:

            print (dev.facts)
    except Exception as err:
        print (err)
        sys.exit(1)

### Running Shell Commands

`jnpr.junos.utils.start_shell` defines the `StartShell` command.

`Device.open()` is not required.

Example:

    from jnpr.junos import Device
    from jnpr.junos.utils.start_shell import StartShell

    dev = Device(host='router1.example.net')

    ss = StartShell(dev)
    ss.open()
    ss.run('cli -c "request support information | save /var/tmp/information.txt"')
    version = ss.run('cli -c "show version"')
    print (version)
    ss.close()

### Using Junos PyEZ to Execute RPCs on Devices Running Junos OS

RPC - Remote Procedure Calls

You can get the request tag as text with:

    from jnpr.junos import Device

    with Device(host='router.example.com') as dev:   
        print (dev.display_xml_rpc('show route', format='text'))

Example: Invoke a show version RPC

    from jnpr.junos import Device
    from lxml import etree

    with Device(host='dc1a.example.com') as dev:   
        #invoke the RPC equivalent to "show version"
        sw = dev.rpc.get_software_information()
        print(etree.tostring(sw, encoding='unicode'))

On the router the command `user@router> show interfaces ge-0/0/0 | display xml rpc` would be:

    rsp = dev.rpc.get_interface_information(interface_name='ge-0/0/0')

### Specify the output format of an RPC

To output as text use:

    from jnpr.junos import Device
    from lxml import etree  
        
    with Device(host='router1.example.com') as dev:      
        sw_info_text = dev.rpc.get_software_information({'format':'text'})
        print(etree.tostring(sw_info_text))

To get the output as `json`:

    from jnpr.junos import Device
    from pprint import pprint

    with Device(host='router1.example.com') as dev:      
        sw_info_json = dev.rpc.get_software_information({'format':'json'})
        pprint(sw_info_json)

Specify the rpc timeout:

    dev.rpc.get_route_information(table='inet.0', dev_timeout=55)

### Suppressing RpcError Exceptions Raised for Warnings in Junos PyEZ Applications

    from jnpr.junos import Device
    from jnpr.junos.utils.config import Config

    dev = Device(host='router1.example.com')
    dev.open()

    with Config(dev, mode='exclusive') as cu:  
        cu.load(path="mx-config.conf", ignore_warning=True)
        cu.commit()
        
    data = dev.rpc.get_configuration(ignore_warning=True)
    print(etree.tostring(data, encoding='unicode'))

    dev.close()

More info at [pyez warnings ignoring](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-warnings-ignoring.html)

### Rebooting a device with pyEZ

    #Python 3
    from jnpr.junos import Device
    from jnpr.junos.utils.sw import SW
    from jnpr.junos.exception import ConnectError
    from getpass import getpass

    hostname = input("Device hostname: ")
    username = input("Device username: ")
    password = getpass("Device password: ")

    try:
        with Device(host=hostname, user=username, passwd=password) as dev:
            sw = SW(dev)
            print(sw.reboot())
    except ConnectError as err:
        print (err)

### Reboot with a Delay

    from jnpr.junos import Device
    from jnpr.junos.utils.sw import SW

    with Device(host='dc1a.example.com') as dev:
        sw = SW(dev)
        sw.reboot(in_min=2)

Only reboot the routing engine you are connected to:

    from jnpr.junos import Device
    from jnpr.junos.utils.sw import SW

    with Device(host='dc1a.example.com') as dev:
        sw = SW(dev)
        sw.reboot(all_re=False)

## Info on Installing or Upgrading Images

[Info on Installing or Upgrading Images](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-program-software-installing.html)

## Transfering files using PyEZ

Use the `jnpr.junos.utils.scp.SCP` utility

Example:

    from jnpr.junos import Device
    from jnpr.junos.utils.scp import SCP

    dev = Device('router1.example.com')
    with SCP(dev) as scp:
        scp.put("local-file", remote_path="path")
        scp.get("remote-file", local_path="path")

Track the progress of the download with `with SCP(dev, progress=True) as scp:`

## Using Junos PyEZ to Retrieve a Configuration

### Retrieve the complete config

    from jnpr.junos import Device
    from lxml import etree

    with Device(host='router1.example.net') as dev:
        data = dev.rpc.get_config()
        print (etree.tostring(data, encoding='unicode', pretty_print=True))

### get the config from the committed Configuration Database

    from jnpr.junos import Device
    from lxml import etree
    
    with Device(host='router1.example.net') as dev:
        data = dev.rpc.get_config(options={'database' : 'committed'})
        print (etree.tostring(data, encoding='unicode', pretty_print=True))

## Specifying the scope of configuration to Return

    from jnpr.junos import Device
    from lxml import etree

    with Device(host='router1.example.net') as dev:

        filter = '<configuration><interfaces/><protocols/></configuration>'
        data = dev.rpc.get_config(filter_xml=filter)
        print (etree.tostring(data, encoding='unicode', pretty_print=True))

### Get all Interface Names

    from jnpr.junos import Device
    from lxml import etree

    with Device(host='router1.example.net') as dev:

        filter = '<interfaces><interface><name/></interface></interfaces>'
        data = dev.rpc.get_config(filter_xml=filter, options={'inherit':'inherit'})
        print (etree.tostring(data, encoding='unicode', pretty_print=True))  

### Specifying the format of the config to return

Json Format:

    from jnpr.junos import Device
    from lxml import etree
    from pprint import pprint
    
    with Device(host='router1.example.net') as dev:

        # JSON format
        data = dev.rpc.get_config(options={'format':'json'})
        pprint (data)

### Specifying data for YANG

More info on the [Yang Data Format and Junos](https://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-program-configuration-retrieving.html)

Read about YANG

### Using Junos PyEZ to Compare the Candidate Configuration and a Previously Committed Configuration

    from jnpr.junos import Device
    from jnpr.junos.utils.config import Config

    dev = Device(host='router1.example.com').open()
    with Config(dev, mode='exclusive') as cu:  
        cu.load(path='configs/junos-config-mx.conf', merge=True)
        cu.pdiff()
        cu.commit()

    dev.close()

### Using PyEZ to configure devices

* [Using Junos PyEZ to Retrieve a Configuration](https://www.juniper.net/documentation/en_US/junos-pyez/topics/reference/general/junos-pyez-configuration-process-and-data-formats.html)

## Tables and Views

You can also use Tables and Views to define structured configuration resources

> Tables and Views are defined using YAML, so no complex coding is required to create your own custom Tables and Views.

Example: Output of `show arp no-resolve` , the table extracts `arp-table-entry` elements from the output and selects three fields from `arp-table-entry` item.

    ---
    ArpTable:
      rpc: get-arp-table-information
      args:
        no-resolve: True
      item: arp-table-entry
      key: mac-address
      view: ArpView

    ArpView:
      fields:
        mac_address: mac-address
        ip_address: ip-address
        interface_name: interface-name

### Predefined Junos PyEZ Operational Tables and Views

[Table of available tables](https://www.juniper.net/documentation/en_US/junos-pyez/topics/reference/general/junos-pyez-tables-op-predefined.html)

### Custom Tables and Views

    fromom jnpr.junos import Device
    from jnpr.junos.factory.factory_loader import FactoryLoader
    import yaml

    myYAML = """
    ---
    UserTable:
        get: system/login/user
        view: UserView
    
    UserView:
        fields:
            username: name
            userclass: class
    """

    globals().update(FactoryLoader().load(yaml.load(myYAML)))

    with Device(host='router.example.com') as dev:
        users = UserTable(dev)
        users.get()

        for account in users:
            print("Username is {}\nUser class is {}".format(account.username, account.userclass))




https://github.com/Juniper/py-junos-eznc