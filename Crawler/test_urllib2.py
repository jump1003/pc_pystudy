#  -*- coding: utf-8 -*-
from urllib import request
import http.cookiejar
url = r'http://www.baidu.com'

print('简单爬取')
response1 = request.urlopen(url)
cnt1 = response1.read()
print(response1.getcode())
print(len(cnt1))

print('爬取二-伪装成浏览器')
req = request.Request(url)
req.add_header('user-agent','Mozilla/5.0')
response2 = request.urlopen(req)
cnt2 = response2.read()
print(response2.getcode())
print(len(cnt2))

print('爬取三-cookie')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
cnt3 = response3.read()
print(response3.getcode())
print(cj)
print(len(cnt1))
