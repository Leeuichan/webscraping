import requests
from bs4 import BeautifulSoup
import re


url = "https://www.coupang.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup)
#items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[1].find("div",  attrs={"class":"name"}).get_text())



