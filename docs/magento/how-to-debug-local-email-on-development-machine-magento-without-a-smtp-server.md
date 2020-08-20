---
author: ''
category: Magento
date: '2020-06-21'
summary: ''
title: How To Debug Local Email On Development Machine Magento Without A Smtp Server
---
#How to Debug Email Sent from Magento on your Local Development Machine

Debugging or even viewing Emails Sent from Magento can be a real hassle.
Even if you have a local smtp set up you need to make sure the email doesn't go to the spam folder or is not rejected entirely by the server.
Also you will have to find multiple email addresses to use for debugging account activation for example.

The best way to debug is to catch the mails on your local machine, before they are sent out.

The best thing to use is a ruby gem called [MailCatcher](http://mailcatcher.me/).

Steps to Install:

- Install [Ruby](https://github.com/sstephenson/rbenv)
    Don't use your package manager as it is usually an outdated version

- Install the gem:

```
gem install mailcatcher
```

- Launch the mailcatcher daemon:

```
mailcatcher
```

- Route all mail sent by your local smtp, in this case `postfix`:

```
sudo vim /etc/postfix/main.cf
```

Edit `relayhost`:

```
relayhost = 127.0.0.1:1025
```

```
sudo /etc/init.d/postfix restart
```

Source: [nls.io](https://nls.io/sysadmin/webdev/2013/04/18/use-mailcatcher-on-your-development-box-to-catch-all-outgoing-em.html)
