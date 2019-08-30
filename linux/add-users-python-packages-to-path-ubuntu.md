# Add a user's python packages to the python path

Where are python packages kept?

apparently they are in `~/.local/` with binaries stored at `~/.local/bin`

To add them to the path, edit `~/.bashrc`:

    export PATH="~/.local/bin/:$PATH"

Reinitialise the shell:

    exec $SHELL

### Source

* [Add to path](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7)