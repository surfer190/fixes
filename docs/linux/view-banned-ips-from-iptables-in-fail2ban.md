---
author: ''
category: Linux
date: '2020-05-12'
summary: ''
title: View Banned Ips From Iptables In Fail2ban
---
## How to View the blocked Ip's for Rules in IPtables arising from Fail2Ban

Find the policy / chain you want to test

    sudo iptables -L

    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination         
    f2b-NoAuthFailures  tcp  --  anywhere             anywhere             multiport dports http,https

    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination         

    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination         

    Chain f2b-NoAuthFailures (1 references)
    target     prot opt source               destination         
    REJECT     all  --  dedic1351.hidehost.net  anywhere             reject-with icmp-port-unreachable
    RETURN     all  --  anywhere             anywhere 

Then test it

    sudo iptables -L <policy_name> -v -n

eg.

    sudo iptables -L f2b-NoAuthFailures -v -n

here:

    Chain f2b-NoAuthFailures (1 references)
    pkts bytes target     prot opt in     out     source               destination         
    20  4114 REJECT     all  --  *      *       151.80.47.82         0.0.0.0/0            reject-with icmp-port-unreachable
        6   352 REJECT     all  --  *      *       178.159.37.139       0.0.0.0/0            reject-with icmp-port-unreachable
    2809  564K RETURN     all  --  *      *       0.0.0.0/0            0.0.0.0/0 

### Source

* [Show the banned ips on IP tables from Fail2ban](https://serverfault.com/questions/841183/how-to-show-all-banned-ip-with-fail2ban)