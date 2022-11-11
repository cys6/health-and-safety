import requests
from bs4 import BeautifulSoup
import csv
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'Cookie':'uuid_tt_dd=10_30276077140-1657677988202-279246; dc_session_id=10_1657677988202.229991; c_segment=14; dc_sid=a64eb0feb61d15306a77681483458d3c; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1657677989; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac={"islogin":{"value":"0","scope":1},"isonline":{"value":"0","scope":1},"isvip":{"value":"0","scope":1}}; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30276077140-1657677988202-279246; hide_login=1; __gads=ID=bdf250a52e332d79-22a316332cd500b7:T=1657677990:RT=1657677990:S=ALNI_MZNt23S9QzZqmqJ46cG5aiKISUKYw; __gpi=UID=000007a7f1ad2a8b:T=1657677990:RT=1657677990:S=ALNI_MYO7hbgv8ddbF71Pj9SlwpS1QzC9w; unlogin_scroll_step=1657677994841; SESSION=2f5bc908-69a1-4724-b9b4-f3aadb9f083f; ssxmod_itna=eqGxci0=GQDt0QNGHD8KRx0KT3vbDgD8ip7YhGx0y0oGzDAxn40iDtooTciY6ijDrwefiQEcwQf8mh+3de3/TanzdmDB3DEx065HkYxii9DCeDIDWeDiDG4GmB4GtDpxG=Djjtz1M6xYPDEj5DREPDuxBGDGP1LaKhDeKD0xwFDQ9hLxDr8rY1H3yqkt0DLxG1540HKA3xL=gf6bGzkt8ExfbODl9UDCI1tKypDB+kl1HG/Bn4WYhahODdNQiqGixxoglDoniEpUiKZW3iemhBKCRPwVQDirxYNwhDD=; ssxmod_itna2=eqGxci0=GQDt0QNGHD8KRx0KT3vbDgD8ip7YhDnF8FKDsqNDLex3yS9YqnbIQPQ3lKji9DiUABkywenz=7DNkDc6L0=HdY0khXPav3qEIUP5mD9bnKhUChWngKzt6ajRwby78jHPfriqODs07cFPtDhHgTGj1pTR6WmYOawDontDIFIuBAQC=iq0Qmrw3aAKBRQHcIddFvdLa7IvZb6o43=DrYHdjibSKPQhSf=2fTAEPELQdy4e3aeUBC8PEo=eQGd6UuOf+1L+R=fUS1HPzzAX0aLYiU0om4DwrGdDjKD+rGDD; log_Id_click=1; firstDie=1; c_pref=default; c_ref=default; c_first_ref=default; c_first_page=https://blog.csdn.net/weixin_39229385/article/details/109638442; c_dsid=11_1657680159344.938691; c_page_id=default; dc_tos=rexu73; log_Id_pv=14; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1657680160; log_Id_view=30; FCNEC=[["AKsRol_koTyOQDRAqVsZdQtqT9dF9TxIScMJioI0teqvh6tMgh5BjUW99hbYkM9Q76kaZQbpmxmnQShzkpuWd6lEtGVxaf2uKjo2uHz69pHBh-oOdBfuno7V2_IbWLIFBfEiAmCbnaIbL95_uT6kZeWHeaQPxnnFKQ=="],null,[]]'
}
tex=[]
tit=[]
ura=[]
bus=[]
a=[]
url='https://blog.csdn.net/geekmubai/article/details/81318806'
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,'lxml')
text=soup.text
titlt=soup.title.string
#url=soup.url
body=soup.body
h1=soup.select('h1')
find_all=soup.find_all('p')
tex.append(text)
tit.append(titlt)
ura.append(find_all)
bus.append(body)
a.append(h1)
with open('D:\.pashuju.csv','w',newline='',encoding='utf-8')as f:
    writer=csv.writer(f)
    writer.writerow(['number','all','min','avg','image'])
    #for i in range(1,11):
    writer.writerow(
            [tex,
             tit,
             ura,
             bus,
             a
             ])