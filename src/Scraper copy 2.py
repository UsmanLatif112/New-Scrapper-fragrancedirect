from lib.imports import *
from lib.page import *
from lib.resources import *
from lib.Driver import *    
import os
import time
import logging
import re

# from src.lib.Driver import initialize_and_navigate

def main():
    url = "https://www.fragrancedirect.co.uk/"
    driver = initialize_and_navigate(url)
    action_chains = ActionChains(driver)
    csvv = HomePage(driver)
    csvv.make_csv('fragrancedirect.csv', 'Title,Price,updated price,weight,Product overview,Range,Brand,Volume,URL\n')

    mainpage = HomePage(driver)
    mainpage.wait(Fragrancess.Fragrance)
    time.sleep(1)
    action_chains.send_keys(Keys.ESCAPE).perform()

    time.sleep(1)
    Fragrancee = HomePage(driver)
    Fragrancee.click_btn(Fragrancess.Fragrance)
    time.sleep(2)
    
    current_page = 1
    next_button_xpath = '//*[@class="responsiveProductListPage_bottomPagination"]//button[@class="responsivePaginationNavigationButton paginationNavigationButtonNext"]'

    while True:
        logging.info(f"Processing products on page {current_page}...")

        try:
            Shop_alll = driver.find_element(By.XPATH, Fragrancess.Shop_all)
            action_chains.move_to_element(Shop_alll).perform()
            time.sleep(2)
            Shop_alll = HomePage(driver)
            Shop_alll.click_btn(Fragrancess.Shop_all)
        except Exception as e:
            logging.error(f"Error clicking Shop_all button: {e}")

        time.sleep(2)

        try:
            mainpagee = HomePage(driver)
            mainpagee.wait(Fragrancess.Bar)
            barr = driver.find_element(By.XPATH, Fragrancess.Bar).click()
        except Exception as e:
            logging.warning(f"No bar found: {e}")

        main_folder = 'men_frag'
        if not os.path.exists(main_folder):
            os.makedirs(main_folder)

        productts = driver.find_elements(By.XPATH, Fragrancess.Products)

        for product in productts:
            try:
                time.sleep(1)
                action_chains.key_down(Keys.CONTROL).perform()
                product.click()
                action_chains.key_up(Keys.CONTROL).perform()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)

                product_titlee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.Title)))
                print(product_titlee.text)
                product_folder = os.path.join(main_folder, product_titlee.text.strip())
                if not os.path.exists(product_folder):
                    os.makedirs(product_folder)

                image_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="athenaProductImageCarousel_thumbnailScrollContainer "]//ul/li//img')))
                for img in image_elements:
                    img_url = img.get_attribute('src')
                    if img_url.startswith('http'):
                        new_img_url = img_url.replace('/130/130/', '/512/512/')
                        download_image_with_resolution(new_img_url, 512, product_folder, product_titlee)
                    else:
                        logging.warning(f"Invalid image URL: {img_url}")

                time.sleep(0.5)
                product_rrp_text = ''
                product_over_text = ''
                product_range = ''
                product_brand = ''
                product_volume = ''
                # updated_title = ''

                try:
                    product_rrp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.RRP)))
                    product_rrp_text = product_rrp.text.replace('RRP:', '').replace('$', '').strip()
                except:
                    logging.warning("RRP not found")

                try:
                    product_over = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.PRODUCTover)))
                    product_over_text = product_over.text.replace('"', '""').strip()
                except:
                    logging.warning("Product overview not found")

                time.sleep(0.5)
                product_deta = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.product_detailll)))
                action_chains.move_to_element(product_deta).perform()
                time.sleep(0.5)
                product_detaill = HomePage(driver)
                product_detaill.click_btn(Fragrancess.product_detailll)
                time.sleep(0.5)

                try:
                    # product_range_element = driver.find_element(By.XPATH, Fragrancess.RANGE)
                    product_range_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.RANGE)))
                    product_range = product_range_element.text.replace('"', '""').strip() if product_range_element else ''
                except:
                    logging.warning("Range not found")

                try:
                    # product_brand_element = driver.find_element(By.XPATH, Fragrancess.BRAND)
                    product_brand_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.BRAND)))
                    product_brand = product_brand_element.text.replace('"', '""').strip() if product_brand_element else ''
                except:
                    logging.warning("Brand not found")

                try:
                    # product_volume_element = driver.find_element(By.XPATH, Fragrancess.VOLUME)
                    product_volume_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.VOLUME)))
                    product_volume = product_volume_element.text.replace('"', '""').strip() if product_volume_element else ''
                except:
                    logging.warning("Volume not found")
                try:
                    
                    if product_brand in product_titlee.text:
                        updated_title = product_titlee.text.replace(product_brand, '').strip()
                except:
                    updated_title = "brand not found"
                
                product_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Fragrancess.RRP)))
                product_price_text = product_price.text.replace('RRP:', '').replace('£', '').strip()
                updated_price = float(product_price_text) * 1.5

                weight_match = re.search(r'(\d+ml|\d+ ml)', product_titlee.text, re.IGNORECASE)
                weight = weight_match.group(1).strip() if weight_match else ''
                current_url = driver.current_url
                csvv.make_csv('fragrancedirect.csv', f'"{product_titlee.text}","{product_rrp_text}","{updated_price}","{weight}","{product_over_text}","{product_range}","{product_brand}","{product_volume}",{current_url}\n', new=False)

                time.sleep(2)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
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
