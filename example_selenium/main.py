from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_browser(proxy):
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    options.add_argument('--log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")
    # proxy = "0.0.0.0:00"
    if proxy != "0.0.0.0:00":
        options.add_argument('--proxy-server=%s' % proxy)
    browser = webdriver.Chrome(options=options)
    return browser

def bing_search_url(_question):
    base = "https://cn.bing.com/search?q="
    url = base + _question.lower().replace(" ", "+").replace("?", "%3F").replace("'", "%27")
    return url

proxy = "0.0.0.0:00"
browser = get_browser(proxy)
browser.get(bing_search_url('abc'))
element = WebDriverWait(browser, 5, 0.5)
browser.quit()
