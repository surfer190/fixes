# How to create a systemd script to auto-start mailcatcher

A lot of this stuff needs to be done as root so you might as well log in as root with `sudo su -`

1. go to: `/lib/systemd/system`. This is where systemd scripts usually are placed.

2. Create the service: `vim mailcatcher.service`

3. Put the following contents in there:

    ```
    [Unit]
    Description=Mailcatcher Service

    [Service]
    Type=simple
    ExecStart=/usr/local/bin/mailcatcher
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

4. Enable the mailcatcher service and automatically create the symlink to

    `enable mailcatcher.service`

5. To enable boot time start you need to symlink it to `/etc/systemd/system` with:


    ```
    ln -s /lib/systemd/mailcatcher.service /etc/systemd/system/mailcatcher.service
    ```

### Source

* [DigitalOcean configure linux services](https://www.digitalocean.com/community/tutorials/how-to-configure-a-linux-service-to-start-automatically-after-a-crash-or-reboot-part-1-practical-examples)
* [Start on boot](http://www.dynacont.net/documentation/linux/Useful_SystemD_commands/)
* [Github gist](https://gist.github.com/tstellanova/7323116)
