# Python File Systems

Working with the file system

#### Files

* Filename
* Filetype - file extensions (.png, .jpg) is extra info for humans, software actually uses the `filetype`

#### Directories

Folders

Tracing up directories takes you to the `root` directory.
On Windows that is a drive letter like `C:\`
On Posix it would be just a `/`

Official word for slashes `/` is seperators

On windows: backslashes lean to the left `\`
On linux: forward slashes lean to the right `/`

## OS

    >>> import os
    >>> os.getcwd
    <built-in function getcwd>
    >>> os.getcwd()
    '/Users/surfer190/projects/fixes'
    >>> os.chdir('..')
    >>> os.getcwd()
    '/Users/surfer190/projects'

Use `os.getcwd()` to get current working directory
Use `os.chdir('..')` to go back a directory

### Paths

* Absolute path - full path from the root
* Relative path - path from another directory

`..` - move up one directory
`.` - means current directory

To check if a path is absolute use `os.paths.isabs(<path>)`

    >>> os.path.isabs('/Users')
    True
    >>> os.path.isabs('workspaces/')
    False

Path does not actually have to exist

Link to (`os` documentation)[https://docs.python.org/3/library/os.html]

When joining paths python will know what seperator to use with:

        os.path.join(os.getcwd(), 'backups')

Can also add multiple paths

        os.path.join(os.getcwd(), '..', 'backups')

## Pathlib

Library for working with paths

Here are sone docs for (`pathlib`)[https://docs.python.org/3/library/pathlib.html], (`pure paths`)[https://docs.python.org/3/library/pathlib.html#pure-paths] and (`concrete paths`)[https://docs.python.org/3/library/pathlib.html#concrete-paths] 

        >>> import pathlib
        >>> path = pathlib.PurePath(os.getcwd())
        >>> path
        PurePosixPath('/Users/surfer190/projects')

You can join paths with the `/` operator

        >>> path2 = path / 'examples' / 'paths.txt'
        >>> path2
        PurePosixPath('/Users/surfer190/projects/examples/paths.txt') 

Check the `parts`

        >>> path2.parts
        ('/', 'Users', 'stephen', 'projects', 'examples', 'paths.txt')

The root or parent

        >>> path2.root
        '/'
        >>> path2.parents[2]
        PurePosixPath('/Users/surfe190')

Get the filename and suffix

        >>> path2.name
        'paths.txt'
        >>> path2.suffix
        '.txt'

### Back to OS

Check the file and folders in working directory

        >>> os.listdir()

You can provide a path

        >>> os.listdir('my/path`)

Another way is using `scandir` which returns an iterable

        >>> list(os.scandir())

Returns a `DirEntry`

        >>> file
        <DirEntry 'README.md'>
        >>> file.name
        'README.md'
        >>> file.is_file()
        True

Get sats on a file

        >>> file.stat()
        os.stat_result(st_mode=33188, st_ino=6361471, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=3115, st_atime=1482839524, st_mtime=1452884872, st_ctime=1452884872)

`st_size` returns the file size in bytes

If you are not using `scandir` in an iterable or with a context `with` then you need to close it.

        >>> scanner = os.scandir()
        >>> scanner.close()

### Script to show filesize per folder

        import os

        def treewalker(start):
            total_size = 0
            total_files = 0

            for root, dirs, files in os.walk(start):
                subtotal = sum(
                os.path.getsize(os.path.join(root, name)) for name in files
                )
                total_size += subtotal
                file_count = len(files)
                total_files += file_count
                print(root, "consumes", end=" ")
                print(subtotal, end=" ")
                print("bytes in", file_count, "non-directory files")
            print(start, "contains", total_files, "files with a combined size of", total_size, "bytes")

        treewalker('../fixes')

### Utilities

Check if a file or directory exists

    >>> os.path.exists('bootstrap')
    False

Creating a file

    open('test_file.txt', 'w').close()
    open('test_file.txt', 'a').close()

`w` - is truncate
`a` - is append

On `mac` you have to be running python as root to use:

        os.mknod('/mysir/myfile.txt')

By default permissions it creates is `0660`

Make a directory:

        os.mkdir('templates')

Can create multiple at once with:

        os.makedirs('layouts/mobile/apple')

Best thing is create even if a directory already exists:

        os.makedirs('layouts/mobile/apple', exist_ok=True)

Rename a single file:

        os.rename('test_file.txt', 'test.txt')

Rename directories:

        os.renames('assets', 'static/raw')

Replace a directory

        >>> os.replace('templates', 'boiling')


**Get file extension without pathlib**

[Source](https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python)

        >>> import os
        >>> filename, file_extension = os.path.splitext('/path/to/somefile.ext')
        >>> filename
        '/path/to/somefile'
        >>> file_extension
        '.ext'


### File Deletions

        >>> import os

Remove a file

        >>> os.remove('bootstrap/bootstrap.js')

Remove an empty directory, an error given if not empty

        >>> os.rmdir('bootstrap/img')

Deleting a directory that is not empty

        for thing in os.scandir('bootstrap/js'):
            if thing.is_file():
                os.remove(thing.path)

        os.rmdir('bootstrap/js')

Make dirs

        os.makedirs('bootstrap/js/packages/stuff')
        os.removedirs('bootstrap/js/packages/stuff')

Will remove everything except directory not empty

### Send2Trash

There is a package called `send2trash` 

        from send2trash import send2trash

        send2trash('tree.py')

### Working with temporary files, dirctories and friends

        import tempfile

Using the `TemporaryDirectory`:

        with tempfile.TemporaryDirectory() as tmpdirname:
            print("Printed temporary directory named: {}".format(tmpdirname))
            with open(os.path.join(tmpdirname, 'temp_file.txt'), 'w') as f:
                f.write('hello\n')
            input()

Using `TemporaryFile`:

        fp = tempfile.TemporaryFile()
        fp.write(b'hello\n')
        fp.close()

To be able to find the file later on:

        fp = tempfile.NamedTemporaryFile()
        fp.name
        