import re
def print_match(m):
    if m:
        print(m.group()) #일치하는 문자열 반환
        print(m.string)  # 입력받은 문자열
        print(m.start())
        print(m.end())
        print(m.span())
    else:
        print('fail')
p = re.compile("ca.e")

#m = p.match('caffe') #주어진 문자열의 차음부터 일치하는지 화인
#m = p.search('careless')
lst = p.findall('good care cafe') #일치하는 모든 것을 리스트 형태 반환
#print_match(m)
print(lst)