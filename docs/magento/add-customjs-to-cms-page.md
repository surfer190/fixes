---
author: ''
category: Magento
date: '2015-01-18'
summary: ''
title: Add Customjs To Cms Page Magento 1
---
# Add custom JS to CMS page

## Step 1: In magento backend go to: Pages -> Page -> Design Tab -> Layout Update XML

## Step 2: Insert the following

    <reference name="head">
      <action method="addItem">
        <type>skin_js</type><script>folder/js/include-my-js.js</script>
      </action>
    </reference>
