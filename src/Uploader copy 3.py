from lib.imports import *
from lib.page import *
from lib.resources import *
from lib.Driver import *    
from lib.data import *
import os
import time
import logging
import re

def main():
    
    try:
        url = "https://accounts.shopify.com/login?rid=4a7fd5f0-c0d5-4315-8545-64e9ae490816"
        driver = initialize_and_navigate(url)
        csvv = HomePage(driver)
        action_chains = ActionChains(driver)
        
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
        select_account_pageee.wait(Uploaderdata.select_account_page)
        
        time.sleep(1)
        select_account_btn = HomePage(driver)
        select_account_btn.click_btn(Uploaderdata.select_account_page)
        
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
        except:
            print("No browser execption found")
            

        time.sleep(1)
        main_page_storee = HomePage(driver)
        main_page_storee.wait(Uploaderdata.main_page_store)
        

        csv_file_path = 'E:\\New Scrapper fragrancedirect\\Simpleproduct.csv'  # Replace with the actual path to your CSV file
        titles_list = []
        # Open the CSV file
        
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            
            # Skip the header row
            next(reader)
            
            # Iterate over the rows and retrieve values from the specific column
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
                    target_directory = row[10]


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
                    title2 = re.sub(r'\s\d+ml', '', title)
                    time.sleep(1)
                    if title2 in titles_list:
                        time.sleep(1)
                        print(title2)
                        time.sleep(1)
                        csvv.make_csv('dupli.csv', 'Titles\n')
                        time.sleep(1)
                        csvv.make_csv('dupli.csv', f'''"{title2}",,"{title}"\n''', new=False)
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
                        except Exception as e:
                            print("No browser execption found")
                            print(e)
                            pass
                        continue
                    
                    else:        
            
                        time.sleep(1)
                        Title_fileddd = HomePage(driver)
                        Title_fileddd.enter_name(Uploaderdata.Title_filed, title)
                        
                        
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')

                        time.sleep(1)
                        
                        char_limit = 180  # Adjust this value as needed

                        # Split the description into words
                        words = Desscription.split()

                        # Initialize variables
                        paragraphs = []
                        current_paragraph = ''
                        for word in words:
                            if len(current_paragraph) + len(word) + 1 <= char_limit:  # +1 for the space
                                current_paragraph += word + ' '
                            else:
                                # Find the last full stop before the character limit
                                last_full_stop = current_paragraph.rfind('.')
                                
                                if last_full_stop != -1:
                                    paragraphs.append(current_paragraph[:last_full_stop + 1].strip())
                                    current_paragraph = current_paragraph[last_full_stop + 1:].strip() + ' '
                                else:
                                    paragraphs.append(current_paragraph.strip())
                                    current_paragraph = word + ' '

                        # Add the last paragraph
                        if current_paragraph:
                            paragraphs.append(current_paragraph.strip())
                        
                        for paragraph in paragraphs:
                            pyautogui.typewrite(paragraph)
                            time.sleep(1)
                            pyautogui.typewrite('\n')  # Add a new line after each paragraph
                            time.sleep(1)
                            
                        
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
                            
                                time.sleep(1)
                                action_chains.send_keys(Keys.ENTER).perform()
                                time.sleep(1)
                                pyautogui.hotkey("ctrl", "a")
                                time.sleep(1)
                                pyautogui.press('backspace')
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
                            time.sleep(5)
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
                            
                            # Tagsss = HomePage(driver)
                            # Tagsss.enter_name(Uploaderdata.Tags, "£10 - £25")
                            # time.sleep(10)
                            # action_chains.send_keys(Keys.ENTER).perform()
                            
                            # time.sleep(1)
                            # pyautogui.hotkey("ctrl", "a")
                            # time.sleep(1)
                            # pyautogui.press('backspace')
                            # time.sleep(1)
                            
                            if price < 10:
                                time.sleep(2)
                                Tagsss = HomePage(driver)
                                Tagsss.enter_name(Uploaderdata.Tags, "Less than £10")
                                time.sleep(2)
                                action_chains.send_keys(Keys.ENTER).perform()
                            elif 10 <= price < 25:
                                time.sleep(2)
                                Tagsss = HomePage(driver)
                                Tagsss.enter_name(Uploaderdata.Tags, "£10 - £25")
                                time.sleep(2)
                                action_chains.send_keys(Keys.ENTER).perform()
                            elif 25 <= price < 50:
                                time.sleep(2)
                                Tagsss = HomePage(driver)
                                Tagsss.enter_name(Uploaderdata.Tags, "£25 - £50")
                                time.sleep(2)
                                action_chains.send_keys(Keys.ENTER).perform()
                            elif 50 <= price < 100:
                                time.sleep(2)
                                Tagsss = HomePage(driver)
                                Tagsss.enter_name(Uploaderdata.Tags, "£50 - £100")
                                time.sleep(2)
                                action_chains.send_keys(Keys.ENTER).perform()
                            elif 100 <= price :
                                time.sleep(2)
                                Tagsss = HomePage(driver)
                                Tagsss.enter_name(Uploaderdata.Tags, "More than £100")
                                time.sleep(2)
                                action_chains.send_keys(Keys.ENTER).perform()
                            else:
                                print("Price is out of range")
                        except Exception as e:
                            print(e)
                        
                        time.sleep(2)
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
                        upload_media_btnn = HomePage(driver)
                        upload_media_btnn.click_btn(Uploaderdata.upload_media_btn)
                        
                        time.sleep(5)
                        
                        target_directory_path = f'{target_directory}'
                        # target_directory_path = f"E:\New Scrapper fragrancedirect\New folder\men_frag\Nautica Voyage Eau de Toilette Spray 100ml"

                        # Click the address bar
                        pyautogui.hotkey('alt', 'd')
                        time.sleep(0.5)
                        pyautogui.typewrite(target_directory_path)
                        time.sleep(0.5)
                        pyautogui.press('enter')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        time.sleep(0.5)
                        pyautogui.press('tab')
                        # Wait for a while to ensure all images are loaded
                        time.sleep(1)  # Adjust the sleep time as needed

                        # Select all files in the directory
                        pyautogui.hotkey('ctrl', 'a')
                        
                        time.sleep(1)
                        
                        # Press Enter to upload
                        pyautogui.press('enter')
                        
                        time.sleep(1)
                        after_upload_mediaa = HomePage(driver)
                        after_upload_mediaa.waitsix(Uploaderdata.after_upload_media)
                        
                        time.sleep(20)
                        
                        try:
                            # import pdb;
                            # pdb.set_trace()
                            try:
                                SKU_find = HomePage(driver)
                                SKU_find.waitinput(Uploaderdata.SKU_CLICK_INPUT)
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
                        except Exception as e:
                            print(e)
                            
                        time.sleep(10)
                        
                        save_bttn = driver.find_element(By.XPATH, Uploaderdata.save_btn)
                        action_chains.move_to_element(save_bttn).perform()
                        
                        time.sleep(0.5)
                        save_btnn = HomePage(driver)
                        save_btnn.click_btn(Uploaderdata.save_btn)
                        
                        try:
                            time.sleep(0.5)
                            active_btn_modall = HomePage(driver)
                            active_btn_modall.waaiite(Uploaderdata.active_btn_modal)
                            
                            time.sleep(0.5)
                            active_btnn = HomePage(driver)
                            active_btnn.click_btn(Uploaderdata.active_btn)
                        
                        except:
                            print("no modal found")
                        time.sleep(2)
                        
                        driver.get("https://admin.shopify.com/store/brandlistry/products?selectedView=all")
                        
                        try:
                            time.sleep(0.5)
                            con_browserr = HomePage(driver)
                            con_browserr.wait(Uploaderdata.con_browser)
                            
                            if con_browserr:
                                time.sleep(0.5)
                                con_browserrr = HomePage(driver)
                                con_browserrr.click_btn(Uploaderdata.con_browser)
                            
                            else:
                                print("No browser execption found")
                                pass
                        except:
                            print("No browser execption found")
                            pass
                            
                        time.sleep(0.5)
                        main_page_storee = HomePage(driver)
                        main_page_storee.wait(Uploaderdata.main_page_store)
                        csvv.make_csv('uploaded product.csv', 'Titles\n')
                        csvv.make_csv('uploaded product.csv', f'''"{title}"\n''', new=False)
                        titles_list.append(title1)
                except:
                    
                    print(f"error uploading {title}")
                    csvv.make_csv('error_product.csv', 'Titles\n')
                    time.sleep(1)
                    csvv.make_csv('error_product.csv', f'''"{title}"\n''', new=False)
                    time.sleep(0.5)
                    driver.get("https://admin.shopify.com/store/brandlistry/products?selectedView=all")
                        
                    try:
                        time.sleep(0.5)
                        con_browserr = HomePage(driver)
                        con_browserr.wait(Uploaderdata.con_browser)
                        
                        if con_browserr:
                            time.sleep(0.5)
                            con_browserrr = HomePage(driver)
                            con_browserrr.click_btn(Uploaderdata.con_browser)
                        
                        else:
                            print("No browser execption found")
                            pass
                    except:
                        print("No browser execption found")
                        pass
                    pass
                    
    except Exception as e:
        print(e)          
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
