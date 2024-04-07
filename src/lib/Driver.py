from selenium import webdriver
from selenium.webdriver import ActionChains

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
