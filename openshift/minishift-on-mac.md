# Installing Minishift on MacOS

Check the [prerequisites](https://docs.okd.io/latest/minishift/getting-started/setting-up-virtualization-environment.html#for-macos)

Basically is tells you to run:

    brew install docker-machine-driver-xhyve
    
    To have launchd start docker-machine now and restart at login:
    brew services start docker-machine
    Or, if you don't want/need a background service you can just run:
    docker-machine start
    ==> docker-machine-driver-xhyve
    This driver requires superuser privileges to access the hypervisor. To
    enable, execute
        sudo chown root:wheel /usr/local/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
        sudo chmod u+s /usr/local/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve

Ensure to run those 2 commands:
    
    sudo chown root:wheel /usr/local/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
    sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve

Then [install minishift](https://docs.okd.io/latest/minishift/getting-started/installing.html)

    brew cask install minishift

Start minishift

    minishift start
