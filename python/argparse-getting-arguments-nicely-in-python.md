# Argparse getting arguments nicely in python

[Argparse](https://docs.python.org/3/library/argparse.html) is really cool.

No longer do we need to wrangle with `sys.argv`.

## Example

Say you want a program that takes a username and ip address:

    ./myscript.py foxxy445 192.168.0.1

You can handle that nicely with:

    import argparse
    
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Link ip to username')
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('ip', type=str, help='IP address')
        
        input_args = parser.parse_args()
        
        ip = input_args.ip
        username = input_args.username

        # do something

Now validation is handled for you and also help:

    python myscipt.py help

    usage: myscipt.py [-h] username ip

    Link ip to username

    positional arguments:
    username    Username
    ip          IP address

    optional arguments:
    -h, --help  show this help message and exit

### Sources

* [Argparse docs](https://docs.python.org/3/library/argparse.html)
