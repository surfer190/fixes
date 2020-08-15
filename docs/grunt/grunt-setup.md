---
author: ''
category: Grunt
date: '2015-01-18'
summary: ''
title: Grunt Setup
---
#How to Setup Grunt Build - Web Development Build Tool

You will require `node.js` that comes with `npm` the node package manager

##Install Grunt Globally

`npm install -g grunt-cli`

##Create local `packages.json` (in project folder)

`npm init`

##Install grunt to local project

`npm install grunt --save-dev`

###`--save-dev` indicates development dependencies

##Templates for boilerplate grunt

`npm install -g grunt-init`

##Make a [grunt-init template](http://gruntjs.com/project-scaffolding)

`mkdir ~/.grunt-init`

##Clone existing - jQuery example

`git clone https://github.com/gruntjs/grunt-init-jquery.git ~/.grunt-init/jquery`

`grunt-init jquery`

##Useful Plugins:

JSHint - js code linting
Uglify - minification
Concat - combine files
Watch - watches for changes automatic building
Nodeunit - nodejs testing framework

`npm install grunt-contrib-jshint --save-dev`
`npm install grunt-contrib-uglify --save-dev`
`npm isntall grunt-contrib-concat --save-dev`