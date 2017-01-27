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
