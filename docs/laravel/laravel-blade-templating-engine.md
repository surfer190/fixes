---
author: ''
category: Laravel
date: '2015-10-09'
summary: ''
title: Laravel Blade Templating Engine
---
# The Laravel Blade Templating Engine

* Separation of Concerns
* Simplified syntax for embedding logic in views

for `laravel` to recognise a file as blade it needs to end with: `*.blade.php`

## Adding Variables to Views

In the controller:

```
public function index(){
  return view('index')->with('name', 'Surfer190');
}
```

or with a `magic method`:

```
public function index(){
  $name = 'Surfer190';
  return view('index')->withName($name);
}
```

In the View:

```
<p>{{ $name }}</p>
```

## Sending Multiple Variables

In the Controller:

```
$data = array('name => 'Surfer190',
              'gitserver' => 'github.com');
return view('index')->with($data);
```

In the View:

```
Your User is {{ $name }} on {{ $gitserver }}
```

The above can get quite messy so it is suggested to use [PHP Compact](http://php.net/manual/en/function.compact.php)

Eg.

```
$name = 'Surfer190';
$gitserver = 'Github';

return view('index', compact('name', 'date'));

## Setting Default Values in View

```
                                    Hello, {{ $name or 'my man' }}
```

## Escaping Dangerous Input

With the standard `{{ ... }}` syntax script tags etc are automatically sanitised

To make the output `raw` use the following syntax:

```
{!! 'My List <script>alert("spam spam spam!")</script>'}
```

## Looping over an Array

```
<ul>
  @foreach ($list as $list)
    <li>{{ $list }}</li>
  @endforeach
</ul>
```

An array could be empty so use a `forelse`

```
<ul>
  @forelse ($list as $list)
    <li>{{ $list }}</li>
  @empty
    <li>You don't have any lists saved</li>
  @endforelse
</ul>
```

## Conditional Logic

Quite stange syntax

```
@if (count($lists) > 1)
  <ul>
    @foreach ($list as $list)
      <li>{{ $list }}</li>
    @endforeach
  </ul>
@elseif (Count($lists) == 1)
  <p>You have one list: {{ $list[0] }}</p>
@else
  <p>You don't have any lists saved</p>
@endif


## Comments

```
{{-- This is a Comment --}}
```
