from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


 
#browser = webdriver.Chrome()
#browser.get("http://naver.com")

def open_chrome(url):
    driver = webdriver.Chrome(chrome_options=chrome_option)
    driver.get(url)
    
open_chrome("http://naver.com")
elem = open_chrome.driver.find_element(By.CLASS_NAME, 'link_login')
elem.click()