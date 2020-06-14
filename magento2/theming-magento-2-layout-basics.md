# Theming Magento 2 Layout Basics

## Layouts

Pull together entire set of tempalte files to be rendered by the browser

View configuration is built into a structure.

* Page layouts and containers - header, left, main, right, footers
* Blocks - each feature on a page
* Content block templates (`.phtml`)
* Page configuration - content blocks assigned to containers

Extend layout, containing only changes you want.

Overriding base layout file can be done by mimicking the directory but it is not recommended and should be avoided.

### Overriding a base layout

In `<Vendor>/<theme>/<Namespace_Module>/layout/override/base/<layout1>.xml`

### Override a parent theme layout

In `<Vendor>/<theme>/<Namespace_Module>/layout/override/theme/<layout1>.xml`

### Where to find layout files

Order of layout files determined by `app/etc/config.php`
Determines the sequence of inherited themes
Iterated the sequence from last ancestor to the current theme

#### Core Layout Files

Module specific pagelayout in `./view/frontend/page_layout`

Page configuration and generic layout files in `./view/frontend/layout` and `./view/frontend/base`

#### Extending Page Layouts

`<Theme_dir>/<Namespace>_<Module>/page_layout/<layout1>.xml`

#### Override the theme file

In `<Vendor>/<theme>/<Namespace_Module>/layout/override/theme/<Parent_Vendor>/<parent_theme>/<layout1>.xml`

#### Adding and Extending Layouts (Melding)

Create an extending layout file that contains changes you want, instead of creating and mdifying many files.

Eg. To customise: `app/code/Magento/Catalog/view/frontend/layout/catalog_product_view.xml`

Add a layout file in your custom theme:

`app/design/frontend/<Vendor>/<theme>/Magento_Catalog/layout/catalog_product_view.xml`

#### Handles

Each page in magento has a list of layout handles assigned to it:

* Default: default.xml
* _Full action name_: `catalog_product_view.xml`
* Page specific handles: `catalog_product_view_type_bundle`

Check the [common layout customisation tasks](http://devdocs.magento.com/guides/v2.0/frontend-dev-guide/layouts/xml-manage.html)

For example to move `compare products` in `default.xml`:

```
<page ...>
  <body>
    <move element="catalog.compare.sidebar" destination="sidebar.additional" after="-" />
  </body>
</page>
```

## Different XML File Types

* Page layout - overall strcuture
* Page layout declaration - registers page layouts in Magento
* Page configuration - overall page config and head section (meta, css, js)
* Generic layout - rare, mostly used for ajax response content.

### Page layouts

* Contains blocks and containers
* Defined in `xml` files

Finding them: Grep search `<layout (.*?)page_layout.xsd">`

## Container

Sole purpose of assigning content strcuture to a page. Just included elements.

A block employs templates into a page.

`base` layouts are layout files provided by modules

Examples of page layouts:

\* `2 columns left`
* `2 columns right`
* `3 columns`
* `1 column`
* `empty`

`Products -> Categories -> custom design` to set the number of columns

`Products -> Catalog -> Design`

Product page layouts:

* `catalog_product_view_type_simple.xml`
* `catalog_product_view_type_virtual.xml`
* `catalog_product_view_type_grouped.xml`
* `catalog_product_view_type_gift_card.xml`
* `catalog_product_view_type_configurable.xml`
* `catalog_product_view_type_bundle.xml`

Class of the body tag usually points to layout handle used

### Instructions to Update page layouts

Check [Layout Files Types](http://devdocs.magento.com/guides/v2.0/frontend-dev-guide/layouts/layout-types.html)

* `<container name="">` - create new container
* `<referenceContainer name="">` - reference existing container element
* `<move element="" destination="">` - move an lement into a new parent container
* `<update handle="">` - include instrctions from another handle and execute recursively

### Page Layout Declararion

To use a layout you must set it in:

* modules: `app/code/<Namespace>/<Module>/view/frontend/layouts.xml`
* themes: `app/design/frontend/<Namespace>/<theme>/<Namspace_Module>/layouts.xml`

Use: `<layout id="layout_file_name">`

### Page Configuration

If you want to render a full page you want to use `<page>`. Otherwise use `layout`.

One or more of these sections can be declared:

* html
* body
* head
* update

## Customisation Tasks

### Change layout

Copy file and add to theme in same strcuture.

Remove all other nodes except the one you want to change.

### Including a static resource

1. Please `default_head_blocks.xml` into `app/design/frontend/<Vendor>/<theme>/Magneto_Theme/layout/default_head_blocks.xml`
2. Make customisations:

    <page ....>
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <css src="css/my-styles.css" />
        <link src="js/sample2.js"/>
      </head>
    </page>

### Include custom js (or css)

Place component in:

\* `app/design/frontend/<Vendor>/<theme>/web/js`
* `app/code/<Namespace>/<Module>/view/frontend/web/js`

Create a `requirejs-config.js` file in:

    <page ...>
      <head>
        <script src="js/sample2.js"/>
      </head>
    </page>

### Managing a container

Check out [layout instructions](http://devdocs.magento.com/guides/v2.1/frontend-dev-guide/layouts/xml-instructions.html)

Create a container:

`<container name="some.container" as="someContainer" label="Some Container" htmlTag="div"
htmlClass="some-container">`

Update a container:

    <referenceContainer name="some.container">
      ...
    </referenceContainer>

Remove a container:

    <referenceContainer name="container.name" remove="true" />

### Manageing a block

Declare a block:

    <block class="Magento\Module\Block\Class" name="block.name" template="template.phtml" after="-">
      ...arguments
    </block

Update a block:

    <referenceBlock name="some.block">
      <arguments...>
    </referenceBlock>

Remove a block:

    <referenceBlock name="block.name" remove="true" />

Rearranging blocks:

    <move element="block1.name" destination="container1.name" after="-" />

## Blocks

Move reusable functionality into classes for repurposing

Argument values in block can be accessed in template wit:

`get{ArgumentName}` or `has{ArgumentName}`

Eg. `$this->getCssClass()`

`class` attribute specifies class location for a block:

\* `app/code`
* `lib/internal`
* `vendor/`

### Reusable Block Classes

* `Magento\Framework\View\Element\Text`: Renders simple text
* `Magento\Framework\View\Element\Text\ListText`: Renders a list of child blocks
* `Magento\Framework\View\Element\Template`: Renders a PHTML file
* `Magento\Framework\View\Element\Html\Link`: Renders a link with various attributes

## Templates and Customisation

Templates are snippets of HTML code and PHP elements

Templates are lcoated in the module: `app/code/<Vendor>/<module>/view/_area_/tempaltes`

Can enable template hints

### Rewrite core template

1. Create your theme
2. Create a new template in your theme
3. Set your template to the block that contains the core template to rewrite

`<theme_dir>/<Namespace>_<Module>/templates`

### Change template a block uses

1. Copy `app/code/Magento/Sales/view/frontend/layout/sales_guest+form.xml` to `app/design/frontend/<Vendor>/<theme>`
2. Remove everything from the `<body>` tag
3. Add `<ReferenceBlock name="guest.form" template="guest/alternative_form.phtml" />`

### Create a template block

Create `app/design/frontend/<Vendor>/<theme>/Magento_Theme/layout/default.xml`

    <page ...>
      <referenceContainer name="content">
        <block class="Magento\Framework\View\Element\Tempalte" name="custom.name" tempalte="path/to/my/template.phtml">
      </referenceBlock/>
    </page>

## Template Security

### Prevent XSS (Cross site scripting)

* `$block->escpateHtml()`
* `$block->escapeQuote()`
* `$block->escapeUrl()`
* `$block->escapeCssUrl()`

### Escaping is not always necessary

* typecasting: eg. (int)$count
* output in single quotes
* output in double quotes without variables
