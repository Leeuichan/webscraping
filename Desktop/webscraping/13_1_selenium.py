import time
import random
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(random.uniform(1,3))
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")