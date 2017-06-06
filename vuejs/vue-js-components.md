# VueJS components

Important to use a prefix liek the company name so that your component is unique

In the root Vue instance `data` can be an `object`

In component `data` should be a function, so that we avoid having objects data pointing to the same place in memory.

Methods can be an object, as the functions will only run in the component context

## Component example

        <div id="app">
            <my-component></my-component>
        </div>
        <script>

        Vue.component('my-component',
        {
            data: function(){
                return {
                    status: 'Critical'
                }
            },
            template: '<p>Server Status: {{ status }}</p>'
        });

        new Vue({
        el: '#app',
        })
        </script>

## Store component as a variable

Remove selector

        var cmp = {
            data: function(){
                status: 'Critical'
            }
        }

Then register the component locally on the vue instnace:

        new Vue(({
            el: '#app',
            components: {
                'my-cmp': cmp
            }
        }))      

## Methods in components

In components you can write methods like this:

        methods: {
            changeStatus() {
                
            }
        }
    
## Importing your component

        import Home from './Home.vue'

        //Globally add component
        //Allows to add <app-server-status> element in component template
        Vue.component('app-server-status', Home);

## Template code

Wrap all your template code into one element

## Vue component Naming Convention

`CapitalCase`: `ServerStatus.vue`

## Styles

By default any item in `style` tag is set globally.

To override this add `scoped`: uses shadow DOM

`<style scoped>///</style>`

## Communicating between components

Use `props` property set from the parent

Create a `props` variable of the `components Vue Instance`:

        export default {
            props: ['name']
        }

Send it to the component with

        <app-user-detail :name="name"></app-user-detail>

If you just want to send the plain text and not the variable use:

        <app-user-detail name="name"></app-user-detail>

Can access these `props` like a normal property set up in the data `property`

### Validating Props

        props: {
            name : String
        }

        props: {
            name : {
                type: String,
                required: true
            }
        }

        props: {
            name : {
                type: String,
                default: 'Stephen'
            }
        }

If type is object then the default should be a function which returns an object

        props: {
            name : {
                type: Object,
                default: function(){
                    return {name: 'Max'}
                }
            }
        }

## Types

Objects and arrays are `reference` types and only exist in memory once

Variables only store the pointer

Therefore changing in the child component, you also change in the parent component

Sometimes you need to inform the parent component that it did indeed change:

        this.$emit('<eventName>', variable);

        this.$emit('nameWasReset', this.name);

Then you have to lsiten for the event on the component:

        <myComponent @nameWasReset="name = $event"

## Unidirection information

Can communiate from parent to child and child to parent, but not from child to child.

## Event Bus

General centralised code

In 'main.js'

        export const eventBus = new Vue();

In component

        import { eventBus} from '../main';

        eventBus.$emit('ageWasEdited', this.userAge);

Eventbus must be created before the view instance

In `created` lifecycle event:

        created(){
            eventBus.$on('ageWasEdited', (age) => {
                this.userAge = age;
            });
        }


## Slots

Slots allow us to reserve a space in a compnents template to output html content within that component

In parent:

        <appQuote>
                <h2>The Quote</h2>
                <p>A wonderful quote!</p>
        </appQuote>  

In component:

        <template>
            <div>
                <slot></slot>
            </div>
        </template>

**Remember: The styling of the child applies. Everything else works as normal on parent.**

### Named Slots

You can name slots to slectively display content:

        <appQuote>
                <h2 slot="title">{{ quoteTitle }}</h2>
                <p slot="content">A wonderful quote!</p>
        </appQuote>  

        <div class="title">
            <slot name="title"></slot>
        </div>
        <hr/>
        <div>
            <slot name="content"></slot>
        </div>

#### Unnamed Slots

Unnamed slots will become the default slot

## Dynamic Components

Selectively add components to the DOM

        <component :is="selectedComponent">
            <p>Default content</p>
        </component>

**Note: The component is destroyed and recreate when switched**

Good use case is a slideshow, let use put in content.

### Keep Alive

Preserve state, but now `destroyed()` lifecycle hook is not used.

        <keep-alive>
            <component :is="selectedComponent">
                <p>Default content</p>
            </component>
        </keep-alive>

### Lifecycle hooks

`deactivated ()`and `activated()`

### Native event modifier

        @click.native

Treat the click as if it was on the component not the underlying returned template