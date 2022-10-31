---
author: ''
category: Nginx
date: '2019-09-04'
summary: ''
title: SELinux And Nginx
---
# SELinux

SELinux is enabled by default on modern RHEL and CentOS servers.
Each operating system object (process, file descriptor, file) is labelled with an SELinux context that defines its permissions.

In CentOS 6.6 and later, nginx is labelled with `httpd_t` context

> The `httpd_t` context permits NGINX to listen on common web server ports, to access configuration files in `/etc/nginx`, and to access content in the standard docroot location (`/usr/share/nginx`). It does not permit many other operations, such as proxying to upstream locations or communicating with other processes through sockets.

## Nginx and SELinux

The best thing to do it enable permissive mode, which will log all transgressions in `/var/log/audit/audit.log` but allow them.

To add httpd_t to the list of permissive domains:

    semanage permissive -a httpd_t

To delete httpd_t from the list of permissive domains:

    semanage permissive -d httpd_t

To set the mode globally to permissive:

    setenforce 0

To set the mode globally to enforcing:

    setenforce 1

> Note the above actions are temporary

### Next steps

Install the policy tools:

    yum install policycoreutils-python

Make a few requests on your web server and then check `/var/log/audit/audit.log`

You might see something like this:

    type=AVC msg=audit(1567592841.918:9416): avc:  denied  { getattr } for  pid=6374 comm="nginx" path="/var/www/site/site/staticfiles/rest_framework/css/bootstrap.min.css" dev="dm-0" ino=18300561 scontext=system_u:system_r:httpd_t:s0 tcontext=unconfined_u:object_r:var_t:s0 tclass=file permissive=1
    type=SYSCALL msg=audit(1567592841.918:9416): arch=c000003e syscall=5 success=yes exit=0 a0=e a1=7ffebd187290 a2=7ffebd187290 a3=55bea87038f0 items=0 ppid=6373 pid=6374 auid=4294967295 uid=991 gid=994 euid=991 suid=991 fsuid=991 egid=994 sgid=994 fsgid=994 tty=(none) ses=4294967295 comm="nginx" exe="/usr/sbin/nginx" subj=system_u:system_r:httpd_t:s0 key=(null)

Use `audit2why` to interpret the message:

    grep 1567592841.918:9416 /var/log/audit/audit.log | audit2why

If you get this:

	Was caused by:
		Missing type enforcement (TE) allow rule.

		You can use audit2allow to generate a loadable module to allow this access.

File access is forbidden, you need to allow access.

    grep nginx /var/log/audit/audit.log | audit2allow -M nginx
    semodule -i nginx.pp
    semodule -l | grep nginx

Then enable selinux enforcing again with:

    setenforce 1

then check the status with

    sestatus

Or edit `/etc/sysconfig/selinux` and set:

    SELINUX=enforcing

**That fixed it for me, if that does not work for you you can check the source below**

## Sources

* [Using Nginx with SeLinux](https://www.nginx.com/blog/using-nginx-plus-with-selinux/)
* [Nginx can't access a uWSGI unix socket on CentOS 7](https://stackoverflow.com/questions/26334526/nginx-cant-access-a-uwsgi-unix-socket-on-centos-7)