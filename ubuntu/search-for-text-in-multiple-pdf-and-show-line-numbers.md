#Search for Text though Multiple PDFs in a Driectory and Show Line Numbers, Output to a Text File

```
find <path> -name '*.pdf' -exec sh -c 'pdftotext "{}" - | grep -in --with-filename --label="{}" --color "<pattern>"' \; > <filename>.txt
```

Sources:

(Search Multiple PDFs)[http://stackoverflow.com/questions/4643438/how-to-search-contents-of-multiple-pdf-files]
(Show Line Numbers Grep)[http://stackoverflow.com/questions/3968103/how-can-i-format-my-grep-output-to-show-line-numbers-at-the-end-of-the-line-and]
