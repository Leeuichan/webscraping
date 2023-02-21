from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

#Chrome driver 이용
def open_chrome(url):
    driver = webdriver.Chrome(chrome_options=chrome_option)
    driver.get(url)
 #네이버 url지정
open_chrome("http://naver.com")
# 네이버 로그인 element 지정
elem = open_chrome.driver.find_element(By.CLASS_NAME, 'link_login')
#login click
elem.click()
