# Magento 2 Fundementals: Db and Models

## Databases

ORM - Object-relational mapping, technique to access a relational database from an oo language

Magento ORM:

* models - data + behaviour / entities
* resoure models - Data mappers for storage structure
* collections - model sets and related functionality (soring, paging)
* Resources - database connectors via adapters


Only models contain and minpulate data

Models encapsulate storage independent business logic. contain deprecated CRUD methods: `load(), save(), delete()` that delegate to the resource model. **Best practice**: models should be passed directly to CRUD methods on resource models.
Model cannot access db directly.

Resource models - storage related logic. Uses db adapter.

Advantages:

* decouple business logic from the storage layer
* Decouple storage schema from DB driver implementation (Data mapper)

Resource collctions - list of models of a specific type

Resource models access the database through `\Magento\Framework\Db\Adapter\Pdo` and `Zend_Db`

### Model-to-Resource Model

When creating a new model , it needs to know which resource model to us. Class name is specified using `_init()` method in `_construct()`. Which is required to support the inherited `AbstractModel` methods `getResource()` and `getCollection()`

To create a model, create a class and extend from `\Magento\Framework\Model\AbstractModel`

You no longer need to delcare the model, resource model, adapters and other config.

Use the `_init` single underscore, not the real souble underscore PHP constructor.
The `_construct` is also legacy from Magento 1 and is called by the real `__construct()` method.

### Resource Model-To-Database

Extends: `\Magento\Framework\Model\ResourceModel\Db\AbstractDb`

Need to define table name and primary key.

### Collection-To-Model

Extends: `Magento\Framework\Model\Framework\Model\ResourceModel\Db\Collection\AbstractCollection`

Need to specify which model it corresponds to and a matching resource model

### Models

Not all models are storage persistent. No need for models only in `/Models` directory. You can put them anywhere.

Model Type Interfaces - Declare setters and getters for API

Magento 2 models inherit automatically fired events: `_eventPrefix` and `_eventObject`

### Resoure Models

Load, save and delete data

ResourceConnection module (Enterprise edition) provides features to split the database by functionality for higher scalability.

### Collections

Collections have sorting etc and Lazy load

Close to the DB layer

Main issues it solves:

* Container for storing collections of objects
* Prevents unnecessary data loading
* Stores all objects during a session
* Provides an interface for filtering and sorting entities

eg: `array("lteq" => 'uk_')`

## Models

#### CRUD workflow - reading

`$resourceModel->load($model, $id, $field = null)`

* Requires an argument for retrieving records
* Always returns an object instance
* 2nd argument to select record based on proerty or column name

Categories and products (EAV based) can be loaded using `loadByAttribute($attribute, $value, $additionalAttributes = '*')`

`$model->_beforeLoad()` deprecated, better to use plugins into resource model

Difference between read/write adapters has been eliminated

`$model->afterLoad()`

`$model->updateStoredData()`

`$_hasDataChanged`

`$resourceModel->save()`

`$model->isDeleted()`

`$model->hasDataChenged()`

`$model->validateBeforeSave()`

`$model->beforeSave()`

`$model->beforeDelete()`

`$model->afterDelete()`

`$model->afterDeleteCommit()`

`isSaveAllowed()`, checks `_dataSaveAllowed`

`$model->afterSave()`

These all use `$resourceModel` now:

`$resourceModel->save($model)`

`$resourceModel->load($model, $id, $field = null)`

`$resourceModel->delete($model)`

## Setup Scripts and Setup Resources

Setup scripts are powerful to do db customisations and for setting configurations

Once magento runs the isntall script it woll never run it again, you need to write update scripts.

Module version is set in the `module.xml`: `setup_version` attribute

Processed module versions are registered in `setup_module` table

Check module status: `run bin/magento module:status`

## Install script

Syntax is the same as magento 1

### Data setup scripts

Split data setup with data by using data setup scripts.

Are run after all schema setup scripts are completed.

`$context` gives some information about the current module version

Module version status: `bin/magento setup:db:status`

### code

Needs:

```
$installer->startSetup();
$installer->endSetup();
```

2 ways to apply changes:

* `run()`: executes plain sequentially (Db specific)
* `$installer->getConnection()` : Using DDL operations through adapter

## EAV

EAV entity is an entity type that is persisted using the EAV database schema via the EAV resource model

* EAV based entity models also extend Magento\Framework\Model\AbstractModel, just like flat table entity models.
* EAV based resource models extend Magento\Eav\Model\Entity\AbstractEntity, rather than
\Magento\Framework\Model\Resource\Db\AbstractDb

### Resource methods

Additional methods:

* `getAttribute()`: `$product->getResource()->getAttribute('color')`
* `saveAttribute()`: `$product->setWeight(1.99)->getResource()->saveAttribute($product, 'weight');`
* `getWriteConnection()`: Interface to write adapter, read connection
* `getEntityTable()`: Contract to `getMainTable()`, EAV models implement `getEntityTable()`

No difference delcaring `EAV` based entity models

Declaring `EAV` resource models differ from flat table. Instead of intiializing the resource model with the main table name and primary key column. EAV resource models are intialised with the entity type code and the name of the DB connection resource to use.

Any additional data is read from `eav_entity_type` table

#### EAV load process

2 aspects:

* Managing relationships
* Managing content

1. Loads meta of the EAV
2. Concrete attribute values

For select/multi-select attributes: Magento 2 uses the table source model.
Loaded from `eav_attribute_option` and `eav_attribute_option_value`

#### Collection load specific method

* `addAttributeToSelect()` - Adds the attributes value table to select and attribute to result
* `addAttribute ToFilter()` - Joins the attribute table specific for this attribute and adds a filter condition
* `joinAttribute()` - Joins a value table ffrom an attribute from another entity

#### Saving EAV Structure

Similar to flat table except one additional layer `beforeSave()` and `afterSave()` calls the attrbiute backend model.

**Backend Type***:

* static: `entity`
* varchar: `entity_varchar`
* int: `entity_int`
* decimal: `entity_decimal`

Loading or saving from a specific ou use `getTable()`

Eg. `$product->getResource()->getAttribute($attributeCode)->getBackend()->getTable()`

## Attribute Management

`entity_type` specific properties are saved in `catalog_eav_attribute`

* `attribute_id`: Unique id from the `eav_attribute` table
* `entity_type_id`: ID of associated entity type
* `attribute_code`: unique for entity type
* `attribute_model`: optional alternate model to use
* `backend_model`
* `frontend_model`
* `frontend_input`
* `frontend_label`
* `frontend_class`
* `is_required`
* `default_value`

### Two aspects of EAV

Meta information: `Entity type`, `Attributes` amd `Attribute set and groups`
Content: `Entity records`, `Attribute values`

With the `Magento\Eav\Model\Config` class you can get info:

* `getAttribute($entityType, $attributeCode)` - get an attribute instance
* `getEntityType($entityTypeCode)` - Return the entity type instance

#### Standard attribute types

* `varchar`
* `text`
* `int`
* `decimal`
* `datetime`

Two examples of the methods that the Setup class implements are `addAttribute()` and `updateAttribute()`

`

* Creating a new table uses `Setup/InstallSchema.php`
* Making product attribute visible in "more info" tab:
`visible_on_front`
* Class type to fetch multiple records: `Colelction`
* Add new product attribute: `Setup/InstallData.php`
* Add a where clause into query generated by collection object: `addFieldToFilter()`
