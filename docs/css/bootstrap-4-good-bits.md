---
author: ''
category: Css
date: '2018-11-18'
summary: ''
title: Bootstrap 4 Good Bits
---
# Bootstrap 4: the Good Bits

Moving from Bootstrap 3 to Bootstrap 4 what things should we know...

Check [this to see the migration guide moving from a bootstrap beta verstion to stable bootstrap 4](https://getbootstrap.com/docs/4.1/migration/)

## Reboot and Normalize.css

It uses reboot and normalize.css to be consistent across all browsers. This is built-in.

## Headings

[Display Heading](http://getbootstrap.com/docs/4.1/content/typography/#display-headings) can now be used for extra large headings, without having to explictly create a class for them.

Use:

    <h1 class="display-1">Synergy Systems Online</h1>

`display-1`, `dispaly-2`, `display-3` and `display-4` can be used.

[Lead Paragraphs](http://getbootstrap.com/docs/4.1/content/typography/#lead)

Make a paragraph stand out

    <p class='lead'>Coming Soon, the company bringing Saas and data science solutions for your product</p>

## Layout

[Use Standard Containers](http://getbootstrap.com/docs/4.1/layout/overview/#containers)

Just like boostrap 3, wrap your content in:

    <div class="container">
    <!-- Content here -->
    </div>

You can also use `.container-fluid`.

> Required for using the grid system

### Hiding

[Hiding elements](https://getbootstrap.com/docs/4.1/utilities/display/#hiding-elements) is completely different:

There is no longer a `hidden-*` class. 

Now there is the `.d-*-*` class.

Eg. Hidden only on `xs`: `.d-none .d-sm-block`

### Floating (Pull)

`.pull-right` and `.pull-left` are gone. These are now [float](https://getbootstrap.com/docs/4.1/utilities/float/)

`.float-left`, `.float-right` and `.float-none`

You can also float on specific viewport sizes:

    <div class="float-md-left">Float left on viewports sized MD (medium) or wider</div><br>

### Offsetting

Offsets are no longer of the form: `col-md-offset-2`

They are now simply: `offset-md-2`

### Media Query Ranges

Media Query ranges or breakpoints are now split into 5 groups.

`xs`: No minimum
`sm`: `>= 34em`, `>= 576px`
`md`: `>= 48em`, `>= 720px`
`lg`: `>= 62em`, `>= 940px`
`xl`: `> 75em`, `>=1140px`

### Push and Pull Removed

`push` and `pull` modifiers have been removed in favour of `order`:

`.col-8.push-4` becomes `col-8.order-2`
`.col-4.pull-8` becomes `.col-4.order-1`

### Grid

`container` > `row` > `columns`

1 to 12 columns per row

> If you want equal spaced columns, you needn't specify the size

    <div class="container">
        <div class="row">
            <div class="col-sm">1</div>
            <div class="col-sm">2</div>
            <div class="col-sm">3</div>
        </div>
    </div>

## Components

### Cards

[Cards](https://getbootstrap.com/docs/4.1/components/card/) are a good addition. It is a common requirement that we used to have to build manually.



### Navbar

Fixing the navbar to the top uses `.fixed-top` instead of `.fixed-navbar-top`

## Content

### Images

**Responsive Images**

`.img-responsive` is **no more**. It is now [`.img-fluid`](http://getbootstrap.com/docs/4.1/content/images/#responsive-images)


Image thumbnails give a rounded border to an image

    <img src="..." alt="..." class="img-thumbnail">

Circle images:

Use the classes: `.rounded-circle` and `.rounded`

## Utilities

[Text alignment](http://getbootstrap.com/docs/4.1/utilities/text/#text-alignment)

Seems to work the same as bootstrap 3...with: `text-center`, `text-right`, `text-left` and `text-justify`.

You can also specify alignment for viewport sizes eg. `text-sm-left`

[Background Colours](http://getbootstrap.com/docs/4.1/utilities/colors/#background-color) can be added to any element now. Something that was not in boostrap 1 as far as I know.

    <div class="bg-info">

> Background colours **do not** change text colour, use [`.text-*` colour utilities](http://getbootstrap.com/docs/4.1/utilities/colors/#color)

[Contextual Text Colours](https://getbootstrap.com/docs/4.1/utilities/colors/)

    <p class="text-primary">.text-primary</p>
    <p class="text-secondary">.text-secondary</p>
    <p class="text-success">.text-success</p>
    <p class="text-danger">.text-danger</p>
    <p class="text-warning">.text-warning</p>
    <p class="text-info">.text-info</p>
    <p class="text-light bg-dark">.text-light</p>
    <p class="text-dark">.text-dark</p>
    <p class="text-body">.text-body</p>
    <p class="text-muted">.text-muted</p>
    <p class="text-white bg-dark">.text-white</p>
    <p class="text-black-50">.text-black-50</p>
    <p class="text-white-50 bg-dark">.text-white-50</p>

### Spacing

[Spacing](http://getbootstrap.com/docs/4.1/utilities/spacing/) no longer do you have to set additional css styles for margins and padding to add a bit of space. 

The format for spacing is `{property}{sides}-{size}` for all sizes.
For breakpoints `sm`, `md`, `lg`, and `xl` use: `{property}{sides}-{breakpoint}-{size}`

Property is:

* `m` - margin
* `p` - padding

Sides is:

* `t` - top
* `b` - bottom
* `l` - left
* `r` - right
* `x` - left and right
* `y` - top and bottom
* `blank` - for all 4 sides

Size is:

* `0` - eliminates padding
* `auto` - set the margin to auto
* `1` - $spacer * 0.25
* `2` -  $spacer * 0.5
* `3` - $space * 1
* `4` - $spacer * 1.5
* `5` - $spacer * 3

Size uses `rem` - `root em` which is a css unit relative to the fontsize of the root element, usually `<html>`

eg:

    <div class="mt-3">


