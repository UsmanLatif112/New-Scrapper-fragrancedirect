from lib.imports import *
from lib.page import *
from lib.resources import *
from lib.Driver import *    
from lib.data import *
import os
import time
import logging
import re, pyperclip
from selenium.webdriver.common.action_chains import ActionChains

def main():
    
    try:
        url = "https://accounts.shopify.com/login?rid=4a7fd5f0-c0d5-4315-8545-64e9ae490816"
        driver = initialize_and_navigate(url)
        csvv = HomePage(driver)
        action_chains = ActionChains(driver)
        csvv.make_csv('uploaded product.csv', 'Titles\n')
        csvv.make_csv('error_product.csv', 'Titles\n')
        
        mainpage = HomePage(driver)
        mainpage.wait(Uploaderdata.Main_login_page)

        time.sleep(1)
        email_fieldd = HomePage(driver)
        email_fieldd.click_btn(Uploaderdata.email_field)
        time.sleep(1)
        
        time.sleep(1)
        Usernamee = HomePage(driver)
        Usernamee.enter_name_delay(Uploaderdata.email_field, username)
        
        time.sleep(1)
        email_fieldd = HomePage(driver)
        email_fieldd.click_btn(Uploaderdata.continue_email)
        time.sleep(1)
        
        password_pagee = HomePage(driver)
        password_pagee.wait(Uploaderdata.password_page)
        
        time.sleep(1)
        password_feildd = HomePage(driver)
        password_feildd.click_btn(Uploaderdata.password_feild)
        time.sleep(1)

        password_feilddd = HomePage(driver)
        password_feilddd.enter_name_delay(Uploaderdata.password_feild, Password)
        
        time.sleep(1)
        password_feildd = HomePage(driver)
        password_feildd.click_btn(Uploaderdata.login_btn)
        
        time.sleep(1)
        view_allstore_pagee = HomePage(driver)
        view_allstore_pagee.wait(Uploaderdata.view_allstore_page)
        
        time.sleep(1)
        view_allstoreee = HomePage(driver)
        view_allstoreee.click_btn(Uploaderdata.view_allstore)
        
        driver.switch_to.window(driver.window_handles[-1])
        
        time.sleep(1)
        select_account_pageee = HomePage(driver)
        select_account_pageee.waitsix(Uploaderdata.select_account_page)
        
        time.sleep(1)
        select_account_btn = HomePage(driver)
        select_account_btn.click_btn(Uploaderdata.select_account_page)
        
        try:
            time.sleep(1)
            con_browserr = HomePage(driver)
            con_browserr.waitsix(Uploaderdata.con_browser)
            
            if con_browserr:
                time.sleep(1)
                con_browserrr = HomePage(driver)
                con_browserrr.click_btn(Uploaderdata.con_browser)
            
            else:
                print("No browser execption found")
        except:
            print("No browser execption found")
            

        time.sleep(1)
        main_page_storee = HomePage(driver)
        main_page_storee.wait(Uploaderdata.main_page_store)
        

        csv_file_path = 'E:\\New Scrapper fragrancedirect\\Simpleproduct.csv'
        
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    
                    title = row[0]                      
                    Desscription = row[1]
                    Category = row[2]
                    Coollection = row[3].split(',')
                    Taggs = row[4]
                    # Taggs = row[4].split(',')
                    pro_typpe = row[5]
                    vendor = row[6]
                    Prrice = row[7]
                    weeight = row[8]
                    skunumber = row[9]
                    img_srcs = row[10:]


                    try:
                        time.sleep(1)
                        add_product_btnn = HomePage(driver)
                        add_product_btnn.click_btn(Uploaderdata.add_product_btn)
                        
                        time.sleep(1)
                        add_product_pagee = HomePage(driver)
                        add_product_pagee.waitsix(Uploaderdata.add_product_page)
                    except:
                        pass
                    
                    time.sleep(1)
                    Title_filedd = HomePage(driver)
                    Title_filedd.click_btn(Uploaderdata.Title_filed)
                    time.sleep(1)
                    Title_fileddd = HomePage(driver)
                    Title_fileddd.enter_name(Uploaderdata.Title_filed, title)
                    
                    pyperclip.copy(Desscription)
                    
                    time.sleep(1)
                    product_descc = HomePage(driver)
                    product_descc.click_btn(Uploaderdata.product_desc)
                    
                    time.sleep(1)
                    
                    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                    
                    time.sleep(1)
                    cateogoryy = HomePage(driver)
                    cateogoryy.click_btn(Uploaderdata.cateogory)
            
                    time.sleep(1)
                    cateogoryyy = HomePage(driver)
                    cateogoryyy.enter_name(Uploaderdata.cateogory, Category)
                    time.sleep(1)
                    action_chains.send_keys(Keys.ENTER).perform()
                    
                    time.sleep(1)
                    pro_typee = HomePage(driver)
                    pro_typee.click_btn(Uploaderdata.pro_type)
            
                    time.sleep(1)
                    pro_typeee = HomePage(driver)
                    pro_typeee.enter_name(Uploaderdata.pro_type, pro_typpe)
                    
                    time.sleep(1)
                    vendorr = HomePage(driver)
                    vendorr.click_btn(Uploaderdata.vendor)
            
                    time.sleep(1)
                    vendorrr = HomePage(driver)
                    vendorrr.enter_name(Uploaderdata.vendor, vendor)
                    
                    time.sleep(1)
                    action_chains.send_keys(Keys.ENTER).perform()
                    try:
                        for col in Coollection:
                            time.sleep(1)
                            Collectionn = HomePage(driver)
                            Collectionn.click_btn(Uploaderdata.Collection)
                    
                            time.sleep(1)
                            Collectionnn = HomePage(driver)
                            Collectionnn.enter_name(Uploaderdata.Collection, col)
                        
                            time.sleep(3)
                            action_chains.send_keys(Keys.ENTER).perform()
                            time.sleep(1)
                            time.sleep(1)
                            Collectionn = HomePage(driver)
                            Collectionn.click_btn(Uploaderdata.Collection)
                            time.sleep(1)
                            action_chains.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
                            time.sleep(1)
                            
                    except:
                        pass
                    
                    try:
                        time.sleep(1)
                        Tagss = HomePage(driver)
                        Tagss.click_btn(Uploaderdata.Tags)
                        time.sleep(1)
                        Tagsss = HomePage(driver)
                        Tagsss.enter_name(Uploaderdata.Tags, Taggs)
                        time.sleep(3)
                        action_chains.send_keys(Keys.ENTER).perform()
                        time.sleep(1)
                    except:
                        pass
                            
                        
                    time.sleep(1)
                    pricee = HomePage(driver)
                    pricee.click_btn(Uploaderdata.price)
            
                    time.sleep(1)
                    priceee = HomePage(driver)
                    priceee.enter_name(Uploaderdata.price, Prrice)
                    
                    try: 
                        price = float(Prrice)                    
                        time.sleep(1)
                        
                        Tagss = HomePage(driver)
                        Tagss.click_btn(Uploaderdata.Tags)
                        
                        time.sleep(1)
                        
                        if price < 10:
                            time.sleep(1)
                            Tagsss = HomePage(driver)
                            Tagsss.enter_name(Uploaderdata.Tags, "Less than £10")
                            time.sleep(1)
                            action_chains.send_keys(Keys.ENTER).perform()
                        elif 10 <= price < 25:
                            time.sleep(1)
                            Tagsss = HomePage(driver)
                            Tagsss.enter_name(Uploaderdata.Tags, "£10 - £25")
                            time.sleep(1)
                            action_chains.send_keys(Keys.ENTER).perform()
                        elif 25 <= price < 50:
                            time.sleep(1)
                            Tagsss = HomePage(driver)
                            Tagsss.enter_name(Uploaderdata.Tags, "£25 - £50")
                            time.sleep(1)
                            action_chains.send_keys(Keys.ENTER).perform()
                        elif 50 <= price < 100:
                            time.sleep(1)
                            Tagsss = HomePage(driver)
                            Tagsss.enter_name(Uploaderdata.Tags, "£50 - £100")
                            time.sleep(1)
                            action_chains.send_keys(Keys.ENTER).perform()
                        elif 100 <= price :
                            time.sleep(1)
                            Tagsss = HomePage(driver)
                            Tagsss.enter_name(Uploaderdata.Tags, "More than £100")
                            time.sleep(1)
                            action_chains.send_keys(Keys.ENTER).perform()
                        else:
                            print("Price is out of range")
                    except Exception as e:
                        print(e)
                    
                    try:
                        try:
                            
                            SKU_find = HomePage(driver)
                            SKU_find.waitinput(Uploaderdata.SKU_CLICK_INPUT)
                            time.sleep(1)
                            SKU_CLICK_INPUTc = driver.find_element(By.XPATH, Uploaderdata.SKU_CLICK_INPUT)
                            action_chains.move_to_element(SKU_CLICK_INPUTc).perform()
                            if SKU_find:
                                try:
                                    time.sleep(1)
                                    SKU_CLICK_INPUTt = HomePage(driver)
                                    SKU_CLICK_INPUTt.click_btn(Uploaderdata.SKU_CLICK_INPUT)
                                except:
                                    pass
                                try:
                                    time.sleep(1)
                                    SKU_CLICK_INPUTtt = HomePage(driver)
                                    SKU_CLICK_INPUTtt.enter_name(Uploaderdata.SKU_CLICK_INPUT, skunumber)
                                except:
                                    pass
                        except:
                            try:
                                time.sleep(1)
                                SKU_CLICK_BTNn = HomePage(driver)
                                SKU_CLICK_BTNn.click_btn(Uploaderdata.SKU_CLICK_BTN)
                            except:
                                pass
                            
                            try:
                                time.sleep(1)
                                SKU_CLICK_INPUTt = HomePage(driver)
                                SKU_CLICK_INPUTt.click_btn(Uploaderdata.SKU_CLICK_INPUT)
                            except:
                                pass
                            try:
                                time.sleep(1)
                                SKU_CLICK_INPUTtt = HomePage(driver)
                                SKU_CLICK_INPUTtt.enter_name(Uploaderdata.SKU_CLICK_INPUT, skunumber)
                            except:
                                pass
                            
                            time.sleep(8)
                    except Exception as e:
                        print(e)
                        
                    time.sleep(1)
                    Quantityy = HomePage(driver)
                    Quantityy.click_btn(Uploaderdata.Quantity)
            
                    time.sleep(1)
                    Quantityyy = HomePage(driver)
                    Quantityyy.enter_name(Uploaderdata.Quantity, "10")
                    
                    time.sleep(1)
                    Weigthh = HomePage(driver)
                    Weigthh.click_btn(Uploaderdata.Weigth)
            
                    time.sleep(1)
                    Weigthhh = HomePage(driver)
                    Weigthhh.enter_name(Uploaderdata.Weigth, weeight)
                    
                    time.sleep(1)
                    Weigth_btnn = HomePage(driver)
                    Weigth_btnn.click_btn(Uploaderdata.Weigth_btn)
        
                    time.sleep(1)
                    variant_btnn = HomePage(driver)
                    variant_btnn.click_btn(Uploaderdata.variant_btn)
                    
                    time.sleep(1)
                    Variant_sizee = HomePage(driver)
                    Variant_sizee.click_btn(Uploaderdata.Variant_size)
            
                    time.sleep(1)
                    Variant_sizeee = HomePage(driver)
                    Variant_sizeee.enter_name(Uploaderdata.Variant_size, "Size")
                    
                    time.sleep(1)
                    action_chains.send_keys(Keys.ENTER).perform()

                    time.sleep(1)
                    Variant_optionn = HomePage(driver)
                    Variant_optionn.click_btn(Uploaderdata.Variant_option)
                    
                    numeric_part = weeight.split("ml")[0]
                    
                    time.sleep(1)
                    Variant_optionnn = HomePage(driver)
                    Variant_optionnn.enter_name(Uploaderdata.Variant_option, f"{numeric_part} ML")
                    
                    time.sleep(1)
                    Variant_savee = HomePage(driver)
                    Variant_savee.click_btn(Uploaderdata.Variant_save)
                    
                    upload_media_bttn = driver.find_element(By.XPATH, Uploaderdata.upload_media_btn)
                    action_chains.move_to_element(upload_media_bttn).perform()
                    time.sleep(1)
                    for srcc in img_srcs:
                        try:
                            time.sleep(1)
                            upload_media_btnn = HomePage(driver)
                            upload_media_btnn.click_btn(Uploaderdata.upload_media_btn)
                            image_url_modall = HomePage(driver)
                            image_url_modall.waitinput(Uploaderdata.image_url_modal)
                            time.sleep(1)
                            image_url_modal_feildd = HomePage(driver)
                            image_url_modal_feildd.click_btn(Uploaderdata.image_url_modal_feild)
                            time.sleep(1)
                            image_url_modal_feilldd = HomePage(driver)
                            image_url_modal_feilldd.enter_name(Uploaderdata.image_url_modal_feild, f"{srcc}")
                            time.sleep(1)
                            image_url_modal_btnn = HomePage(driver)
                            image_url_modal_btnn.click_btn(Uploaderdata.image_url_modal_btn)
                            time.sleep(8)
                        except:
                            time.sleep(1)
                            action_chains.send_keys(Keys.ESCAPE).perform()
                            time.sleep(1)
                        
                    save_bttn = driver.find_element(By.XPATH, Uploaderdata.save_btn)
                    action_chains.move_to_element(save_bttn).perform()
                    time.sleep(1)
                    save_btnn = HomePage(driver)
                    save_btnn.click_btn(Uploaderdata.save_btn)
                    
                    try:
                        time.sleep(1)
                        active_btn_modall = HomePage(driver)
                        active_btn_modall.waaiite(Uploaderdata.active_btn_modal)
                        
                        time.sleep(1)
                        active_btnn = HomePage(driver)
                        active_btnn.click_btn(Uploaderdata.active_btn)
                    
                    except:
                        print("no modal found")
                    time.sleep(1)
                    
                    driver.get("https://admin.shopify.com/store/brandlistry/products?selectedView=all")
                    
                    try:
                        time.sleep(1)
                        con_browserr = HomePage(driver)
                        con_browserr.wait(Uploaderdata.con_browser)
                        
                        if con_browserr:
                            time.sleep(1)
                            con_browserrr = HomePage(driver)
                            con_browserrr.click_btn(Uploaderdata.con_browser)
                        
                        else:
                            print("No browser execption found")
                            pass
                    except:
                        print("No browser execption found")
                        pass
                        
                    time.sleep(1)
                    main_page_storee = HomePage(driver)
                    main_page_storee.wait(Uploaderdata.main_page_store)
                    csvv.make_csv('uploaded product.csv', f'''"{title}"\n''', new=False)
                except:
                    
                    print(f"error uploading {title}")
                    time.sleep(1)
                    driver.get("https://admin.shopify.com/store/brandlistry/products?selectedView=all")
                    csvv.make_csv('error_product.csv', f'''"{title}"\n''', new=False)
                    time.sleep(1) 
                    try:
                        time.sleep(1)
                        con_browserr = HomePage(driver)
                        con_browserr.wait(Uploaderdata.con_browser)
                        
                        if con_browserr:
                            time.sleep(1)
                            con_browserrr = HomePage(driver)
                            con_browserrr.click_btn(Uploaderdata.con_browser)
                        
                        else:
                            print("No browser execption found")
                            pass
                    except:
                        print("No browser execption found")
                        pass
                    continue    
                    
                
                    
    except Exception as e:
        print(e) 
                
    time.sleep(8)
    driver.quit()

if __name__ == "__main__":
    main()
