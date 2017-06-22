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

## Attributes are Merged

You can have a `class` attribute on an element, but a bound attribute `:class` can also be added and vue js will manage it.

`<div :class="{red: attachRed}">`

With the `v-class` or `:class` bound value it expects a list or javascript object. 
`key` - name of class
`value` - true/false, whether to add that class

### Can also directly change properties

`<div :style="{ 'background-color':color }">`

And it bind to the `color` data attribute

#### Source

Udemy Vuejs 2 Course

## Conditionals

Actually removes or adds the element to the DOM (Including nested) based on a data field that resovles to true of false

Use **v-if=**

```
<p v-if="show">See me</p>
```

**Very important to use `v-if=` instead of `v-if:` as that will break html on the page**

Basically if html on the page is borked, then ensure it is formatted correctly

Can switch to the negative if we use `v-else`

No need for a condition on the `v-else`

#### Show or Hide instead of Removing or adding

Use `v-show=`

## Lists

`v-for=` directive

        <li v-for="ingredient in ingredients">{{ ingredient }}</li>

With an index:

        <li v-for="ingredient, index in ingredients">{{ ingredient }} ({{ index }})</li>

Can also put a `v-for` on a `template` element

### Loop through properties of Objects

        <li v-for="person in persons">
            <span v-for="value in person">{{ value }}</span>
        </li>

        <li v-for="person in persons">
            <div v-for="value, key, index in person">{{ key }}: {{ value }} - ({{ index }})</div>
        </li>

        new Vue({
            el: '#app',
            data: {
                ingredients: ['Meat', 'fruit', 'cookies'],
                persons: [
                    {name: 'Max', age:27 , colour:'red'},
                    {name: 'Anna', age:'unknown' , colour: 'blue'},
                ]
            }
        })

### Looping through a range of integers

        <span v-for="n in 10">{{ n }}</span>

### For loop and keeping track

Sometimes there are issues where updates are not where they should be or sorting is not correct.
This is due to be a reference to the value in memeory and not to the actual value.

So sometimes we need to bind the `:key=` directive

### Check if variable is an array

        Array.isArray(value)

## The Vue Instance in Detail

Multiple Vue Instances are allowed, as long as there is no connection between them.

Can store the vue instance in a variable with:

        var vm1 = new Vue({
            el: "#app1",
            data: {
                title: "Hello world"
            },
            methods: {
                onChange: function(){
                    vm1.title = 'Changed!';
                }
            }
        })

Access properties and functions with:

        vm1.title = 'Changed by Me';

        vm1.onChange();

However Vue JS will not watch or be reactive to properties created from outside the instance:

VueJS doesn't proxy or watch these properties with getters and setters.

        vm1.newProp = 'New!';

Can `console.log()` the instance:

        console.log(vm1);

### Inspecting the Vue Instance

* `$el` - refers to instance, the html representation of the instance
* `$data` - holds data properties, a way of accesing the data from outside: eg. `vm1.$data.title`
* `$ref` - put the `ref` key on an attribute (not a directive), set to any name you like. If you console `this.$refs`. You can access with `this.$this.myButton.text = "Hello world";`. If we access from outside Vue, we are changing in the DOM but not in VueJS. So VueJS will overwrite the change of DOM. **Not Reactive**

### Can create the data variable before Vue Instance and then pass it

        var data = {
            title: 'The VueJS Instance',
            showParagraph: false
        }

        var vm1 = new Vue({
            el: '#app1',
            data: data
        })

### More info on the API

[VUE API Information](https://vuejs.org/v2/api/)

### Mount

Properties prefixed by `$` are native `Vue` js methods and properties.

        vm.$mount('#app1`);

You can specify the template of the `Vue` instance and not have it derive from the `html` with:

        var vm3 = new Vue({
            template: `<h1>Hello!</h1>'
        });

        vm3.$mount('#app3');

Can also create it off screen:

        vm3.$mount();

        //then append it
        document.getElementById('app3').appendChild(vm3.$el);

### Components

Creating reusable components are greated with:

        Vue.components('hello', {
            template: '<h1>Hello!</h1>'
        });

Add the new element:

        <hello></hello>
        <hello></hello>

**Limitation of templates**: We have to specify everything as a string

### Versions

* Compiler version: respects DOM rules
* No-compiler: compiler is stripped out, compile templates during build process

### How Vuejs Updates the DOM

Each property has it's own watcher

Accessing the real DOM is the biggest performance bottleneck, so want to do as selodom as posible.

Vue Instance -> Virtual DOM -> DOM

### VueJS Instance Lifecycle

new Vue()

* beforeCreate() - Initialise Data and Events
* created() - Instance Created - Compile template or el's template
* beforeMount() - before template written to real DOM - replace `el` with compiled template
* **Mount to DOM** 
* Data changed
* beforeUpdate()
* updated()
* beforeDestroy()
* destroyed()

These are all fucntions of the Vue Instance:

        new Vue({
            el: '#app',
            data: {
                title: 'The Vue Instance'
            },
            beforeCreated: function() {
                console.log('beforeCreated()');
            },
            created: function() {
                console.log('created()');
            },
            beforeMount: function() {
                console.log('beforeCreate()');
            },
            mounted: function(){
                console.log('mounted()');
            },
            beforeUpdate: function(){
                console.log('beforeUpdate()');
            },
            updated: function(){
                console.log('updated()')
            },
            beforeDestroy: function(){
                console.log('beforeDestroy()')
            },
            destroyed: functino(){
                console.log('destroyed()')
            }
        })


## Filters

Filter helps you transform output in the data
Transforms what the user sees

Ie. Turning to uppercase letters

No built-in filters, have to create your own

Local filter:

    <p>{{ text || toUppercase }}</p>


    export default {
        filters: {
            'to-uppercase'(value) {
                return value.toUpperCase();
            }
        }
    }

Global filter:

    Vue.filter('to-lowercase');

Sometimes a computed property is the better solution - performance reasons

## Mixins

Reusable pieces of code

        import { fruitMixin } from './fruitMixin';

        export default {
            mixins: [fruitMixin],
        }

A global instance is added to every instance and eery component. Rarely should use this.

        Vue.mixin({
            created() {
                console.log('Global Mixin - Created Hook');
            }
        });

### Mixin Order

Global Mixins, local mixins then local instance code

