# Magento 2 API Info

## Service Contracts

Service contracts - set of interfaces for modules to delcate stard API's

* Improve upgrade process
* Formalise customisation
* Decouple modules

Magento 2 implements "Development based on interface", developer relies only on public methods declated in an interface

Modules communicate through the API

2 types: data API and operational API

### Data API

Provides access to a module's entity data

Located: `_MODULE_NAME_/Api/Data`

### Operational API

Actual operations on data

Located: `_MODULE_NAME_/Api`

### Magento 1 way

Had to read core code first and then make changes

### Magento 2 way

Customise a module using an API interface that communicates with the model without interacting directly with the core

Pros:

\* Customise based on documentation, not module internals
* Better decoupling
* Minimisng conflicts
* Ability to rely on interface not implmentation

Drawbacks:

\* More difficult to perform low-level customisation
* Implementation method can sometimes matter
* Can be difficult to debug
* Changes must be compatible with interfaces

## Services API

API provides structured form of communication between modules

Describe the sturcutre of API components:

\* Repository - equivalent service-level collections (typically using `getList()`)
* Business API - actual business operations
* Data API - May extend `AbstractExtensibleObject` (Does not extend of use any framework components)

These tasks use an API instead of a mageto 1 type object (collection):

\* Fetch a list of objects from a database
* To save or delete an object

### AbstractSimpleObject

Base class for many DTO objects (Similar to `Varien` but does not have magic get and setters)
Only `_setData()` and `_get()`
If created with `ObjectFactory` the `$data` array will be passed as a constructor argument

## Frameowrk API

### Repository and Business Logic API

#### Repositories

* Provide access to the database through the services API
* Unchanged with new releases
* Deals with data objects
* Provides high-level access to data
* Supports searchCriteria mechanism for filtering and sorting
* Does not provide low level access to the DB

The `getList()` method accepts a `SearchCriteria` instance

Magento 2 uses a number of smaller registries

If it does not exist in the registry then it is created with `CustomerFactory`

#### SearchCriteria

Public methods available within the `SearchCriteriaInterface`

* FilterGroups(filters)
* SortOrders(Sorts)
* PageSize(Limits)
* CurrentPage(Offsets)

## Data API

Goals:

* Simplify SOAP API
* Provide service-level access to module's data


**Note**: Cannot directly change interfaces. Instead change the interface's implementation.

`extension_attributes.xml`

`stock_item` is an extension attribute. If you request a stock item from a product object you get an extension object.

Can join tables

## Web API

There is an area for each web api: `webapi_rest` and `webapi_soap`

`webapi.xml` file

ACL options: `self` (customer data), `anonymous` (anyone) and `Magento acl`

3 types of authentication:

\* OAuth (SOAP)
* Token-based (REST)
* Session based

### SOAP OAuth

Access token must be created

WSDL url is: `host/soap?wsdl&services=ModuleInterfaceV1`

or `host/soap?wsdl&services=Module2InterfaceV1`

eg. `host/soap?wsdl&services=catalogProductRepositoryV1`

### REST web services

Make a token request
