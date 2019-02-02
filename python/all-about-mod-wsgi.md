# Mod WSGI

**TL;DR - I decided not to use Apache and `mod_wsgi` because it is too difficult to setup and maintain. Simple is better than complex**

An apache module which can host any python application supporting the WSGI spec - the python web server gateway.
A WSGI is a specification of a generic API for mapping between an underlying web server and a Python web application [PEP3333](http://www.python.org/dev/peps/pep-3333/)

## Installation

* As an apache module
* As a python package, which install `mod_wsgi` into your environment. THe binary program `mod_wsgi-express` then becomes available on the command line. - does not require any configuration of apache yourself

## Getting Started

Start off with a hello world app to verify that your mod_wsgi set up is working, then move on to a framework based project.

Place the following in a file (`site.wsgi`) in your web root:

    def application(environ, start_response):
        status = '200 OK'
        output = b'Hello World!'

        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)

        return [output]

The user running apache usually `www-data` will need read permission on this file.

> Note that mod_wsgi requires that the WSGI application entry point be called `application`

### Mounting the WSGI Application

This is done in a similar manner to other `CGI` applications using `WSGIScriptAlias`

    WSGIScriptAlias / /var/www/app/site.wsgi

The first argument is the _URL mount point_, the second argument is the absolute pathname to the WSGI application script file

> This directive can only appear in the main Apache configuration files. It cannot be used within either of the Location, Directory or Files container directives, nor can it be used within a “.htaccess” file.

> Note that it is highly recommended that the WSGI application script file in this case NOT be placed within the existing DocumentRoot for your main Apache installation, or the particular site you are setting it up for. This is because if that directory is otherwise being used as a source of static files, the source code for your application might be able to be downloaded.

Then add the following configuration (`sudo vim /etc/apache2/sites-available/app.conf`):

    <VirtualHost *:80>

        ServerName app.synergysystems.co.za
        DocumentRoot /var/www/app

        WSGIScriptAlias / /var/www/app/site.wsgi

    </VirtualHost>

Now enable the site `sudo a2ensite app.conf` and reload apache `service apache reload`

Visit the website at `app.synergysystems.co.za` or whereever you pointed it and see `Hello World!`

> Loading it to the root above would mean that requests to static files for example: `favicon.ico` would be processed by the wsgi application.

In this case you would need to rempa the URL's using aliases:

    Alias /robots.txt /usr/local/www/documents/robots.txt
    Alias /favicon.ico /usr/local/www/documents/favicon.ico

    Alias /media/ /usr/local/www/documents/media/

### Delegating to a daemon process

By default any WSGI app is run in `embedded` mode - it will be run within the apache worker processes used to handle normal file requests.
In this mode any applcation changes would require a server restart - which is annoying.
To avoid this you can use daemon mode.

In Daemon mode, a set of processes are created for the app, any requests are routed to the processes.

To use daemon mode: `WSGIDaemonProcess` and `WSGIProcessGroup` would need to be defined. 

Eg: 2 multithreaded processes

    WSGIDaemonProcess example.com processes=2 threads=15
    WSGIProcessGroup example.com

Changing our existing embedded method:

    <VirtualHost *:80>

        ServerName app.synergysystems.co.za
        DocumentRoot /var/www/app


        WSGIDaemonProcess app.synergysystems.co.za processes=2 threads=15 display-name=%{GROUP}
        WSGIProcessGroup app.synergysystems.co.za

        WSGIScriptAlias / /var/www/app/site.wsgi

    </VirtualHost>

### Debugging

> Apache error logs for more detailed descriptions

The default Apache LogLevel be increased from `warn` to `info` is also a good idea.

    LogLevel info

### Virtual Environments

> When using a Python virtual environment with mod_wsgi, it is very important that it has been created using the same Python installation that mod_wsgi was originally compiled for

**You cannot for example force mod_wsgi to use a Python virtual environment created using Python 3.5 when mod_wsgi was originally compiled for Python 2.7**

So I tried to install mod_wsgi with python 3.6, which means I needed to download the release and compile it from source with:

    cd /opt/mod_wsgi-4.6.5
    sudo ./configure --with-python=/usr/local/bin/python3.6
    sudo make
    sudo make test
    sudo make install

but I got this error:

    /usr/bin/ld: /usr/local/lib/libpython3.6m.a(abstract.o): relocation R_X86_64_32S against `_Py_NotImplementedStruct' can not be used when making a shared object; recompile with -fPIC
    /usr/local/lib/libpython3.6m.a: error adding symbols: Bad value
    collect2: error: ld returned 1 exit status
    apxs:Error: Command failed with rc=65536

So according to this [answer](https://stackoverflow.com/questions/17996628/apxserror-command-failed-with-rc-65536) I need to recompile my python version with `--enable-shared`:

    wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
    tar -xzvf Python-3.6.8.tgz
    cd Python-3.6.8.tgz
    ./configure --enable-shared
    make
    sudo make install

Successful, yet when I run:

    root@web:/opt/Python-3.6.8# python3.6 -V
    python3.6: error while loading shared libraries: libpython3.6m.so.1.0: cannot open shared object file: No such file or directory

So it can't find the libraries, which I used this [answer](https://stackoverflow.com/questions/7880454/python-executable-not-finding-libpython-shared-library) to fix:

    ./configure --enable-shared \
                --prefix=/usr/local \
                LDFLAGS="-Wl,--rpath=/usr/local/lib"

That worked!

I recompiled `mod_wsgi` and that was successful:

    /usr/lib/apache2/modules/mod_wsgi.so

Now I check the apache configuration and...

    sudo apachectl configtest

    apache2: Syntax error on line 248 of /etc/apache2/apache2.conf: Syntax error on line 1 of /etc/apache2/mods-enabled/wsgi.load: Cannot load /usr/lib/apache2/modules/mod_wsgi.so into server: libpython3.6m.so.1.0: cannot open shared object file: No such file or directory

You can view the linked libraries with (taken from this [blog post](https://bluehatrecord.wordpress.com/2016/09/04/compiling-and-installing-mod_wsgi-4-5-6-on-rhelcentos-6/)):

    root@web:/var/log/apache2# ldd /usr/lib/apache2/modules/mod_wsgi.so
	linux-vdso.so.1 (0x00007ffd57fbe000)
	libpython3.6m.so.1.0 => not found
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fd3fb0f4000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fd3faef0000)
	libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fd3faced000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fd3fa9ec000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fd3fa641000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fd3fb54e000)

Importantly the `libpython3.6m.so.1.0 => not found`

I should have read this:

    If you ever happen to want to link against installed libraries
    in a given directory, LIBDIR, you must either use libtool, and
    specify the full pathname of the library, or use the `-LLIBDIR'
    flag during linking and do at least one of the following:
    - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
        during execution
    - add LIBDIR to the `LD_RUN_PATH' environment variable
        during linking
    - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
    - have your system administrator add LIBDIR to `/etc/ld.so.conf'

That file is in: `/usr/local/lib/libpython3.6m.so.1.0` so we must recompile `mod_wsgi` again but with specifiying the `LD_RUN_PATH`

    cd /opt/mod_wsgi-4.6.5
    sudo ./configure --with-python=/usr/local/bin/python3.6
    sudo LD_RUN_PATH=/usr/local/lib make
    sudo make install

Damnit...

    make: Nothing to be done for 'all'.

It did nothing...Ah you have to say:

    make clean

Whoopee:

    root@web:/opt/mod_wsgi-4.6.5# apachectl configtest
    Syntax OK

### Source

* [mod_wsgi read the docs](https://modwsgi.readthedocs.io/en/develop/)