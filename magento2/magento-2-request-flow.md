# Magento 2 Request Flow

Request flow - sequence of steps an application takes to process and respond to requests

Required:

`index.php -> Bootstrap -> App Class -> Routing`

Sometimes:

`Controller processing -> Rendering (Container and blocks) -> Output (HTML)`

## Initiation

Init phase: Setting u pkey objects: bootstrap object, app object, dependency injection, object manager, log configs etc.

Multiple entry points: `index.php`, `pub/cron.php`, `pub/static.php` and `shell commands (bin/magento)`

Cron calls go through: `ub/cron.php`

Calls to satic files go through: `pub/static.php`

There are 2 `index.php` files:

* `<root>/index.php`
* `<root>/pub/index.php`

The `Bootstrap.php` file registers the `autoloader`

Bootstrap creats the `ObjectManager` factory: `ObjectManager::create()` - `di` initialisation happens in the same call

`$app = $bootstrap->createApplication('Magento\Framework\App\Http');`

create the application

`PublicFunction::launch()` are similar to `$major->run()` and `$app->run()` methods in magento 1.

## Routing Phase

routing - converts a request URL into a style magento can handle and finds class to process it

Goals:

* Defining all avialable routers
* Converting a URL to Magento style
* Parsing request parameters
* Identifying an action class that will process the URL

Controller - class that contains the `execute()` method

Router - class responsible for handling certain types of URL's

Magento style URL: `3 parts` + parameters

Eg. `catalog/product/view/id/5`

### Route declaration

route - declaration of set of pages belonging to a particular module

Defined in `routes.xml`

### Controller Processing

Controller does not manage data, it manages the parameters and exceptions. It may initiate a main class for category pages.

Launches the rendeing process between view and data layers in production.

## Steps in rendering and flushing output

* Front controller (`Magento\Framework\App\FrontController`) dispatches request and gets result object.
* The app (`Magento\Framework\App\Http`) in the `launch()` method copies html to response object.
* The bootstrap (`Magento\Framework\App\Bootstrap`) flushes html from response object to browser.

There are multiple result objects that a controller can return.

**Best Practice**: It is recommended to return a `Magento\Framework\Controller\ResultInterface`

# Request Routing

## Front Controller

front controlers are used to efficiently handle requests and direct work flows across all pages

responsibilities:

* gathering all routers
* finding matching controller/router
* obtaining generated HTML to the response object

In magento 2, URL rewrites are implemented by a router

### High level execution flow

`index.php -> Bootstrap::run() -> App::launch() -> FrontController::dispatch()`

disPatch:

`router::match() -> Controler::execute() -> View::loadlayout() -> View->renderLayout() -> Response::sendResponse()`

### Routing Mechanism

`Router::match()` most useful when looking for the list of routers.

Available routers:

* Base router: `Magento\Framework\App\Router\Base`
* Default router: `Magento\Framework\App\Router\DefaultRouter`
* CMS router: `Magento\Cms\Controller\Router`
* URL rewrite router: `Magento\UrlRewrite\Controller\Router` (new)

The Base router extends `RouterInterface`

Base router is located `lib/internal/Magento/Framework/App/Router/Base.php` (Not in the code)

The router interface is simple in structure; it contains a single method, Router::match()

The default router: `Magento/Framework/App/Router/DefaultRouter.php` handles **Not Found** pages.
Magento 2 allows different handles for "Not Found" pages, eg. `Sorry, this product does not exist` or `This category does not exist`

### UrlRewrite Controller

In magento 1 URL rewrites is implemented in frontController.
In magento 2 we have a seperate router for processing URL rewrites.

### Order of Routing

1. `frontControler::dispatch()`
2. `Base Router`
3. `CMS Router`
4. `URL Rewrite Router`
5. `Default Router`

### Registering a new router

1. Add it as a parameter to class `Magento\Framework\App\RouterList` by using `etc/frontend/di.xml` of the module

### URL Processing

In magento 2 a single product can have multiple URL's for SEO and human reading optimization

Structure of URl acceped by base router is:

`$baseUrl/$frontName/$controllerName/$actionName/$otherParams`

eg: `http://magento.dev/catalog/product/view/id/1`

### CMS Router

Pertanent code:

```
$request->setModuleName(‘cms’)
->setControllerName(‘page’)
->setActioName(‘view’)
->setParam(‘page_id’;$pageid);
```

### Exercise: modify the not found page to forward to the home page

Easiest way is to change `/web/default/noroute`

## Controller Architecture

Controller is a class specific to a URL or group of URL's

A Controller can only process a single action. One class per action.

Eg. `Magento\Catalog\Controller\Product\View`

### Action classes / Controllers

Action classes include:

* execute() method
* Constructor (dependencies injected using DI)
* Extra methods and variables

Usually extends `Magento\Framework\App\Action\Action`. Which itself extends `Magento\Framework\App\Action\AbstractAction` which implements `Magento\Framework\App\ActionInterface`

`ActionInterface` has two methods: `dispatch()` and `getResponse()`

### Action\AbstractAction

* Obtains request and response objects using DI
* Contains the method `getRequest()` and `getResponse()` - msut call parent class

### Action\Action

* Implements `dispatch()` method

### High Level execution flow

* Router::match() -> Controller::dispatch() -> Controller::execute()

### Action Wrappers

If controller does not extend `Action/Action` but directly implements `ActionInterface`, it must implement `dispatch()` method with specific logic.

### Key result objects

* Page: Html output `$page = $this->pageFactory->create()`
* Json: For JSON database `$result = $this->jsonFactory->create(); return $result->setData($data);`
* Forward: internal redirect to another controller `$result = $this->forwardFactory->create(); $result->forward('some/new/route'); return $result;`
* Redirect: Physically redirect customers browser to another URL: `$result = $this->redirectFactory->create(); $result->setUrl('some/new/url'); return $result;`

### Types controllers

* Frontend
* Backend - must support ACL

### Backend AbstractAction

* Constructor with extra objects injected
* Contains the new `dispatch()` method
* Contains the `_isAllowed()` method
* own implementation of `redirect()` and `forward()`

### Asigned Modules

`routerConfig` is injected with `DI`

`matchAction()` will perform 2 calls:

* `Router\Base::matchModuleFrontName()`
* `Router\Config::getModulesByFrontName()`

### Debugging the matching controller process

1. Check the `frontName` is correct
2. Check the list of available modules
3. Check path name for each module
4. Check whether controlled being debuged is listed and whether class exists

### Creating controllers

1. Create `routes.xml`
2. Create the correct action class and implement an `execute()` method
3. Test

**routes.xml**:

```
<?xml version="1.0"?>
<!--
/**
 * Copyright © 2016 Magento. All rights reserved.
 * See COPYING.txt for license details.
 */
-->
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="standard">
        <route id="catalog" frontName="catalog">
            <module name="Magento_Catalog" />
        </route>
    </router>
</config>
```

speifiy the `id` of the router, the `frontName` and the `module` name

`standard` means the `base` router

Above tells magento it is ready to process URL that starts with `catalog`

- frontName is connected to the module
- ActionPath is connected to the folder/subfolder of Controller folder of module
- Action is connected to the PHP class

Controller must extend `Magento\Framework\App\Action\Action` and must implement `execute()`

#### Testing

Enter the URL: `frontName/actionPath/action`

#### Customize existing controllers

Controllers are same as any other class in Magento 2. So customised in the same way using `preferences` or `plugins`

### URL Rewrites

Making complicated URL's more user-friendly: shorter, more descriptive and easier to remember

Magento allows you to specify a `URL key`

### Process Flow

Browser sends request to server which requires `Magento\UrlRewrite\Controller\Router`

Then it accesses the database: `url_rewrite`

Url Finder is an instance of `Magento\UrlRewrite\Model\Storage\DbStorage`

### Exercise: Add a rewrite for the 'Hell World' Controller

`INSERT INTO url_rewrite SET request_path=’testpage.html’, target_path=’test/action/index’,
redirect_type=0, store_id=1, is_autogenerated=0;`
