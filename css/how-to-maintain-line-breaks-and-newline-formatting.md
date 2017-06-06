## How to maintain line breaks and new lines in HTML and CSS

We have had this issue before. We store some server side code entered from a `textarea` by a client and whne we output the data the linebreaks are not maintained.

To do this we need to set the css attribute `white-space`

You can read more about the [white-space css attribute](https://developer.mozilla.org/en/docs/Web/CSS/white-space)

### Solution

You want to set `white-space: pre;` to output the formatting as it was entered

        white-space: pre;