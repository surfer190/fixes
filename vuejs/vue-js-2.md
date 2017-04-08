# VueJs

Why javascript? It runs in the browser

Why use vue?
* lean, small (16 kb)
* fast at runtime

## Vue Instance

        new Vue({
            el: '#app',
            data: {
                title: 'Hello World'
            }
        });

        <div id="app">
            <p>{{ title }}</p>
        </div>

Core of vue application
Control their own template of HTML
Pass a javascript object to constructor

## Directive

A command or instruction that vuejs will recognise

        <input type="text" v-on:input="changeTitle"/>

Add `method` to the Vue Instance

Remember the default `event` object is created by vanilla js

## Quick start

### JS

        new Vue({	el: 'div#app',
					data: {
          	title: 'Hello World!'
          },
          methods: {
          	changeTitle: function(event){
            	this.title = event.target.value;
            }
          }
        })

### HTML

        <script src="https://unpkg.com/vue@2.2.6"></script>

        <div id="app">
        <input type="text" v-on:input="changeTitle">
        <p>
            {{ title }}
        </p>
        </div>

## VueJS Templates

Creates a template based on html code, which it uses to create the real HTML rendered as the DOM
The html is the layer in the middle, not the same html in the DOM

Access to `data` object properties of `Vue` instance are accesses by simply their variable name eg. `{{ title }}`

Can also run `methods` inside templates eg. `{{ sayHello() }}`, but has to be something that can be converted to string

## Accessing data in Vue Instance

Accessing data and methods from the `Vue` object is done though the `this` keyword. Even though the title may be a property of the `data` object it is accessed with `this.title` within the `Vue` Object

**Cannot use curly braces (parenthesis) in any html element attribute**

Need to use `v-bind`: eg: `v-binf:href="link"`

All instances of a variable change in the DOM when it is updated

Adding `v-once` to an element will not be updated later on.
Eg. `<p v-once>{{ title }}</p>`

## Html elements as data attributes - Output Raw HTMl

By default Vue escapes html. However if there is a case where you know it is safe.

Use `v-html` Eg. `vhtml=finishedLink`

#### Source

Udemy Vuejs 2 Course