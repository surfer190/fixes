## Magento 2 Fundementals of Development

### Six goals of Magento 2

* Streamline the customisation process
* Update the technology stack
* Improve performance and scalability
* Reduce upgrade efforts and costs
* Simplify Integrations
* Provide high quality, tested code and resting resources

Greater independence of modules (standalone)

#### Areas

Load only required config files

adminhtml, frontend, crontab, REST web api, SOAL web api, Install

entry point for `adminhtml` and `frontend` is `index.php`

**Exceptions**
1. Framework files not technically modular and some static files belong to a theme,
not a module.
2. Themes include all types of static assets connected to the magento rendering system.
Some assets are in the module folder and some are in the theme folder.
PHP code is mostly located in modules.
3. Layout files are `xml` define which elements should be on a page. Blocks are special PHP classes
that are usually connected to a template. A block class generates HTML using its template.
4. Each module has its own configuration files: `events.xml`, `routes.xml`, `acl.xml`...Magento merges
all these files together.
5. Dependency injection / object instantiation magic is a magento 2 feature. A new object is declared in
the constructor, magento will deliver the instance.
6. Naming conventions: routes need a special corresponding controller (and route in `route.xml`).
Layouts are also connected to route names.
7.
Events: fired in core, developers can add observers to that event.
Plugin: add specific behaviour to every public method of each class.

#### Folders

Config: `app/etc`: global config db credentials, enabled modules. Not module configuration.
Framwork: `lib/internal/Magento/Framwork`: low level code for logging, db interation, url processing
Modules: `app/code/magento`: Magento business logic and features
CLI tool: `bin/magento`: tool to clear cache etc.
Themes: `app/design`: defines how pages look
Dev tools: `dev`: tools that assist the developer like testing framework

#### Paths

* Modules

        composer install - `vendor/magento/module-*`
        cloned repo - `app/code/Magento/*`

* Framework

        lib/internal/Magento/Framework/*
        vendor/magento/framework

* Themes

        vendor/magento/theme-frontend-*
        app/design/frontend|adminhtml/Magento/*

Magento 2 can be installed by composer install or cloning the repo

#### File Types

Configuration files
PHP classes
Layout instructions (`*.xml`)
Templates (`*.phtml`)
Javascript modules (`.js`)
Javascript templates (`*.html`)
Static assets (css, images)

### Config files

custom config is inside modules `etc` folder - defines module behaviour
global, module and theme

### PHP classes

* `Model/resource` and `module/collection`: interact with db, magento 2 moving away towards api
* API interfaces: CRUD for modules entities,
* controllers: handle pages in accordance with MVC
* Blocks: special classes representing part of a page. Usually connected to a `.phtml` template file
* observers: Events fire during different places along its execution flow.
* plugins:wrapper around any public method of any class
* helpers: auxillary classes with useful functions
* setup/upgrade scripts: upgrade the db schema or add data
* UI components: Allows developer to create a component, an independent element on a page with its own backend part

### Dev Process

Class is placed somewhere along the execution flow, where some method gets executed.

* Adding class into class's constructor
* Creating a plugin
* Creating an observer

### Enabling custom code

* Create and register a module
* Run `bin/magneto setup upgrade` to executre setup/ugprade scripts
* modify core classes by creating a plugin
* Create observers
* Add your class to the core's class array in constructor
* Controllers
* System configuration

### Modules

Module is package of code encapsulating a particular busines feture or set of features

Magento 2 module is now in a single folder

Modules are organised per functionality and are smaller

Each module is independent

Located in:

* `app/code/<vendor>/<module_name>`
* `vendor/<vendor-composer-namespace>/<modue-name>`

Modules in vendor are regsitered with a composer autoload callback:

`\Magento\Framework\Module\Registrar::registerModule('<module name', __DIR__)`

Eg. Customer module is found `app/code/Magento/Customer`

Vendor and Module must start with an uppercase character

Code base: `/app/code/<Vendor>/<Module>`
Custom theme files: `/app/design/<area>/><Vendor>/<theme>/<Vendor_Module>`
Custom theme files: `/app/design/<Module>/<theme>`

#### Registering a module

* custom written modules are in `app/code` regardless of installation type
* Grouped by vendors
* composer installed core modules are in `vendor/magneto/module-*`
* Every module must have a `etc/module.xml` and a `registration.php`

#### Module.xml

Includes name, version and dependencies

it is located in modules `etc` folder. Other folders usually start with a capital letter.

```
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
		<module name="Vendor_ComponentName" setup_version="2.0.0"/>
</config>
```

[More info on module.xml](http://devdocs.magento.com/guides/v2.0/extension-dev-guide/build/create_component.html)

#### Registation.php

Instructions on how to find a module

```
ComponentRegistrar::register(ComponentRegistrar::MODULE, '<VendorName_ModuleName>', __DIR__);
```

[More info on registation.php](http://devdocs.magento.com/guides/v2.0/extension-dev-guide/build/component-registration.html)

### Module dependencies

* multiple modules can't be responsible for 1 feature
* One module cannot be responsible for multiple features
* modules explicitly declare dependencies
* theme dependencies must be declared
* disabling or removing a module does not remove others

Modules can be dependent on:

\* Other modules
* PHP extensions
* Libraries

Soft order dependencies are declared in `module.xml` other dependencies are in `composer.json`

Hard dependency: can't function without module

* uses code: instances, class constants, static methods, pubic class properties, interfaces and traits
* strings from another module
* deserialises object from another module
* uses or modifies datbase tables used by another module

Soft dependency: can function without

* directly checks another module's availability
* extends another modules configuration
* entends another modules Layout

#### Declaring module dependency

* Name and declare module (`module.xml`)
* Delcare dependencies in `composer.json`
* Define desired load order (`module.xml`) with `sequence` element- optional

### File System

* `app` - core code (cloned repo), custom modules, themes, global config
* `bin` - cli tool
* `dev` - tools for developers
* `lib` - external libraries not available in composer
* `vendor` - composer folder
* `pub` - public folder. `/static` folder for files
* `setup` - installation specific files
* `var` - cache, generated code, logs and other files (uploaded csv)

#### App Folder

* `app/etc` - global configuration
* `app/code` - custom modules (cloned repo - core modules)
* `app/design` - themes
* `app/i18n` - translations
* `app/Bootstrap.php`, `app/autoload.php`, `app/functions.php` important...begin execution process

#### File System

* `app/code/Magento/` - Core
* `lib/internal/Magento/Framework` - Framework

#### Module Folder

The only required folder is `etc`

* `Api`
* `Block`
* `Console`
* `Controller`
* `etc`
* `Helper`
* `i18n`
* `Model`
* `Observer`
* `Plugin`
* `Registration.php`
* `Setup` - upgrade scripts
* `Test`
* `Ui`
* `view` - layout xml, templates, static view files

##### View subfolder

* `frontend` - templates, layout, web (images, js, widegets.css, zoom.css)
* `adminhtml`
* `base`

[Typical module file structure](http://devdocs.magento.com/guides/v2.0/extension-dev-guide/build/module-file-structure.html)

#### Check

* Static files placed in theme rather than specific module when it is a general file affecting all pages.

### DevOps

#### Development mode

* static file materialisation not enabled
* uncaught exceptions displayed in browser
* exceptions thrown in wrror handler, not logged
* Logging in `var/report` highly detailed

#### Production mode

* Best performance
* Exeptions only written to log
* Disabled static file materialisation

#### Default mode

* Used when no mode specified
* Hides exceptions and writes to log files
* static file materialisation is enabled
* Not recommened for production, caching impacts performance negatively

#### Maintenance mode

* make site unavailable
* Set flag `var/.maintenance.flag`
* Can specifify people with access `var/.maintenance.ip`

#### Setting mode

* Use `nginx` environment variable

#### Command line tool

* Enable and disable: `magento module:enable <module-list>`
* Change caching `app/etc/env.php`
* Cleaning cache: from admin,using cli, manually removing cache files

### DI and Object Manager

Dependency Injection - Manage object dependencies by settings objects in current objects constructor
The object manager is responsible for creating the objects a class requires.

Lots of depedency limits code reuse and makes moving components to new projects difficult

Dependency injection is configuration that is XML-based and validated by XSD

Eg. You need a `storeManager` instance in the `Product` class. You can declare an argument with type
`StoreManagerInterface` in the constructor of the product.
Then using `di.xml` you have to define which class will be substituted for the interface.

> Constructor has a list of objects assigned to protected properties, then used inside a class.

### Class Instantiation

`di.xml` specifies the List or interfaces, classes and factories sent into `__construct()` method

THe best candidate to use `di` is a singleton-type class - only single instance but used in multiple places. Eg. Cache, session, registry, helpers. Factory / API classes als match this definition.

Not every class has to be injected. Eg. an entity class like `product` depends on data from database. So a `factory` is recommended for injecting.

eg.

```
public function __construct(\Magento\Catalog\Model\ProductFactory $factory) {
  $this->factory = $factory;
}

...

public function someFunction(){
  $product = $this->factory->create();
  $product->load($someId);
}
```

The **factor class may not exist**, when the DI mechanism identifies a class ending in Factory and it does not exist it generates it in `var/generation`

### Object Manager

A class that:

\* Creates objects
* Implements singleton pattern
* Manages dependencies
* Automatically instatiates parameters

Parameters - variables declared in the constructor signature
arguments - values passed to the constructor when the class instance is created

Has replaced the `Mage` class.

Magento 1 instantiation was centralised most classes created through `Mage` class and a config file.
4 Generic patterns:

\* Abstract Factory
* Factory Method
* Singleton
* Builder

For all `singletons` the `registry` was used, so you could request singletons from the registry, creating them if not present.

#### Magento 2

Object Manager has 2 methods: `get` and `create`.
Get method: return a singleton object called `Shared Instance` from protected registry.
Create method: creates a new instance of a given class

`Mage` was a static class always included in the beginning of the request flow. Now the object manager is no longer static or globally available.

Best practice to avoid calling the object manager directly.

#### Object Manager Usage

To use the `ObjectManager` include it in the constructor (`__construct()`)

Then assign it to the protected property and use it in your class:

`$this->objectManager = $objectManager`

`$objectManager->get(’Magento\Catalog\Api\ProductRepositoryInterface’);` will return the same implementation of... `ProductRepositoryInterface` as you would receive by including it in the constructor

You should not use `ObjectManager` in your code as it breaks the `DI` concept

#### Autogenerated Classes

`factory classes`, `Interceptors` and `proxies` are autogenerated.

Interceptor: class that allows plugin functionality to work. When you require a class that has a registered plugin, magento generates an interceptor with the same method as the required class but will call a plugin in that method.

Interceptors use PHP traits to extend both the abstract interceptor and the original class.

Proxy - tool that helps with circular dependencies, and relates to an internal implementation of how DI works.
So you won't have to deal with them directly.

#### Object Manager Configuration

Uses config from `di.xml` to define which instance to deliver into the constructor of a class

Each module can have multiple `di.xml` files - global or specific

* You need to use the **real class name including the PHP namespace** when you require an instance of a class
* Creation of objects is managed for you
* Recursively creates any arguments for the objects yourboject requires
* Declaring an interface in the constructor, the boject manager automatically creates the matching implementation for it.
* Thinking in terms of `interfaces` and not `implementations`

#### Where to specify object manager configurations

* Global across all of magento: `app/etc/di.xml`
* Entire module `<your directory>/etc/di.xml`
* Area specific configuration: `<your directory>/etc/<area>/di.xml`

Magento only uses 1 `di.xml`...the merged one

#### Defining preferences

* Preferences can be defined for interfaces and regular classes
* Preferences define which classes will be instantiated for a constructor argument of your class

**Best Practice** to request only interfaes and not concrete classes.

Eg. Request `\Magneto\Framework\App\Response\HttpInterface` instead of `\Magento\Framework\App\Response\Http`

#### Defining Arguments

There are different types of arguments: `string, array, object`
DI defines which objects should be used as an argument when a new instance is created

Sometimes you need a specific product but the object manager can only deliver a generic product.
It can't provide a loaded entity. As a result this object type is not injectable.

Some objects have to be gotten with the `object manager`

#### DI affecting parameters of a class

1. Define which classes correspond to certain interfaces. An interface cannot be instantiated, a class implements the interface. Using DI we can figure out exactly which class is being used.
Look at `\Magento\Catalog\etc\di.xml` search for `ProductAttributeRepositoryInterface`, a line substitutes `Magento\Catalog\Model\Product\Attribute\Repository` assigned to parameter `$metadataService`

2. Define a specific parameter for a specific class. Define a specific instance for a specific class. For products you may need a particular class only for products. Eg. magento data parameter. With `di.xml` we can add something to `data` parameter. So for `\Magento\Catalog\Model\Product\ReservedAttributeList.php` look at parameters of constructor and see `$productModel`. Now search `productModel` in `Magento/Catalog/etc/di.xml`

Example: So when instance of this class is created, `productModel` is set to the string `\Magento\Catalog\Model\Product`

```
<type name="Magento\Catalog\Model\Product\ReservedAttributeList">
    <arguments>
        <argument name="productModel" xsi:type="string">\Magento\Catalog\Model\Product</argument>
        <argument name="reservedAttributes" xsi:type="array">
            <item name="position" xsi:type="string">position</item>
        </argument>
        <argument name="allowedAttributes" xsi:type="array">
            <item name="type_id" xsi:type="string">type_id</item>
            <item name="calculated_final_price" xsi:type="string">calculated_final_price</item>
            <item name="request_path" xsi:type="string">request_path</item>
        </argument>
    </arguments>
</type>
```

#### Configuration Shared Argument

* shared object == singleton
* Use same instance of a class within several other classes

In `di.xml` if the node has `shared="false"` it won't be shared.

* Can use on both `type` and `argument` nodes with the `xsi:type="object"`

### Plugins

* Plugins extend / change the behaviour of a native method within a magento class
* Plugins change behaviour of original class, but not class itself
* Can't use with `final methods`, `final classes`, `private methods` or classes without dependency injection.

`plugins` allow you to modify a single method, `preference` allows you to change a whole class.

#### Customisations

* Events: commonly handle external actions or input
* Plugins: Allow you to customise a method. Executed sequentially.

Magento 1 used `events` and `rewrites`. Sometimes events not in correct places and too many events might cause many firing hurting response time. Class rewrites need a thorough understanding.

#### Declaring a plugin

Use `di.xml`:

```
<config>
  <type name="{ObservedType}">
    <plugin name="{pluginName}"
      type="{pluginClassName}"
      sortOrder="1"
      dsabled="true"/>
</config>
```

Required:

* `type name`: class, inheritance or virtual type the plugin observes
* `plugin name`: name identifying the plugin
* `plugin type`: name of plugin class or `virtual` type. Naming convention: `<ModelName>\Plugin`

Optional:

* `plugin sort order`: order that plugins calling the same method run
* `plugin disabled`: **true** to disable

> The syntax is very simple. The way it works: you define a plugin -- you create a class within another
class, then inside that class you can define which methods write the plugin. - MagentoU

* Before-Listener: Chnage an argument before a method is called

    public function beforeSetName(\Magento\Catalog\Model\Product $subject, $name){
        return ['(' . $name . ')'];
    }

* After-Listenenr: Add after

    public function afterSetName(\Magento\Catalog\Model\Product $subject, $result){
      return '|' . $result . '|';
    }

* Change arguments and returned values of original method use an **aroundlistener**

    namespace My\Module\Model\Product;

    class Plugin
    {
      public function aroundSave(\Magento\Catalog\Model\Product $subject, \Closure $proceed)
      {
        $this->doSmthBeforeProductIsSaved();
        $returnValue = $proceed();
        if ($returnValue){
          $this->postProductToFacebook();
        }
        retunr $returnValue;
      }
    }

* `$subject` provides access to all public methods of the original class
* `$process` is a ambda that will call the next plugin or method

further arguments passed to net plugin with `$proceed()`

Can also ovveride an original method (a conflicting change)

#### Sequence of plugins

1. `before` listener in plugin with highest priortiy (smallest `sortOrder`)
2. `around` listener in plugin with highest priorty
3. Other `before` listeners
4. other `around` listeners
5. `after` listneer of plugin with lowest priorty (highest `sortOrder`)
6. `after` listeners in reverse sort order

#### Configuration inheritance

We can create a module, make it dependent from the core module, and redefine preference for a certain interface.
Similar to a magento 1 rewrite.
Compiler tool can minimise the performance impact.

#### Interception

Object manager checks whether the are any plugins registered for any methods of a required class.
If so it generates an interceptor class.
Interceptor extends the original class but wraps its methods to all plugin to be called before, after or instead.
They are creted in `var/generation` folder

### Events

External actions

Event-observer pattern. Objects (subjects) and their list of dependents (observers). Events trigger objects to notify their observers of state changes.

Magento 1 used `Mage::dispatchEvent()`, magento 2 uses the special event manager class.

declared in `events.xml`

Eg. `Magento\Checkout\Model\OnePage` method `saveOrder()`:

    $this->_eventManager->dispatch(
        'checkout_submit_all_after',
        [
          'order' => $order,
          'quote' => $this->getQuote()
        ]
      )

Then in `Magento/CatalogInventor/etc/events.xml`:

    <event name="checkout_submit_all_after">
      <observer name="inventory" instance="Magento\CatalogInventory\Observer\CheckoutAllSubmitAfterObserver"/>
    </event>

#### Observer class

`Magento\CatalogInventor\Observer\CheckoutSubmitAllAfterObserver` and `execute()` function

    public function execute(EventObserver $observer)
    {
      $quote = $observer->getEvent()->getQuote();
      if (!$quote->getinventoryProcessed()){
        $this->subtractQuoteInventoryObserver->execute($observer);
        $this->reindexQuoteinventoryObserver->execute($observer);
      }
      return $this;
    }

event object contains event's parameters

### Module Configuration

Files split into funtion

* `app/etc/config.php` - delcaration of all modules
* `app/etc/env.php` - db connectino info

* `module.xml` - module declaration
* `config.xml` - default admin settings
* `events.xml` - observers and events they are subscribed to
* `di.xml` - dependency injection config
* `routes.xml` - lists the routes and routers

Auto completion for xsd

#### Storing config values

* Database: Merchants (`core_config_data`)
* ML files: Developers, technical config

Table `core_config_data` is the same as magento 1.

If scope is `website` then `scope_id` is treated as `website_id`
If scope is `store` then `store_id` for global scope does not apply

#### Configuration scopes

* Global: config file in `etc/`
* Frontend: `etc/frontend`
* Admin: `etc/adminhtml`

#### Load order of config files

* Primary: loaded on bootstrap (config for app start and install specific)
* Global: All config files common across all app areas
* Area-specific: Files that apply to specific areas such as `adminhtml`

#### Merging Config files

Merged based on Fully qualified Xpaths
Special attribute is defined in `$idAttributes` array
After 2 XML documents are merged, resulting document contains all nodes from the original files
Second XML file supplements or overwrites nodes in the first XML file

#### Validation

Each file is validated against a schema

Eg. `events.xml` is validated against `events.xsd`

Validated against: `lib/internal/Magento/Framework`

All config files are processed by `Magento\Framework\Config`. Loan, merge, validate and convert into array.

#### Interfaces to manage config files:

* `\Magento\Framework\Config\DataInterface` - config data within a scope
* `\Magento\Framework\Config\ScopeInterface` - Identifies current application scope
* `\Magento\Framework\Config\FileResolverInterface` - identies files read by `\Magento\Framework\Config\ReaderInterface`
* `\Magento\Framework\Config\ReaderInterface` - reads config from storage

#### Loading XML configuration

* `Config`: Class that is used to get access to the config values
* `Reader`: reads a file
* `SchemaLocator`: encapsulates path to the schema
* `Converter`: Converts XMl to array
* `XSD`: schema file

**New config files must be accompanied with an XSD validations schema**

#### Creating a custom config file

Requires:

\* XML file
* XSD schema
* Config PHP file
* Config reader
* Schema locator
* Converter


## Error Reporting

Magento uses strongest error reporting, even PHP notice will cause an exception
