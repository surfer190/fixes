---
author: ''
category: Ecmascript
date: '2016-02-10'
summary: ''
title: Check If Using Jquery Or Prototype
---
#Check if you are using jQuery or Prototype

```
if (window.$$ === window.jQuery)
    console.log('jQuery');
else
    if ( typeof Prototype !== "undefined" ) {
      	console.log('Prototype');
    }
```
