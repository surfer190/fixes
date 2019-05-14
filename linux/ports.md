# View the processes listening on ports

Install net-tools

    sudo yum install net-tools

Check applications and what ports they are listening on

    netstat -ltnp

* `-l` - Only show listening sockets
* `-t` - Display tcp connections
* `-n` - Show numerical addresses
* `-p` - Show process id and name


## Source

[Find out process listening on a port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)