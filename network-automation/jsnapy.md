# Jsnapy: Juniper Test Driven Networks

On your juniper network device:

    vagrant@vqfx-re> show bgp summary 
    BGP is not running

On the control node setup your jsnapy config:

    cat jsnapy_config.yaml

which should contain connection credentials to the network devices:

    ---
    hosts:
    - device: vqfx1
        username: antidote
        passwd: antidotepassword
        port: 22
    - device: vqfx2
        username: antidote
        passwd: antidotepassword
        port: 22
    - device: vqfx3
        username: antidote
        passwd: antidotepassword
        port: 22
    tests:
    - jsnapy_tests.yaml

Your test info:

    cat jsnapy_tests.yaml

contains:

    ---
    test_rpc_bgp:
    - rpc: get-bgp-summary-information
    - item:
        xpath: '//bgp-information'
        tests:
            - is-equal: group-count, 1
            err: "Test failed! BGP count is <{{post['group-count']}}>"
            info: "Test succeeded! BGP group count is <{{post['group-count']}}>"
            
            - is-equal: peer-count, 2
            err: "Test Failed! BGP group configured peer count is <{{post['peer-count']}}>"
            info: "Test succeeded! BGP group configured peer count is <{{post['peer-count']}}>"
            
            - is-equal: down-peer-count, 0
            err: "Test Failed! BGP down peer count is <{{post['down-peer-count']}}>"
            info: "Test Succeeded! BGP group configured peer count is <{{post['down-peer-count']}}>"

Three checks are being performed:
* The must be one BGP group configured
* There must be two BGP peers configured
* There must not be any "down" BGP Peers

Running jsnapy:

    jsnapy --snapcheck -f jsnapy_config.yaml -v

