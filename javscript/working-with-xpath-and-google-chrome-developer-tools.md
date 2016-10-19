# XPath and Google Developer Tools

## How to find an xpath on a webpage

1. Open `Developer tools` -> `console`

2. Type:

```
$x(<YOUR XPATH HERE>)

$x('a[concat(" ",normalize-space(.)," ") = " %s "]/..')
```

## How to find the xpath of an item

1. Inpect element, under the `Elements` tab

2. Right click the element, say `copy` -> `copy xpath`
