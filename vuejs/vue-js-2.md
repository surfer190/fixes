# VueJs

### Why javascript? 

It runs in the browser

### Why use vue?

- lean, small (16 kb)
- fast at runtime

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

- Core of vue application
- Control their own template of HTML
- Pass a javascript object to constructor

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

- Creates a template based on html code, which it uses to create the real HTML rendered as the DOM
- The html is the layer in the middle, not the same html in the DOM

Access to `data` object properties of `Vue` instance are accesses by their variable name eg. `{{ title }}`

Can also run `methods` inside templates eg. `{{ sayHello() }}`, but has to be something that can be converted to string

## Accessing data in Vue Instance

Accessing data and methods from the `Vue` object is done though the `this` keyword. Even though the title may be a property of the `data` object it is accessed with `this.title` within the `Vue` Object

**Cannot use curly braces (parenthesis) in any html element attribute**

Need to use `v-bind`: eg: `v-binf:href="link"`

All instances of a variable change in the DOM when it is updated

Adding `v-once` to an element will not be updated later on.
Eg. `<p v-once>{{ title }}</p>`

## Html elements as data attributes - Output Raw HTML

By default Vue escapes html. However if there is a case where you know it is safe.

Use `v-html` Eg. `vhtml=finishedLink`

## Events

Use the `v-on` keyword

You can listen to any event available for that DOM element

eg.

          <button v-on:click="increase">Click me</button>

### How do we access the default event object created by the DOM

Well it is passed automatically to all vueJS methods from `v-on`

## How do you pass your owner argument

          <button v-on:click="increase(2)">Click me</button>

          ...
          methods:
            increase: function(step){
                ...
            }
          ...

## Passing both your own argument and the default event object

Use the protected `$event` variable

          <button v-on:click="increase(2, $event)">Click me</button>

          ...
          methods:
            increase: function(step, event){
                ...
            }
          ...

## Event Modifiers

Vue has a function in between

- `.stop` - stop Propagation
- `prevent` - prevent Default

Eg.

            <span v-on:mousemove.stop>DEAD SPOT</span>

## Key modifiers

Only avaialble for keyboard related events

Listen only for `Enter keyup`

Eg.

          <input type="text" v-on:keyup.enter="alertMe">

## Writing javascript in template

Wherever you can access your Vue instance, you can run any valid single javascript expression and does not contain an `if` or `loop`

Can also put ternary expressions there

Eg. 

        {{ counter > 50 ? 'Hello' : counter++}}

## Two way data binding

Is done by using the `v-model` directive

## Reactive

**Data is not reactive**

### Computed

Another option for VueJS constructor called `computed`

Where functions are declared but are used like properties in data object

Computed properties is aware of data that has changed and whether the function should be rerun

        new Vue({
            computed: {
                functionName : function(){
                    
                }
            }
        })

### Watch

Set up property name you want to watch

Specific code you want to execute when property changes

Computed properties always need synchronous tasks. For asynchronous tasks you msut use **watch**

**Best practice** to use `computed` as they are more optimised

        new Vue({
            watch: {
                counter : function(value){
                    
                }
            }
        })

keyword `this` is not available in a callback closure

**You can also watch a computed variable**

## Shorthand

- Events - can replace `v-on` with `@`

Eg. `@click=...` === `v-on:click=...`

- Bind - replace `v-bind` with `:`

Eg. `:href` === `v-bind:href`


#### Source

Udemy Vuejs 2 Course