from lib.imports import *
from lib.page import *
from lib.resources import *
from lib.Driver import *    
import os
import time
import logging
import re

def main():
    url = "https://www.fragrancedirect.co.uk/fragrance/mens-fragrance/shop-all.list"
    driver = initialize_and_navigate(url)
    action_chains = ActionChains(driver)
    
    actions = ActionChains(driver)
    csvv = HomePage(driver)
    csvv.make_csv('fragrancedirect.csv', 'Title,Price,updated price,weight,Product overview,Range,Brand,Volume,URL\n')

    current_page = 1
    next_button_xpath = '//*[@class="responsiveProductListPage_bottomPagination"]//button[@class="responsivePaginationNavigationButton paginationNavigationButtonNext"]'
    
    try:
        time.sleep(5)
        action_chains.send_keys(Keys.ESCAPE).perform()
        mainpagee = HomePage(driver)
        mainpagee.waiTENt(Fragrancess.Bar)
        barr = driver.find_element(By.XPATH, Fragrancess.Bar).click()
    except Exception as e:
        logging.warning(f"No bar found: {e}")

    main_folder = 'men_frag'
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
    
    while True:
        logging.info(f"Processing products on page {current_page}...")
    
        productts = driver.find_elements(By.XPATH, Fragrancess.Products)
        current_url = driver.current_url
        print(current_url)
        for product in productts:
            try:
                
                time.sleep(1)
                action_chains.key_down(Keys.CONTROL).perform()
                product.click()
                action_chains.key_up(Keys.CONTROL).perform()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)
                
                # try:
                #     time.sleep(5)
                #     action_chains.send_keys(Keys.ESCAPE).perform()
                #     mainpagee = HomePage(driver)
                #     mainpagee.waiTENt(Fragrancess.Bar)
                #     barr = driver.find_element(By.XPATH, Fragrancess.Bar).click()
                # except Exception as e:
                #     logging.warning(f"No bar found: {e}")
                    
                try:
                    varriantt = HomePage(driver)
                    varriantt.waiTENt(Fragrancess.varriaannt)
                    btns_varriant = driver.find_elements(By.XPATH, '//*[@id="mainContent"]//*[@class="athenaProductPage_productVariations productPage_productVariations_selector "]//li')
                    
                    # import pdb
                    # pdb.set_trace()
                    # for btns in btns_varriant:
                    num_btns = len(btns_varriant)
                    time.sleep(5)
                    for x in range(1 ,num_btns + 1):
                        # (locator)[x]
                        btnx = driver.find_element(By.XPATH, f'(//*[@id="mainContent"]//*[@class="athenaProductPage_productVariations productPage_productVariations_selector "]//li)[{x}]')
                        # print(btns.get_attribute('outerHTML'))
                        time.sleep(1)
                        try:
                            print("for test try")
                            btnx.click()
                    
                        except:
                            print("for test exception")
                            driver.execute_script('arguments[0].click()', btnx)
                            
                        time.sleep(10)
                        product_titlee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.varriant_title)))
                        print(product_titlee.text)
                            
                except Exception as e:
                    # print(e)
                    time.sleep(1)
                    product_titlee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.Title)))
                    print(product_titlee.text)
                    time.sleep(1)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                time.sleep(1)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:     
                current_url = driver.current_url
                print(current_url)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                logging.error(f"Error processing product on page {current_page}: {e}")
        if not navigate_to_next_page(driver, next_button_xpath):
            logging.info(f"No more pages available. Finished processing.")
            break   

        current_page += 1
        time.sleep(5)

        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()
