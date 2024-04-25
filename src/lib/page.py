import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import csv
from PIL import Image
import logging




def navigate_to_next_page(driver, next_button_xpath):
    try:
        time.sleep(2)
        next_button = driver.find_element(By.XPATH, next_button_xpath)
        next_button.click()
        time.sleep(3)  # wait for the page to load
        return True
    except Exception as e:
        logging.warning(f"Failed to navigate to next page: {e}")
        return False

def download_image_with_resolution(img_url, resolution, product_folder, product_titlee):
    img_name = os.path.basename(img_url)
    img_response = requests.get(img_url, stream=True)
    
    if img_response.status_code == 200:
        img_path = os.path.join(product_folder, img_name)
        with open(img_path, 'wb') as img_file:
            for chunk in img_response.iter_content(chunk_size=8192):
                img_file.write(chunk)
        
        # Get actual image resolution
        with Image.open(img_path) as img_file:
            width, height = img_file.size
        
        logging.info(f"Downloaded {img_name} with resolution {width}x{height} for product {product_titlee.text} successfully.")
    else:
        logging.warning(f"Failed to download {img_name} for product {product_titlee.text}.")

    
class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    
    def click_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
    def enter_name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
        
    def enter_name_delay(self, xpath: str, clientname: str, delay=0.2):
        element = self.wait(xpath)
        element.clear()
        for char in clientname:
            element.send_keys(char)
            time.sleep(delay)
            
    def wait(self, xpath, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            logging.warning(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
        
    def waiTENt(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            logging.warning(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
        
    def waaiite(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            logging.warning(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
    def waaiiten(self, xpath, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            logging.warning(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
        
    def waitsix(self, xpath, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            logging.warning(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
    def waitinput(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            logging.warning(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
    
    def make_csv(self, filename: str, data, new=True, encoding='utf-8'):
        mode = 'w' if new else 'a'
        with open(filename, mode, newline='', encoding=encoding) as f:
            f.writelines(data)