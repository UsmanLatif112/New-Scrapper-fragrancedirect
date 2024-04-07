class Fragrancess:
    Fragrance = "//*[@class='westendHeader_navigation']//ul//li[@data-js-element='hasSubnav']/a[@data-context='Fragrance']"
    Shop_all = "//*[@data-component='brandLogos']/a[@href='https://www.fragrancedirect.co.uk/fragrance/shop-all.list']"
    Products = '//div[@class="productBlock_itemDetails_wrapper "]/a[@class="productBlock_link"]'
    Bar = '//*[@id="onetrust-button-group"]/*[@id="onetrust-accept-btn-handler"]'
    Title = '//*[@class="athenaProductPage_lastColumn"]//h1'
    RRP = '//*[@class="athenaProductPage_productPrice"]//p[@class="productPrice_price  "]'
    DESCRIPTION = '//*[@class="athenaProductDescription_contentPropertyList"]'
    PRODUCTover = '//*[@class="athenaProductPage_productDescriptionFull"]//*[@class="productDescription_contentPropertyListItem productDescription_contentPropertyListItem_synopsis productDescription_contentPropertyListItem-active"][contains(normalize-space(), "Product Overview")]//p'
    product_detailll = '//*[@class="productDescription_contentPropertyListItem  productDescription_contentPropertyListItem_productDetails  "]//button[@id="product-description-heading-lg-9"]'
    product_detaiL = '//*[@id="product-description-content-lg-9"]/div'
    RANGE = '//*[@class="athenaProductPage_productDescriptionFull"]//div[@id="product-description-content-lg-9"]/div/ul[@data-information-component="range"]/li'
    BRAND = '//*[@class="athenaProductPage_productDescriptionFull"]//div[@id="product-description-content-lg-9"]/div/ul[@data-information-component="brand"]/li'
    VOLUME = '//*[@class="athenaProductPage_productDescriptionFull"]//div[@id="product-description-content-lg-9"]/div/ul[@data-information-component="volume"]/li'
