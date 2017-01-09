# Magento 2 Fundementals: Rendering

## Templates

Handle HTMl, JS and some PHP

templates are `*.phtml` files

## Blocks

Move reusable functionality from PHP temalte files into classes for reuse

Blocks provides data to template. Blocks instantiate models to query database.

## UiComponents

rendered by Javascript, but still depend on backend to obtain data

## Design layouts

pull together entire set of template files to be rendered in browser

## Process flow

`Gather layout Configuration -> Generate page layout XML -> Generate blocks -> Execute output blocks ->
Include tempaltes -> Execute child blocks -> Flush output`

2 rendering systems:
* rendering layout like magento 1 - `View::loadLayout()` and `View::renderLayout()` (ResultInterface)
* page objects

Page object:
1. controller execute until `ResultFactory::create()` is created and returns a page object.
2. Application goes back to object and runs `Page::renderResult()`

Result Object:
* Page : `Magento\Framework\View\Result\Page`
* Json : `Magento\Controller\Result\Json`
* Forward: `Magento\Controller\Result\Forward`
* Redirect: `Magento\Controller\Result\Redirect`

Result object: most important `rednerResult()`

`Magento\Framework\View\Result\Page` extends `\magento\Framework\View\Result\Layout`,
extends `Magento\Framework\Controller\AbstractResult` that implements `ResultInterface`

`Page::renderPage()` includes the `rootTemplate`

The root template is found: `Magento/Theme/view/base/templates/root.phtml`

### Page Objects

2 steps: `build` and `render`

3 actions:
* `loadLayout()`, `generateLayout()`, `loadLayoutBlocks()`

### View Elements

* UiComponents
* Containers
* Blocks

### UiComponents

standalone reusable elements

Used for: grids, forms, minicart

Related to JS

### Containers

* Doesn't have any classes related to it
* Renders all its children
* Allows configuration of some attributes (wrapping tag / css class)

## Blocks

Every web page is a hierachy of blocks that can have any number of content blockd or child containers

Role:
* Change look and feel of website
* Add something to the page
* Change the style of certain elemnt on a page
* Change data on a page

Magento 2 structure is more complex. Structure is defined by layout xml files

In a template, access to block's instance provides access to the data:

## Block Architecture and Life Cycle

`BlockInterface -> AbstractBlock`

### AbstractBlock Methods

* `_prepareLayout()` - method executed when a block is created.
* `addChild()` - For hierachical layout
* `_toHtml()` - before rendering
* `_beforeToHtml()`/`_afterHtml()`/`toHtml()`

`toHtml()` needs to be implemented. Not final. Not recommended to override.

Overriding `_toHtml()` is recommended

### Block Types

* Text
* ListText
* Messages - list of messages, can have a template
* Redirect - template block, renders javascript redirect
* Template

### Template: Assigning a template file

* `setTemplate()` - when you have physical access
* Constructor argument - `$data['template']`

In magento 1 all templates are included in the body or a block.
In magento 2, you can specify another object as the data container for a template.

### Creating or customising blocks

* Using layout: `$layout->createBlock()`
* Using object manager: No need for declaration
* Can be customised using DI/PLugins

### Lifecycle of block

1. Generating
  * instance of all blocks based on layout are created
  * structure built, child blocks set
  * `_prepareLayout()` called for every block
  * Nothing rendered
2. Rendering
  * `toHtml()`

### Generators

* `View\Page\Config\Generator\Head`
* `View\Page\Config\Generator\Body`
* `View\Layout\Generator\Block`
* `View\Layout\Generator\Container`
* `View\Layout\Generator\UiComponent`


### UiComponent

A class and often a block which is why is has to be instantiated.

### Templates

Snippets of `html` code in `.phtml` format. The contains PHP elements such as `PHP instructions`, `variables` and `calls for methods of some classes`

#### Location

In modules sub-folder: `view/<area>/templates`

eg. `app/code/Magento/Catalog/view/frontend/templates/product/view/details.phtml`

**Best practice**: Prepend the template with the module name

```
  catalog/product/view/price.phtml becomes
 Magento_Catalog::catalog/product/view/price.phtml
```

#### Variables

In template a calls from a block are made with: `$this->getSmth()`

which calls the corresponding function in the block

In magento 1 `function getSmth()` could be public, protected or private. In magento 2 a tamplte can only call a public function.

Template is rendered with `Block::_toHtml()` goes to `fetchView()` then to `templateEngine::render()` to include the filename.u can create and rewrite new themes as a core template in the module

Template file included in the template engine: `Magento\Framework\View\TemplateEngine\Php`

#### Fallback

Defining a full path to a file given only its relative path.

`product/view/details.phtml` > `Magento_Catalog/view/frontend/templates/product/view/details.phtml`

uses `getTemplateFile()`-> `Block::fetchView()`, `engine::render()` and includes filename($failname)

`Block::getTemplateFile()` is crucial

The real work of finding remplate is in `Magento\Framework\View\Filesystem` class

#### Customising templates

3 steps in rewriting the core template:

1. Create your module
2. Create a new template in your module
3. Set your template to the block that contains the core template to rewrite

### Layout XML Structure

Build pages in modular and flexible manner.

#### Design pattern

2 step view:
* Gather and arrange content in logical structure
* Generate HTML output

Changes: each layout update resides in its own file so XML syntax issues much easier to identify

Module can add content to existing pages without changing other modules. It can remove and move conent added by other modules.

#### Page Sections

* Head
* Body (Visible to visitors)
* Html
* Update - used to include more page processing instructions in seperate files, to avoid code duplication

In magento 1 layout xml could describe any content. In magento 2, layout xml is just for HTML.

Still possible to overwrite files but it is now non-default behaviour. Not recommened because of upgrade issues.

Layout of page is determined by containers - which act as a framework and don't caontain acual content.
Blocks are content within containers.

XML structure is generated by merging the layout XML files within one design area.

Layout files can be found in 2 places:
* Modules - `app/code/[Namespace]/[Module]/view/[area]/layout/*.xml`
* Themes - `app/design/frontend/[Namespace]/[theme]/[Namespace]_[Module]/layout/*.xml`

In magento 2 the base theme is now the module directory instead of `base/default`. Now each layout file is identified with a module.

Root nodes:
* `<page>` - Renders complete html page. (html, body, header, update)
* `<layout>` - Only a section of an html page (does not allow other nodes inside)

Eg. Page:

```
<page>
  <html>
    <attribute name="lang" value="en">
    <attribute name="data-page-id" value="123"/>
  </html>
</page>
```

renders: `<html lang="en" data-page-id="123">`

### Head

#### JS

In Magento 2, `$layoutContent` is included in the `<body>` tag, while `<head>` section is rendered using `head` section.

In `head/script`:

```
<script src="require/require.js"/>
<script src="Training_Render::example.js"/>
```

#### CSS

It can take a firect file name of module name:

In`head/css` element:

```
<css src="media/gallery.css">
<css src="Magento_Core::prototype/magento.css">
```

#### Link

Attributes:
* src
* ie_condition
* defer

```
<link src="jquery/jquery-1.8.2.js"
```

#### Removing an element

`<remove src="prototype/prototype.js">`

#### Title

`<title>My Title</title>`

#### Meta

`<meta name="keywords" content"coffee, drink">`

### Body

You need to explicitly state what is being to refereed to `<referenceBlock>` or `<referenceContainer>`

#### Container

Atrrbiutes:
* name (required)
* htmlTag
* htmlClass
* htmlId
* label

`<container name="additional.info" htmlTag="div" htmlClass="grey-box" htmlId="custom-content" label="Additional Content"/>`

creates: `<div id="custom-content" class="grey-box">`

#### ReferenceBlock

In `body/referenceBlock`:

```
<block class="Magento\Backend\Block\Template" name="training_render" as="example" after="system_messages" template="Training_Render::some/rendering/template.phtml" />
```

Magento 1 the `<reference>` directive was probably the most important.

In magento 2 directives `<referenceBlock>` and `<referenceContainer>` function in the same way.

In `body/referenceContainer` (same as `referenceBlock` but is a `container`):

`<referenceContainer name="training.render.example"></refenceContainer>`

### Remove element

```
<body>
  <referenceContainer name="header" remove="true" />
  <referenceBlock name="menu" remove="true" />
</body>
```

### Ui_component

`<ui_component name="example">`

Fields required:
* name
* component

Ui_components are predefined generic blocks, most common use is in `adminhtml` grids

### Argument elements

```
<block class="..." name="...">
  <arguments>
    <argument name="title" translate="true" xsi:type="string">Edit Account</argument>
  </arguments>
</block>
```

It is then passed to the constrcutor part of `data` injected through the `object manager`

### Action element

```
<block...
  <arguments>
    <action method="setTitle">
      <argument ...
    </action>
```

attributes:
* name
* xsi:type

### Specifying argument arrays

Use `xsi:type=array`

```
<arguments>
  <argument name="triggers" xsi:type="array">
    <item name="registerSubmitButton" xsi:type="string">.action.submit</item>
  </argument>
</arguments>
```

### Layout XML: Loading and Rendering

#### Directories

**Layout**

* `app/code/*/*/view/frontend/layout/*.xml`
* `app/code/*/*/view/base/layout/*.xml`

**Theme**

`app/design/frontend/magento/blank/*_*/layout/*.xml`

#### Areas

Views within modules:
* base (shared between frontend and admin)
* adminhtml
* frontend

view in theme directories:
* adminhtml
* frontend

#### Page Layout

Used when creating a new page or changing layout

* 1column
* 2columns-left
* 2columns-right
* 3columns

### Themes

Recursively fetches theme's parent until theme with no parent is found...in `Magento\Theme\Model\Theme:getInheritedThemes()`

Themes can inherit other themes with `theme.xml` or in `composer.json` within the theme.

Theme inheritance (Not theme fallback) - btu they seem similar

#### Overriding layout XML files

A theme can completely replace a file from parent theme by placing the replacement file in the appropriate folder.

**Not considered good practice**

It adds upgrade obsticles

You have to specify the file you want to override:

eg. `frontend/Magento/blank/*_*/layout/override/base/*.xml` or `frontend/Magento/blank/*_*/layout/override/theme/*/*/*.xml`

#### Layout Handles

Requests that render output are associated with one or more layout handles
Almost every request is assocaited with the default handle: `default.xml`

Page specific handles: consists of the route, controller and action

Eg:
* `catalog_product_view`
* `customer_account_login`
* `cms_index_index`
* `cms_page_view`

Many additional handles:
* `cms_index_index_id_home`
* `catalog_product_prices`
* `catalog_product_view_is_920`

Developers can add custom handles:

Use `Magento\Framework\View\Result\Page::addHandle('example_handle')`
Or using Layout XML: `<update handle="example_handle
