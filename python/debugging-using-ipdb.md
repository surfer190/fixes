# How to debug python with Ipdb

Sometimes you want to set a break point in the code to inspect what is up

All you need it `ipdb`

## Install Ipdb

`pip install ipdb`

## Usage Ipdb

Then in the code, where you want to break and inpect use:

```
import ipdb as pdb
pdb.set_trace()
```

Source: [Stackoverflow - Installing ipdb](http://stackoverflow.com/questions/34804121/importerror-no-module-named-ipdb)