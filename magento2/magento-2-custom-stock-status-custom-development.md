# How to change the stock status on Magento 2 based on custom options

## The Task

The task is to change the stock status on the product view page based on a seperate backend attribute.

### Magento 1 code

In the file: `app/designfrontend/default/{theme}/template/catalog/product/view/type/default.phtml`

The code for doing this in magento 1 is:

```
<?php

 	$_product = $this->getProduct();
	$qty = $_product->getStockItem()->getQty();
	$qty_txt = round($qty);
	$normally_instock = $_product->getData('normally_instock');

?>
<?php /* @var $this Mage_Catalog_Block_Product_View_Abstract */?>

    available + qty > 0:
        in stock
    available + qty < 1 + normally in stock
        warehouse
    available + qty < 1
        backordered
    not available
        temporarily not available

<?php echo $this->getChildHtml('product_type_data_extra') ?>
<?php echo $this->getPriceHtml($_product) ?>
```

## The solution

First thing to do is check where in the template is the stock indicator by showing template hints.

THe template is `/vendor/magento/module-catalog/view/frontend/templates/product/view/type/default.phtml`

and the block class is: `Magento\Catalog\Block\Product\View\Type\Simple\Interceptor` for simple products

But there is a **snare**, the template for bundle products is `/var/www/shootingstuff/project/vendor/magento/module-bundle/view/frontend/templates/catalog/product/view/type/bundle.phtml` and the block is `Magento\Bundle\Block\Catalog\Product\View\Type\Bundle\Interceptor`

## The incorrect way: Overriding core template files

So we found the string `In Stock` in `app/code/Magento/Catalog/view/frontend/templates/product/view/type/default.phtml`. So changing stuff in this file only changes `simple` products.

For `Downloadable` you have to check: `Magento/Downloadable/view/frontend/templates/catalog/product/type.phtml`

For Grouped products: `Magento/GrouperProduct/view/frontend/templates/product/view/type/default.phtml`

For Bundled products:
`Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle.phtml`

and the `summary.html` file.

So it is in alot of places...

Flippit.

### The JS option

This is probably the best way to do it.

### Correct way is using dependency injection

http://magento.stackexchange.com/questions/97943/how-to-get-stock-quantity-of-each-product-in-magento-2
