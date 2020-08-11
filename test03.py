

from urllib.request import Request , urlopen

from bs4 import BeautifulSoup

req = urlopen("http://media.daum.net")

print(req.getcode())

if req.getcode()==200:

    html = req.read()
    print(html[:256]) # 인코딩을 안했기 때문에 깨질 것

    html = html.decode("utf-8")
    print(html[:256])

else:
    print("http ERROR")


soup = BeautifulSoup(html, "html.parser") # soup 생성

# print(soup.prettify())

print(soup.title)

print(soup.title.text)


# print(bs.prettify()[:1024])

print("")


req = Request("https://movie.naver.com/movie/running/current.nhn")

res = urlopen(req)


html = res.read().decode("utf-8")

bs = BeautifulSoup(html , "html.parser")

print(bs.title)
print(bs.title.name)


currents = bs.find("ul", attrs={"class":"lst_detail_t1"})

for child in currents:

    try:
        titles = child.find("dt", attrs={"class":"tit"})
        for title in titles:
            try:
                # print(title)

                if title.name == "a":
                    print(title.text, title['href'])
            except:
                pass
    except:
        pass


print("")


req = Request("https://movie.naver.com/movie/running/current.nhn")
# print(dir(req))
# print(req.host)

res = urlopen(req)

html = res.read().decode("utf-8")

bs = BeautifulSoup(html,"html.parser")

cm = bs.select(".lst_detail_t1 > li")

print(type(cm))
print("")

for movie in cm:
    titles = movie.select(".lst_dsc > .tit > a")

    for title in titles:
        print(title.text, title['href'])


print("")


# 네이버에서 검색기능


# import os
# import sys

import urllib.request

import json

client_id = "ausQxMUpF8GH02SZxHy0"
client_secret = "btv4u8JNNM"
encText = urllib.parse.quote("핫딜")
url = "https://openapi.naver.com/v1/search/news.json?query={}".format(encText) # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))

    json_rt = response_body.decode('utf-8')
    py_rt = json.loads(json_rt)

    new_list = py_rt['items']

    for news in new_list:
        print("title : {title} @ {pubDate}".format_map(news))

    for news in new_list:
        news['title']
        print("title : {title} @ {pubDate}".format_map(news))

else:
    print("Error Code: %d" %rescode)










