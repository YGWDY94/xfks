from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_website(website):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    opt = webdriver.ChromeOptions()
    opt.add_argument('--user-agent=%s' % user_agent)
    browser = webdriver.Chrome(executable_path=r"./chromedriver", options=opt)
    browser.get(website)
    return browser

#browser = webdriver.Chrome(executable_path=r"/Applications/chromedriver", options = opt)
"""
def get_website(website):
    browser = get_browser()
    browser.get(website)
    return browser"""

def login(username, passwd, CAPTCHA, browser):

    username = username
    passwd = passwd
    time.sleep(2)
    elem = browser.find_element_by_name("mobile")
    elem.send_keys(username)
    elem = browser.find_element_by_name("password")
    elem.send_keys(passwd)
    key = CAPTCHA
    elem = browser.find_element_by_name("captcha")
    elem.send_keys(key)
    elem = browser.find_element_by_name("submit")
    elem.click()

    print("LOGIN Succeed!!")
 #   browser.implicitly_wait(10)
    return browser


