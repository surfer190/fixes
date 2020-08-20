---
author: ''
category: Laravel
date: '2015-10-28'
summary: ''
title: Laravel 5 Models
---
# Laravel 5 Models

A good application is model centric - models are what view and controllers are based on.

Database settings are found in `config/database.php` but most environment variables used can be set in `.env`:

```
DB_HOST=localhost
DB_DATABASE=myproject
DB_USERNAME=homestead
DB_PASSWORD=secret
```
_don’t forget to create the database because Laravel will not do it for you_

Object Relational Mappers (ORM's) are used to map application obejcts to databse obejcts.
Most ORMs come with common functions such as: querying, inserting, updating, and deleting records, managing table relationships, and dealing with other aspects of the data life cycle

### Creating a model with a migration

`php artisan make:model MyModel -m`

**Note**: Like most web frameworks, Laravel expects the model name to be singular form (Todolist), and the underlying table names to be plural form (todolists).

### Migrations

Migrations offer a file-based approach to changing the
structure of your database, allowing you to create and drop tables, add, update and delete columns,
and add indexes, among other tasks. Further, you can easily revert, or roll back, any changes if a
mistake has been made or you otherwise reconsider the decision. Finally, because each migration is
stored in a text file, you can manage them within your project repository

Migrations are found in `database/migrations`

The methods in migrations are `up()` (redo) and `down()` undo.

* $table->increments('id'): The increments method indicates we want to create an
automatically incrementing integer column that will additionally serve as the table’s primary
key.

* $table->timestamps(): The timestamps method informs Laravel to include created_at and
updated_at timestamp columns, which will be automatically updated to reflect the current
timestamp when the record is created and updated, respectively.

Adding a string column:

`$table->string('name');`

##### Running Migrations

`php artisan migrate`

Undoing a migration

`php artisan migrate:rollback`

##### Checking Migration Status

`php artisan migrate:status`

# Models

Virtual Attributes (Fullname does not exist in the database):

```
public function getFullnameAttribute()
{
  return $this->first_name . " " . $this->last_name;
}
```
eg.

```
$list = User::find(12);
echo $list->fullname;
```
