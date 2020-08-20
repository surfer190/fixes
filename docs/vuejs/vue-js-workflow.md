---
author: ''
category: Vuejs
date: '2020-06-14'
summary: ''
title: Vue Js Workflow
---
# Vue JS Workflow

* build process to optimise and write es6
* development server - test under realistic circumstances, lazy loading files

## VueCLI

* VueJS project templates

Templates:

* simple
* webpack-simple
* webpack
* browserify/browserify-simple

Install the cli: `sudo npm install -g vue-cli`

[Vue-cli quick info](https://github.com/vuejs/vue-cli)

eg: `vue init <template-name> <project-name>`

### Run dev server

`npm run dev`

### Folder structure

* `babel.rc` - sets up babel, transpiler for es6
* `index.html` - served file
* `package.json` - dependencies
* `webpack.config.js` - responsible for build

Source folder: `src` 

* `App.vue` - single file templates

The [render function](http://vuejs.org/guide/render-function.html)

## Vue Files structure

`App.vue`: [single-file-components](http://vuejs.org/guide/single-file-components.html)

Template: `<tempalte>...</template>`
Script: `<script>...</script>` - works as vue instance
style: `<style>...</style>`

## Debugging

Use the [vue-devtools](https://github.com/vuejs/vue-devtools)