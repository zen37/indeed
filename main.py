import sys
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Define browser choices
class Browsers:
    CHROME = 'chrome'
    EDGE = 'edge'
    FIREFOX = 'firefox'
    SAFARI = 'safari'

# Function to read the browser configuration from config.json
def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config.get('browser', Browsers.CHROME)  # Default to 'chrome' if not found

# Read the browser choice from the configuration file
browser = load_config()  # Example: Set to the desired browser from config.json

# Conditional import and installation of webdriver-manager only if the browser isn't Safari
if browser not in [Browsers.SAFARI]:  # Only import webdriver-manager if the browser isn't Safari
    try:
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
    except ImportError:
        print("Required libraries not found, installing...")
        from subprocess import call
        call([sys.executable, "-m", "pip", "install", "webdriver-manager"])
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
else:
    print("Safari browser selected, no need for webdriver-manager.")

class SeleniumScraper:
    
    def __init__(self, browser: str = Browsers.CHROME):
        self.browser = browser
        self.driver = None

    def open_browser(self):
        if self.browser == Browsers.SAFARI:
            print("Opening Safari browser...")
            self.driver = webdriver.Safari()
        elif self.browser == Browsers.CHROME:
            print("Opening Chrome browser...")
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=ChromeOptions())
        elif self.browser == Browsers.EDGE:
            print("Opening Edge browser...")
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=EdgeOptions())
        elif self.browser == Browsers.FIREFOX:
            print("Opening Firefox browser...")
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=FirefoxOptions())

        self.driver.get("https://www.example.com")

# Example of how to run
scraper = SeleniumScraper(browser=browser)
scraper.open_browser()
