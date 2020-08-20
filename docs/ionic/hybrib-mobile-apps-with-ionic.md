---
author: ''
category: Ionic
date: '2020-06-21'
summary: ''
title: Hybrib Mobile Apps With Ionic
---
# Hybrid mobile applications with Ionic Framework

## Introduction

Open source frontend SDK (Standard Development Kit - Tools to develop) to develop hybrid mobile applications with web technologies

It is a web app run within a **native web view component** which has access to the **native API**'s, it is then compiled into the native app. The ionic framework provides lookalike native components.

Ionic is built on top of **Apache Cordova**, an open source framework allowing developers to access native device functions eg. camera, accelerometer from JS.

## Knowledge requirements

- HTML5
- CSS
- JS
- Angular

## Setting up Environment

- [Install node js](https://nodejs.org/en/download/)
- [Install git](https://git-scm.com/)
- Install Cordova

```
sudo npm install -g cordova
cordova -v
```

- Install Ionic

  ```
  sudo npm install -g ionic
  ionic -v
  ```

- Install native mobile SDK's
  - for iOS you need [Xcode](https://developer.apple.com/xcode/)
    - Install Command line tools: `Xcode -> preferences -> Components -> Select ones you want`
    - iOS Simulator: `sudo npm install -g ios-sim`
    - iOS Deploy: `sudo npm install -g ios-deploy`
    - Provision phone for development - sign up as apple developer (**$99 a month fee** Madness!!)
  - for android you need [Android SDK](http://developer.android.com/sdk/index.html) just need SDK android studio application is not required
    - Add the extracted folder `tools` and `platform-tools` to your bash path
    - Check by running `android` in terminal - should open the Android SDK Manager
    - Minimum requirements:
      - Android SDK Tools
      - Android SDK platform-tools
      - Android SDK build-tools
      - SDK Platform (Any android version preferably the latest stable)

## What you need to know about Angular JS?

[Key Knowledge required about Angular JS](https://doolan.pw/key-knowledge-angular-js)

## Start a New Ionic App

`ionic start <appname> <template>`

**Note**: If app name has a space, rather edit this later leave it as unspaced here

`<template>`: 3 default `tabs`, `sidemenu`, `blank`

### Directories

- bower.json
- config.xml - configure settings for cordova
- gulpfile.js - taskrunner
- hooks/ - execute user scripts during build ([Read cordova docs](https://cordova.apache.org/docs/en/5.0.0/))
- ionic.project
- package.json - dependencies
- platforms/ - native applications are compiled and stored
- plugins/ - cordova plugins
- scss/ - style
- www/ - application html, css and js (**Where you will code**)

##### Components

Check the [extensive ionic docs](http://ionicframework.com/docs/)

## Ionic CLI

Getting help: `ionic help`

#### Local development server

Preview app in browser

`ionic serve --lab`

`--lab` says display as iOS and android

#### Ionic View

Free app on play store or app store to test apps

Need an [ionic.io account](https://apps.ionic.io)

## Developing the ionic App

Ionic adds iOS as a platform automatically. To add `android` use:

```
ionic platform add android
```

#### Style classes

- Styles are named by mood, not colour
- positive, calm, energised, balanced, assertive, dark

#### Best practices

- Ionic will try and keep native as much as possible

#### Ionic hints

For code hints and snippets if you are using Atom use [Ionic atom plugin](https://github.com/imsingh/ionic-atom-plugin)

#### App.js

The structure of the default controller

`angular.module('starter', ['ionic'])` - injects ionic framework and starter module

`run()` function - executes when the entire framework is ready (`document.ready()..`)

## Ionic Icons

Check out the [Ionic Icons](http://ionicons.com/)

Base button class is `button` to use an ionic icon as a button use `button button-icon`. Also add the ionic icon class.

## Extending the App with Firebase

Can store locally with `cookies`, `local storage` or `web sql`

Google owns firebase - synergy with angular

##### firebase

- Real-time json database
- tools to authenticate
- rapid dev
- `angularfire` 3-way data binding

#### Setup

In **index.html**:

Add the firebase js after `ionic.bundle.js` asit requires some ionic stuff

```
<script src="https://cdn.firebase.com/js/client/2.4.2/firebase.js"></script>
```

In **app.js**:

Inject firebase

eg.

```
angular.module('starter', ['ionic', 'firebase'])
...
```

Create a factory service to point to your firebase url:

```
.factory('Items', ['$firebaseArray', function($firebaseArray){
  var itemsRef = new Firebase(
    'https://your-url.com/items'
  );
  return $firebaseArray(itemsRef);
}])
```


#### Source

[Hybrid Mobile App Development with Ionic](http://shop.oreilly.com/product/0636920046141.do)
