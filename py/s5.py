import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'Cookie': 'll="118163"; bid=pk9_omA7aIM; __utmz=30149280.1657523047.1.1.utmcsr=aidaxue.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=1508a7b16946effd.1657611526.1.1657611526.1657611526.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1045764713.1657523047.1657538222.1657611527.4; __utmb=30149280.0.10.1657611527; __utmc=30149280; __utma=223695111.958047770.1657611527.1657611527.1657611527.1; __utmb=223695111.0.10.1657611527; __utmc=223695111; __utmz=223695111.1657611527.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=f1533246dbf774e0-22141949b1d300fc:T=1657611527:RT=1657611527:S=ALNI_MbNmVin6ncwF83aCvGlywefIRXB6Q; __gpi=UID=0000079c9a8a1a69:T=1657611527:RT=1657611527:S=ALNI_MYPQAA4_fTLxc5snIPdsFtzwQPbYA'
}
ranks = []
titles = []
ratings = []
inqs = []
countrys = []
genres = []
release_times = []
director_actors = []
pinglun = []

for i in range(10):
    response = requests.get(
        'https://movie.douban.com/top250?' + 'start=' + str(25 * i) + '&filter=', headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    ol = soup.ol
    all_li = ol.find_all('li')
    for li in all_li:
        rank = li.find('em', class_="").string
        title = li.find('span', class_="title").string
        rating = li.find('span', class_="rating_num").string
        info = li.find('div', class_="bd").p.get_text().strip()
        country = info.split('/')[-2]
        genre = info.split('/')[-1]
        release_time = info.split('\n')[1].split('/')[0].replace(" ", "")
        director_actor = li.find('div', class_="bd").p.next_element.replace(
            "\n", "").replace(" ", "")
        pl = li.find('span', class_='inq')

        ranks.append(rank)
        titles.append(title)
        ratings.append(rating)
        countrys.append(country)
        genres.append(genre)
        release_times.append(release_time)
        director_actors.append(director_actor)
        pinglun.append(pl)

    time.sleep(3)
with open('D:\.as.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["排名", "名称", "评分", "国家", "类型", "上映时间", "导演&主演", "评论"])
    for i in range(250):
        writer.writerow([
            ranks[i],
            titles[i],
            ratings[i],
            countrys[i],
            genres[i],
            release_times[i],
            director_actors[i],
            pinglun[i]
        ])
