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
* Other modules
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















