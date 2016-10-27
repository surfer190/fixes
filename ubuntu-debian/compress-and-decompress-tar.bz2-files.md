# How to Compress and Decompress .tar.bz2 (bz2 tarball)

### Extract

    tar -vxjf /tmp/archive.tar.bz2

    -v: verbose
    -x: extract
    -z: pass through gzip
    -f: bzip2 file

### Compress

```
tar -jcvf archive_name.tar.bz2 dir_to_compress
```

**Source:** [simplehelp](http://www.simplehelp.net/2008/12/15/how-to-create-and-extract-zip-tar-targz-and-tarbz2-files-in-linux/)
[logicassembly](http://logicassembly.com/linux/decompress_tar_dot_gz.htm?ext=bz2)
