

# 모듈


from t1 import w1 as t1_w1, w2 as t1_w2, f1 as t1_f1

w1 = "t1 hello"
w2 = "t1 world"

def f1():
    print("test02.py f1() 함수")

if __name__ =='__main__':


    print(w1)
    print(w2)
    print(t1_w1)
    print(t1_w2)

    f1()
    t1_f1()

print("")
# 예외 처리


try:
    
    a = 10
    
    b = 0
    
    print(a,b)
    print(a/b)

except ZeroDivisionError:
    print("ZeroDivisionError 발생")
except IndexError:
    print("IndexError 발생")

print("")
#예외 처리 확장


print("try 성공시")
print("")

try:

    a = 10

    b = 0

    print(a , b)

except ZeroDivisionError:
    print("ZeroDivisionError 발생")
except IndexError:
    print("IndexError 발생")

else:
    print("try 정상적 실행 >> else 실행")

finally:
    print("최종적으로 무조건 실행!")


print("")
print("try 실패시")
print("")

try:

    a = 10

    b = 0

    print(a/b)

except ZeroDivisionError:
    print("ZeroDivisionError 발생")
except IndexError:
    print("IndexError 발생")

else:
    print("try 정상적 실행  >> else 실행")

finally:
    print("최종적으로 무조건 실행!")

print("")

# 강제로 에러 발생


def f(x):
    if x==1:
        raise ValueError("1을 넣지 마세요!")
    else:
        print("success")


f(2)

print("")


# 모듈

# pip install requests

import requests as rq

url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=189618"

res = rq.get(url)
res = rq.post(url)


print(res)
print(res.status_code) # 응답코드
print(res.headers) # 헤더 가져오기
print(res.cookies) # 쿠키 가져오기
print(res.text) # HTML 코드 가져오기
print(res.content) # 바이너리 형태로 변환된 HTML 코드 가져오기
print(res.encoding) # 페이지 인코딩 확인

print("")

# 쿼리 스트링으로 만들어서 요청

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url, params={"key1":"value1" , "key2":"value2"})

print(res.url)

print("")

# Header body에 포함하여 요청

url = "http://blog.naver.com/pjt3591oo"

res = rq.post(url, params={"key1":"value1" , "key2":"value2"})

print(res.url)

print("")
# 헤더를 만들어서 요청

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url, headers={"User-Agent":"Mozilla/5.0(Macintosh:Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})

print(res.url)
print("")


# 예외처리

try:
    url = "http://blog.naver.com/pjt3591oo"

    res = rq.get(url)

    print(res.url)

except rq.exceptions.HTTPError:
    print("HTTP 에러 발생")

except rq.exceptions.Timeout:
    print("TimeOut 에러 발생")


print("")
# TimeOut 에러가 발생한다면 딜레이를 주면 된다.

import time

url = "http://blog.naver.com/pjt3591oo"
delay_time = 1

def connection(u):
    return rq.get(u)

try:
    connection(url)

except rq.exceptions.Timeout:
    time.sleep(delay_time)
    connection(url)

print("")


from urllib.request import urlopen, Request

url = "http://blog.naver.com/pjt3591oo"

req = Request(url)
page = urlopen(req)

print(page) # 응답객체
print(page.code) # 응답코드
print(page.headers) # 헤더확인
print(page.url) # 요청 URL 확인
print(page.info().get_content_charset()) # 인코딩 설정 확인
print(page.read()) # HTML 코드 가져오기

# urllib는 없는 페이지 요청시 에러 발생

url = "http://blog.naver.com/pjt3591oo/1/"

req_post = Request(url)
page = urlopen(req_post)

print(page)
print(page.url)

# urllib은 data의 유무로 get 요청과 post 요청을 구분함

from urllib.request import urlopen, Request

import urllib

url = "http://blog.naver.com/pjt3591oo"

data = {"key1":"value1", "key2":"value2"}
data = urllib.parse.urlencode(data)
data = data.encode("utf-8")

req_post = Request(url, data=data, headers={}) # 2번째 인자 데이터, 세번째 인자 헤더
page= urlopen(req_post)

print(page)
print(page.url)


req_get = Request(url+'?key1=value1&key2=value2',None,headers={}) # 2번째 인자 데이터, 세번째 인자 헤더
page=urlopen(req_get)

print(page)
print(page.url)

print("")


# requests와 urllib은 요청시 요청 객체를 만드는 방법에 차이가 있음

# 데이터를 보낼 때 requests는 딕셔너리 형태로 urllib는 인코딩 해 바이너리 형태로 전송

# requests는 요청 메소드(get,post)를 명시하지만 urllib는 데이터 여부에 따라 get, post 요청 구분

# 없는 페이지 요청 시 requests는 에러를 띄우지 않지만 urllib은 에러 발생


# 파서 모듈

# bs4를 사용하여 HTML 코드를 파이썬이 사용가능한 객체로 변경

# pip install bs4로 설치
# bs4를 사용할 때 lxml이 필요한데 만약 없다면 pip install lxml을 이용해 설치

from bs4 import BeautifulSoup

html = """"""

soup = BeautifulSoup(html,'lxml')

# 파서 종류

# lxml : XML 해석도 가능한 파서, 파이썬 2.x , 3.x 모든 버젼 사용 가능, 처리속도 매우 빠름(c로 구현)
# html5lib : 웹 브라우저 방식으로 HTML을 해석, 처리속도가 매우 느림, 파이썬 2.x 버전 전용





# 셀레니움

# javaScript로 인해 requests 모듈로 정상적인 HTML을 가져오지 못할 경우 , 웹 자동 테스팅 프레임워크인 selenium을 이용하면 편리하게 크롤링 가능
# pip install selenium으로 설치
# 피시에 설치된 웹 드라이버 설치가 필요.
# https://sites.google.com/a/chromium.org/chromedriver/downloads << 크롬

from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe') # 해당 코드 실행시 빈 웹브라우저 실행

# chd = webdriver.Chrome('chromedriver.exe')
# ied = webdriver.Ie('IEDriverServer.exe')
# ffd = webdriver.Firefox('FirefoxDriver.exe')



html="""<html><head></head><p>d<test/p></html>"""

startTime = time.time()

BeautifulSoup(html,'lxml')

lxml_end_time = time.time()-startTime


startTime = time.time()

BeautifulSoup(html,'html5lib')

html5lib_end_time = time.time()-startTime


print("lxml 시간 측정 : %f"%(lxml_end_time))
print("html5lib 시간 측정 : %f"%(html5lib_end_time))
print(html5lib_end_time/lxml_end_time)

print("")


# prettify() << 정렬해줌

html = """<html><head><title>test</title><head><body><p>test</p><p>test2</p></body></html>"""
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print("")

# find_all(), find(), select() 를 이용해 원하는 요소를 리스트 또는 단일 객체의 형태로 가져올 수 있음
# class 와 id를 이용해 DOM에 접근한다
# id값은 find()로 , class 는 find_all()이나 select()로 접근하면 효율적인 코드 작성이 가능하다


# 태그, 아이디를 이용해 DOM 가져오기

html = """<html><head><title>test</title><head><body><p>test</p><p id='d'>test2</p><p>test3</p></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.find_all('p', id='d'))
print(soup.find_all('p', id='c'))
print("")

# 태그, 클래스를 이용해 DOM 가져오기


html = """<html><head><title>test</title><head><body><p>test</p><p class='d'>test2</p><p class='c'>test3</p></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.find_all('p', class_='d'))
print(soup.find_all('p', class_='c'))
print("")
# 여러개의 태그를 이용해 이용해 DOM 가져오기


html = """<html><head><title>test</title><head><body><p>test</p><p class='d'>test2</p><p class='c'>test3</p><a>a 태그</a><b>b 태그</b></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.find_all(['a','b']))
print("")

# 태그, 텍스트를 이용해 DOM 가져오기


html = """<html><head><title>test</title><head><body><p>test1</p><p class='d'>test2</p><p class='c'>test3</p></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.find_all('p', text="test1"))
print(soup.find_all('p', text="t"))
print("")


# find()

html = """<html><head><title>test</title><head><body><p id='i' class='a'>test1</p><p class='d'>test2</p><p class='d'>test3</p></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.find('p', class_="d"))
print(soup.find('p', class_="d"))
print(soup.find('p', id="i"))
print("")


# select

html = """<html><head><title>test</title><head><body><div><p id='i' class='a'>test1</p><p class='d'>test2</p></div><p class='d'>test3</p></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.select('body p'))
print(soup.select('body .d'))
print(soup.select('body p.d'))
print(soup.select('body #i'))
print(soup.select('body p#i'))
print(soup.select('div p'))
print("")


# extract()는 필요없는 태그를 없앨 때 사용한다.
# 주로 script나 style 같이 크롤링 시 필요없는 태그를 없앨 때 사용한다
# 제거할 돔을 선택하기 위해 find 등과 같이 사용한다.
# extract()는 제거한 돔을 반환한다.


html = """<html><head><title>test</title><head><body><div><p id='i' class='a'>test1</p><p class='d'>test2</p></div><p class='d'>test3</p><a>a 태그</a><b> b 태그</b></body></html>"""
soup = BeautifulSoup(html,'lxml')

for tag in soup.find_all(['p','a']):
    print(tag.extract())

print("제거완료")
print(soup)
print("")


# 정규식
# https://regexr.com에서 정규표현식 연습 가능

import re


html = """<html><head><title>test</title><head><body><div><p id='i' class='a'>test1</p><p class='d'>test2</p></div><p class='d'>test3</p><a href="/example/test1">a 태그</a><b> b 태그</b></body></html>"""
soup = BeautifulSoup(html,'lxml')

print(soup.find_all(class_=re.compile('d'))) # 클래스
print(soup.find_all(id=re.compile('i'))) # 아이디
print(soup.find_all(re.compile('t'))) # 태그에 t가 포함된 모든 요소
print(soup.find_all(re.compile('^t'))) # 태그가 t로 시작하는 모든 요소
print(soup.find_all(href=re.compile('/'))) # href에 /가 포함된 모든 요소


print("")

# 대문자 + 소문자 찾기

test_str = """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrstuAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/<>
12345 -98.7 3.141 .6180 9,000 +42"""

pattern1 = re.compile('[a-zA-Z]')
pattern2 = re.compile('[a-zA-Z]+')
c = pattern1.findall(test_str)
d = pattern2.findall(test_str)

print(c)
print(d)
print("")


test_num = "저의 전화번호는 010-6666-7777입니다"

pattern10 = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
pattern11 = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
pattern12 = re.compile('\d{3}-\d{4}-\d{4}')

pf1 = pattern10.findall(test_num)
pf2 = pattern11.findall(test_num)
pf3 = pattern12.findall(test_num)

print(pf1)
print(pf2)
print(pf3)

print("")


test_str = """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrstuAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/<>
12345 -98.7 3.141 .6180 9,000 +42"""

pattrn20 = re.compile('[a-zA-Z0-9]+') # a~z , A~Z , 0~9
pattrn21 = re.compile('\w+')

pf11 = pattrn20.findall(test_str)
pf12 = pattrn21.findall(test_str)

print(pf11)
print(pf12)

print("")

pattrn22 = re.compile('[^a-z]+') # a~z 까지 포함되지 않는 것
pf13 = pattrn22.findall(test_str)
print(pf13)

print("")

pattrn23 = re.compile('[^A-Z]+') # a~z 까지 포함되지 않는 것
pf14 = pattrn23.findall(test_str)
print(pf14)

print("")

pattrn24 = re.compile('t..t') # t문자문자t 패턴
pattrn25 = re.compile('t...t') # t문자문자문자t 패턴
pf15 = pattrn24.findall(test_str)
pf16 = pattrn25.findall(test_str)
print(pf15)
print(pf16)

print("")


pattrn26 = re.compile('t?est\w+') # test나 est로 시작하는 문자열 뒤에 \w가 있어야 됨
pattrn27 = re.compile('t?est\w*') # test나 est로 시작하는 문자열 뒤에 \w가 없어도 됨
pf17 = pattrn26.findall(test_str)
pf18 = pattrn27.findall(test_str)
print(pf17)
print(pf18)

print("")

# pjt35910oo.github.io

def get_posts(soup): # 돔 접근
    return soup.select('body main.page-content div.wrapper div.home div.p')

def data_parse(posts): # 돔에서 필요한 데이터 뽑기

    for post in posts:
        title = post.find('h3').text.strip()
        descript = post.find('h4').text.strip()
        author = post.find('span').text.strip()
        print(title,descript,author)

base_url = "https://pjt3591oo.github.io"
page_path = "/page%d" # url 변경 가능하도록 포맷팅
page = 2

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')

posts = get_posts(soup)
data_parse(posts)

while True: # 다음페이지로 접속할 수 있도록 반복문 이용
    sub_path = page_path%(page) # url 생성
    page += 1
    res = rq.get(base_url + sub_path)

    if(res.status_code!=200): # 200아니면 탈출
        break

    soup = BeautifulSoup(res.content,'lxml')
    posts = get_posts(soup)
    data_parse(posts)

