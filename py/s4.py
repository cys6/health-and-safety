import bs4
import requests
from bs4 import BeautifulSoup
url='https://www.baidu.com'
respones=requests.get(url)
soup=BeautifulSoup(respones.content,'lxml')
body=soup.body
title=soup.title
if type(soup)==bs4.BeautifulSoup:
    print(soup.title.string)
for item in body:
    if type(soup.string)==bs4.BeautifulSoup:
        print(item)
for str in soup.stripped_strings:
    print(repr(str))
#find_all(name, attrs, recursive, text,kwargs)
print(soup.find_all('p'))
print(soup.select('title'))