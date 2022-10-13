from selenium import webdriver

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-feature=AutomationControlled")
    browser = webdriver.Chrome(options=options)
    browser.get("http://selenium.dev/")
    return browser

browser = get_browser()
e = browser.find_element(by="xpath", value="/html/body/div/main/section[1]/div/div/div/div/h1")
print(e.text)    