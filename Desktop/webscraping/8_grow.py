

import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/list?titleId=776255"


#grow = soup.find_all("td",attrs={"class":"title"})

#title = grow[0].a.get_text()
#link = grow[0].a["href"]
#print(title)
#print("https://comic.naver.com" + link)

#만화 제목 링크 가져오기
#for cartoon in grow:
 #   title = cartoon.a.get_text()
  #  link = "https://comic.naver.com"+cartoon.a["href"]
   # print(title,link)
   
# 평점 구하기

total_rate = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)
print("평균점수 :", round(total_rate / len(cartoons),2))



    

