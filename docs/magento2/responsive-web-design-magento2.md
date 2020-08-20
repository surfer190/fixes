---
author: ''
category: Magento2
date: '2017-02-01'
summary: ''
title: Responsive Web Design Magento2
---
## Responsive Web Design in Magento 2

### Concepts

Fluid grids: Design in percentages

Flexible images: Use `max-width: 100%`

Media query: A media type that limits stylesheet scope based on screen size

Bland and Luma use Mobile First

### Breakpoints

* 320px
* 480px
* 640px
* 768px (When mobile and desktop switch)
* 1024px
* 1440px

Mobile first

* `style-m.less`: basic and mobile styles
* `style-l.less`: generate desktop specific

The large less is never loaded on a mobile device

### Magento UI

Uses `media-width()` mixin, all the rules defined in `lib/web/css/source/lib/_responsive.less`

* `lib/web/matchMedia.js` is a polyfill to allow older browsers
* `frontend/Magento/blank/web/js/responsive.js` - responsive functions for blank
* `/lib/web/mage/menu.js` changes navigation menu look and behavious based on device width
* `lib/web/mage/gallery/gallery.js` Managed product photo gallery on storefront
