---
author: ''
category: Laravel
date: '2015-10-09'
summary: ''
title: Creating A Controller
---
# How to Create a Simple Controller, Action and Route with Laravel

```
php artisan make:controller <Name>Controller
```

When creating a controller laravel by default stubs actions of RESTful resources.
You can override this behaviour using `--plain`

```
php artisan make:controller --plain <Name>Controller
```

This creates `app/Http/Controllers/<Name>Controller.php`

## Creating actions

Actions are controller class methods that respond to an application endpoint address.

```
class NameController extends Controller
{
  function index()
  {
      return view('name.index');
      //The view file needs to be name/index.php
  }
}
```

## Setting up a default route to display

```
Route::get('/', 'NameController@index');
```

This route tells laravel to respond with a `GET` request, on the `/` route ie. homepage.
To serve up `NameController` `Index` Action
