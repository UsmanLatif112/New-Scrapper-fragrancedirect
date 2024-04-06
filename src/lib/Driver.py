
from lib.imports import *



url = "https://www.fragrancedirect.co.uk/"



def initialize_and_navigate(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_prefs = {}

    # Disable "Save Password" prompt
    chrome_prefs["credentials_enable_service"] = False
    chrome_prefs["profile.password_manager_enabled"] = False

    chrome_options.add_experimental_option("prefs", chrome_prefs)

    # Additional ChromeOptions
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")  # Disable notifications

    # Set a user-agent string to make it appear more like a regular user's browser
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    # Disable the Blink features associated with automation detection
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    actions = ActionChains(driver)

    # Navigate to the specified URL
    driver.get(url)

    return driver