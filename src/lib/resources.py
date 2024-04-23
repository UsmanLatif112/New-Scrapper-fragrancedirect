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
    # varriant_btn = '//*[@id="mainContent"]//*[@class="athenaProductVariations_list"]/li'
    # varriant_btn = '//*[@id="mainContent"]//*[@class="athenaProductVariations"]//div[@aria-label="Size"]//ul[@class="athenaProductVariations_list"]/li'
    varriant_btn = '//*[@id="mainContent"]//*[@class="athenaProductPage_productVariations productPage_productVariations_selector "]//li'
    varriaannt = '//*[@id="mainContent"]//*[@class="athenaProductVariations_list"]'
    varriant_title = '//*[@id="mainContent"]//*[@class="productName_title"]'
    
    
    
    
    
class Uploaderdata:
    Main_login_page = '//*[@class="login-card "]'
    email_field = '//*[@id="account_email"]'
    continue_email = '//*[@name="commit"][contains(normalize-space(), "Continue with email")]'
    # password_page = '//*[@class="login-card "][contains(normalize-space(), "login")]'
    password_page = '//*[@class="login-card "]//*[@class="login-card__content"]//*[@class="password-wrapper polaris-uplift-input-wrapper"]'
    password_feild = '//*[@id="account_password"]'
    login_btn = '//*[@name="commit"][contains(normalize-space(), "Log in")]'
    view_allstore_page = '//*[@class="ui-layout__item"]//*[@class="ui-card__section"][contains(normalize-space(), "View all stores")]'
    view_allstore = '//*[@class="ui-card__section"]//a[contains(normalize-space(), "View all stores")]'
    select_account_page = '//*[@class="login-card "]//*[@class="main-card-section"]//a[contains(normalize-space(), "Muzzamil Ali")]'
    main_page_store = '//*[@class="Polaris-Frame__Content"]//*[@class="Polaris-Box"][contains(normalize-space(), "Products")]'
    add_product_btn = '//*[@class="Polaris-Page-Header__RightAlign"]//a/span[contains(normalize-space(), "Add product")]'
    add_product_page = '//*[@id="AppFrameMain"]//*[@class="Polaris-Box"][contains(normalize-space(), "Add product")]'
    con_browser = '//*[@class="_UnsupportedBrowser_my03m_1"]//button[contains(normalize-space(), "Continue with unsupported browser")]'
    
    
    
    Title_filed = '//*[@class="Polaris-Connected"]//input[@name="title"]'
    # product_desc = '//*[@data-id="product-description"]'
    product_desc = '//*[@id="product-description_ifr"]'
    cateogory = '//*[@class="Polaris-LegacyCard"]//input[@id="ProductCategoryPickerId"]'
    pro_type = '//*[@class="Polaris-LegacyCard"]//input[@id="ProductOrganizationCustomType"]'
    vendor = '//*[@class="Polaris-LegacyCard"]//input[@id="VendorAutocompleteField1"]'
    Collection = '//*[@class="Polaris-LegacyCard"]//input[@id="CollectionsAutocompleteField1"]'
    Tags = '//*[@class="Polaris-LegacyCard"]//input[@name="tags"]'
    price = '//*[@class="Polaris-LegacyCard"]//input[@name="price"]'
    Quantity = '//*[@class="Polaris-Layout"]//input[@name="inventoryLevels[0]"]'
    Weigth = '//*[@class="Polaris-Box"]//input[@id="ShippingCardWeight"]'
    Weigth_btn = '//*[@id="ShippingCardWeightUnit"]/option[@value="GRAMS"][contains(normalize-space(), "g")]'
    variant_btn = '//*[@class="Polaris-Box"]//button[contains(normalize-space(), "Add options like size or color")]'
    Variant_size = '//*[@class="Polaris-Layout"]//input[@name="optionName[0]"]'
    Variant_option = '//*[@class="Polaris-Layout"]//input[@name="optionValue[0][0]"]'
    Variant_save = '//*[@class="Polaris-Layout"]//button[@type="button"][contains(normalize-space(), "Done")]'
    upload_media_btn = '//*[@class="Polaris-LegacyCard"]//button[contains(normalize-space(), "Upload new")]'
    after_upload_media = '//*[@class="Polaris-LegacyCard"]//div[@class="_Grid_1o4jr_4"]'
    save_btn = '//*[@id="AppFrame"]//*[@class="Polaris-PageActions"]//button[contains(normalize-space(), "Save")]'
    active_btn_modal = '//*[@id="PolarisPortalsContainer"]//div[@class="Polaris-Box"][contains(normalize-space(), "This product is set to Active")]'
    active_btn = '//*[@id="PolarisPortalsContainer"]//button[contains(normalize-space(), "Save as active")]'
    SKU_CLICK_BTN = '//*[@class="Polaris-Frame__Content"]//div[@class="Polaris-FormLayout__Item Polaris-FormLayout--grouped"][contains(normalize-space(), "This product has a SKU or barcode")]//input[@class="Polaris-Checkbox__Input"]'
    SKU_CLICK_INPUT = '//*[@class="Polaris-Frame__Content"]//div[@class="Polaris-BlockStack"][contains(normalize-space(), "SKU (Stock Keeping Unit)")]//input[@name="sku"]'
    
    
    