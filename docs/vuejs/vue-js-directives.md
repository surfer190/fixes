---
author: ''
category: Vuejs
date: '2017-06-13'
summary: ''
title: Vue Js Directives
---
# Directives

These are the `v-{ command}=` attributes

`v-html=` and `v-text=`

## Hooks

* bind (el, beinding, vnode)
* inserted(el, binding, vnode)
* update(el, binding, vnode, oldVNode)
* componentUpdate(el, binding, vnode, oldVnode)
* unbind(el, binding, vnode)

## Setup

Globally setup in `main.js`:

        Vue.directive('highlight', {
            bind(el, binding, vnode) {
                el.style.backgroundColor = 'green';
            }
        }); // v-highlight

Use binding value:

        Vue.directive('highlight', {
            bind(el, binding, vnode) {
                el.style.backgroundColor = binding.value;
            }
        });

### Local Directives

        export default {
            directives: {
                'local-highlight': {
                    bind(el, binding, vnode) {
                        ...
                    }
                }
            }
        }