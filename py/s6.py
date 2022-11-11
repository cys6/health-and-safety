import bs4
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}
url = 'https://axutongxue.com/'
respones = requests.get(url, headers=headers)
soup = BeautifulSoup(respones.text, 'lxml')
titles = soup.title
for title in titles:
    if type(title) == bs4.BeautifulSoup:
        print(title)
for str in soup.stripped_strings:
    print(str)
