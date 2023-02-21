import requests
#url 설정
url = "http://naver.com"
res = requests.get(url,verify=False)
print('응답코드:', res.status_code) # 200 이면 정상


