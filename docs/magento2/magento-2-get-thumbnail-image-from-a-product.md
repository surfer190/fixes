---
author: ''
category: Magento2
date: '2017-01-16'
summary: ''
title: Magento 2 Get Thumbnail Image From A Product
---
## Magento 2: How to get a thumbnail image from a product

This is the simplest wat to get a product image thumbnail

Awaiting the correct way but for now this feels goods

```
$imagewidth = $imageheight = 250;
$imageUrl = $this->helper('Magento\Catalog\Helper\Image')
->init($currentproduct, 'product_page_image_large')
->setImageFile($currentproduct->getFile())
->getUrl();
```

### Source

* [Stackoverflow get a product image from product model Magento 2](http://stackoverflow.com/questions/37732103/get-product-image-from-product-model-magento-2)
