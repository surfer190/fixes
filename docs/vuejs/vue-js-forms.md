---
author: ''
category: Vuejs
date: '2017-06-13'
summary: ''
title: Vue Js Forms
---
# VueJS Forms

## Checkboxes

You can bind chekbox values to a single array field, just by binding to the same data field which is an arrray

## Radiobuttons

Vue will recognise if they are bound to the same model field and will ensure only 1 is selected at a time

## Select

Populate a select and set a default

        <option v-for="priority in priorities" :select="priority == 'Medium'">{{ priority }}</option>

## What does v-model actually do

    `v-model='x'`

Is really just a shortcut for binding the value field and input events

        :value="x"
        @input="x = $event.target.value"

## Creating our own form component

2 THings are required

Needs to accept a value prop

and need to emit an input event

More [Forms info at Vue](http://vuejs.org/guide/forms.html)

