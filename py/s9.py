import requests
from bs4 import BeautifulSoup
def pachongshuju_get():
    url='https://tag.planning.momenta.works/audit/'
    respose=requests.get(url)
    soup=BeautifulSoup(respose.content,'lxml')
    title=(soup.title).text
    print(title)
pachongshuju_get()
"""
alter table xxx add xxx xx()
selct from where group by having order by limit
avg count max min sum
insert into  delete for  update set
natural join/left join/right join/inner join
add index on/create view view_name as select
rename round show dorp databases() int char varchar
select *from t natural join a where a.id=9 group by name='limeimei' having avg(source)>9% order by desc limit(1,9)
"""