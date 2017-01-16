# Theming Magento 2 Core Priciples

## Resources

[Magento Frontend Developer Guide](http://devdocs.magento.com/guides/v2.1/frontend-dev-guide/bk-frontend-dev-guide.html)

## Configuration

* Usually in `System -> Stores`

Cache to disable: (`System -> Cache Management`)
* `config`
* `layout`
* `blocks_html`
* `full page cache`

Increase admin session lifetime: `Stores -> Config -> Advanced -> Admin -> Security Panel`

Set Wysiwyg editor on/off: `Stores -> Config -> General -> Content Management -> Wysiwyg`

Enable Demo store notice: `Stores -> Config -> General -> Design -> HTML Head`

Important the complexity in theming must be balanced between the ability to share between multiple storefronts

## Theme

Consistent look and feel
Used to override module layouts and templates

Themes control:
* Visual aspects: fonts, css, js, images
* Functional aspects: blocks, templates and data shown in blocks

## File Structure

* `app/code` - Magento and third-party program code
* `app/design` - Design for magento storefronts
* `app/etc` - Base config
* `app/i18n` - Config for language files
* `pub/` - Static files (should not be modified manually)
* `pub/media` - All uploaded media
* `pub/static` - Theme specific CSS, JS, fonts and images
* `var` - Temporary items: reports, cache, sessions and import/export files

Changes:
* Composer support
* Magento UI library
* Less compilation
* theme.xml

Easier to upgrade, better modularity, better organisation and improved security

### Theme folder

`app/design/frontend/<Vendor>/<theme>`

Contents of theme dir:
* `<Vendor>_<Module>/`
  * `web/`
    * `css/`
      * `source/`
  * `layout/`
      * `override/`
  * `templates`
* `etc/` - `etc` is mandatory when theme does not have a parent
* `i18n/`
* `media/`
* `web/` - theme specific js, styles (.less) and image files
  * `css/`
    * `source/`
  * `fonts/`
  * `images/`
  * `js/`
* `composer.jso`
* `registration.php` - declares the theme as a system component
* `theme.xml` - file used to recognise the theme

Magento 2 theme is in a single directory, instead of `skin` and `app/design`

`composer.json` integrate with composer as an optional step. More info on [composer integration in magento 2](http://devdocs.magento.com/guides/v2.1/extension-dev-guide/build/composer-integration.html)

`Admin` theme can also be edited with themes, not just `frontend`

## Configuration

- Websites - can have different themes of share a theme

Applying a theme `Stores -> Configuration -> Design -> Design Theme Select`

## Inheritance
