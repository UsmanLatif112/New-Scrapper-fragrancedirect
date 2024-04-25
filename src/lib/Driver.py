from selenium import webdriver
from selenium.webdriver import ActionChains
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def initialize_and_navigate(url):
    chrome_options = webdriver.ChromeOptions()

    # Disable "Save Password" prompt
    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)

    # Additional ChromeOptions
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    return driver

# def get_undetected_chrome_browser(profile=None):
#     """Returns an instance of an undetected Chrome browser with added features to make it more undetectable and secure.
#     The browser will save the profile and cookies to the specified folder so that you don't have to log in every time.

#     Returns:
#         uc.Chrome: An instance of the Chrome class from the undetected_chromedriver library.
#     """
#     options = uc.ChromeOptions()
#     if profile:
#         options.user_data_dir = f"{BASE_DIR}/profile/{profile}"
#     driver_version = "122.0.6261.58"  # You can also specify a specific version here
#     driver_path = ChromeDriverManager(driver_version=driver_version).install()
#     return uc.Chrome(options=options, executable_path=driver_path)
