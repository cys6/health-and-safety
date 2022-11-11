from bs4 import BeautifulSoup
import requests
import csv
url='https://www.baidu.com'
#headers={
    #'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    #'cookie': 'JSESSIONID=0ACBEA37483EA8C5617B0E38916A0D8D; atlassian.xsrf.token=BMSH-Y9ET-KTF3-XH7F_00de2e35d9e25783169ba3c141cbe1c2d2076efa_lin'
    #}
response=requests.get(url)
soup=BeautifulSoup(response.content,'lxml')
b=[]
tit=soup.body
for body in tit:
    b.append(body)
with open(r'D:\9.csv','w',encoding='utf-8')as f:
    write=csv.writer(f)
    write.writerow(['hollo'])
    write.writerow([b])
