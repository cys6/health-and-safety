import requests
from lxml import etree
import json

"""定位到需要获取的数据"""
url = "https://movie.douban.com/subject/35073886/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}

r = requests.get(url, headers=header,stream=True).text
s =etree.HTML(r)

movie = s.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
daoyan = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
actor = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')

"""把获取到的数据存入字典"""
douban_json = {
    '电影名字': movie,
    '导演': daoyan,
    '演员': actor
}

"""把字典转化为json，并循环9次"""
douban_json_str = [douban_json for i in range(9)]
with open('json/douban.json', 'w', encoding='utf-8') as f:
    json.dump(douban_json_str, f, ensure_ascii=False, indent=9)