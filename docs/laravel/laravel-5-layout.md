---
author: ''
category: Laravel
date: '2015-10-09'
summary: ''
title: Laravel 5 Layout
---
# Laravel 5 Layout

A master layout is used for a `master layout`, which typically consists of a header and footer, as well as a log and navigation bar.

## Creating a layout

- Create a directory: `resources/views/layouts`

- Create a file called `master.blade.php`

With the follwing basic content:

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome to Laravel</title>
</head>
<body>
@yield('content');
</body>
</html>
```

The `@yield` directive identifies the name of the section embedded into the template.

## Using the layout in Views

You will need to Add:

```
@extends('layouts.master')

@section('content')

<Content Goes here>

@endsection
```

to the top of each view that uses that layout

_Note: Dot notation to represent path_

## Defining Multiple Layout Sections

Eg. Main Content and a Sidebar
 `@section`

 `@show`: A shortcut for closing a section and immediately yielding it

 `@parent`: cause anything in the views sidebar section to be appended to that is the layouts sidebat section

 You can replace instead of append by removing the `@parent`

 ## View Partials

 Recurring views

 #### Declaring

 In `resources/views/partials/row.blade.php`:

 ```
 <tr style="padding-brrom: 5px;">
  <td>
    {{ $link->name }}
  </td>
</tr>
```

#### Using View Partials

```
<table class="table borderless">
  @foreach ($links as $link)

    @include('partials.row', array('link' => $link))

  @endforeach
</table>
```

## Integrating CSS and ECMAScript

Images, CSS and ECMAScript should be placed in the `public` folder.

You can use the `LaravelCollective/HTML` package but it seems a waste

No wonder it was removed from the framework but you can check the docs at [Laravel Collective](http://laravelcollective.com/) or on the [laravel Collective Github page](https://github.com/LaravelCollective)

## Bootstrap

They can't make up their minds whether to keep bootstrap as standard or not.

#### Use a CDN

You could just use a CDN though:

```
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
```

#### Or If you are Cool...

Where bootstrap is not prepackaged, [get bootstrap](http://getbootstrap.com) and download the source files.

Place unzipped contents into `resources/assets/less/bootstrap`

Then place the following at the top of `resources/assets/less/app.less`

```
@import "bootstrap/bootstrap";
```

The `@import` statement automatically compiles the less into `app.css`

_note: Laravel does not include bootstraps javascript files_

## Bootstrapper

I don't see what the fuss is about but you can try it if you want [Bootstrapper](https://github.com/patricktalmadge/bootstrapper)
