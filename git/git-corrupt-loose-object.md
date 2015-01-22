##Loose Objects, Empty Objects, ref does not point to valid object, Invalid sha1 pointer

Something like this
```
error: object file .git/objects/eb/0d37edc20d9c937754acd6d4dcc41b2b854acd is empty
fatal: loose object eb0d37edc20d9c937754acd6d4dcc41b2b854acd (stored in .git/objects/eb/0d37edc20d9c937754acd6d4dcc41b2b854acd) is corrupt
```
or
```
dangling blob 5801781ef66b4f5f402e07cb1d9d436953c46846
```
or
```
error: refs/remotes/origin/master does not point to a valid object!
```

Solution:
```
[ create a backup of the corrupt directory: cp -R foo foo-backup ]
clone again the remote repository to a new directory: git clone git@www.mydomain.de:foo foo-newclone
delete the corrupt .git subdirectory: rm -rf foo/.git
move the newly cloned .git subdirectory into foo: mv foo-newclone/.git foo
delete the rest of the temporary new clone: rm -rf foo-newclone
```

(source)[http://stackoverflow.com/questions/11597003/how-to-remove-fatal-loose-object]
