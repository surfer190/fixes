# Theming Magento 2 Customisation Tasks

## Theme Loho

Must put in `app/design/frontend/<vendor>/<theme>/web/images` as `logo.svg`

It is then automatically recognised

## Magento 2 and less

Why?

* Faster deveopment
* Simpler customisation
* Cleaner Structure
* Selectors nesting
* Use of variables
* Extends
* Operations

### Compilation mode

Server side: best for production
Client side: During development and done in browser

`_extend.less` is easiest way to extend parent theme

`web/css/source/_theme.less` is override default magento ui library variables

### Theme Css and LESS

Module specific styles:

`app/design/frontend/<vendor>/<theme>/<Namespace>_<Module>/web/css`

`/web/css/`:

* `print.less` - printed versions
* `_styles.less` - included file
* `styles-m.less` - mobile specific styles
* `styles-l.less` - Desktop specific styles
* `source/` - Mixins and overrides of Magento UI library

`_<filename>.ext` - usually mean file is included in other files

### Adding LESS

In `app/design/frontend/Magento/blank/Magento_Theme/layout/default_head_blocks.xml`:

```
<head>
  <css src="css/style-m.css">
</head>
```
### Less directives

`@magento_import`

## Magento UI Librarry

* Built on LESS
* Foxuesed on web standards
* Customisable
* Easy to maintain
* Responsive
* Accessible

Readme for mixins: `/libs/web/css/docs/src/readme.md`

Mixin description: `/lib/web/css/docs`

HTML view: `pubs/static/frontend/magento/blank/en_US/css/docs/index.html`

Can customise the following elements:

* action-toolbar
* breadcrumbs
* buttons
* components
* drop-downs
* forms
* icons
* layout
* loaders
* messages
* pagination
* grids
* popups
* ratings
* resets
* Responsive
* sections: tabs and accordions
* tables
* tooltips
* typography
* utilities
* list of theme variable

### To override a Magento UI variable

Specify the new variable value in:

`app/design/frontend/<Vendor>/<theme>/web/css/source/_theme.less`

Note: It overrides that of parent theme, to inherit you must copy parent `_theme.less` content

### Extending

Best practises:

* Use a new theme for customisation, don't use existing Blank or Luma themes (Use parent mechanism)
* Use grunt for processing
* Reuse the UI library

To extend less files you add `_extend.less`

Eg. To extend `Magento_Catalog` add:

`/app/design/frontend/Vendor/themename/Magento_Catalog/web/css/source/_extend.less`

## Compiling / Processing

Three ways to compile LESS:

* Server-side compilation with PHP
* Client-side compilation with JS
* Local compilation with Grunt

To change: `Admin -> Stores -> Configuration -> Advanced -> Developer -> Front-end Dev Workflow`

### Server side compilation

Production mode. Slow, global recompile, need to delete static files before each run.

### Client side compilation

Cons: Annoying blinking before styles compile.
Pros: No additional setup, Fast.

### Local compilation

Advanced mode
Cons: requires initial setup of local env
Pros: Fast, recompiles only local changes, easy to debug, can be automated

### Local Compilation Setup

Copy `package.json.sample` to `package.json`

Copy `Gruntfile.js.sample` to `Gruntfile.js`

1. Install node.js
2. Install grunt: `npm install -g grunt-cli`
3. Install npm packages: `npm install`
4. Register your theme in: `dev/tools/grunt/configs/theme.js`

### Useful grunt commands

* `grunt refresh` - Cleans static files and compiles all theme styles
* `grunt clean` - Cleans static files (pub and var)
* `grunt less` - Compiles LESS to CSS
* `grunt watch` - Start watching changes, compiles on save
* `grunt exec <theme>` - Republishes symlinks to locale directory

[Add theme to Grunt config example styles debugging](http://devdocs.magento.com/guides/v2.0/frontend-dev-guide/css-topics/css_debug.html)
