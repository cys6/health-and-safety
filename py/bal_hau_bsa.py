import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
'Cookie':'ll="118163"; bid=pk9_omA7aIM; __utmc=30149280; __utmz=30149280.1657523047.1.1.utmcsr=aidaxue.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.8cb4=["","",1657538221,"https://www.aidaxue.com/"]; _pk_ses.100001.8cb4=*; __utma=30149280.1045764713.1657523047.1657530773.1657538222.3; __utmt=1; _pk_id.100001.8cb4=d5a1b1ad6b1f052b.1657523046.3.1657538263.1657531669.; __utmb=30149280.2.10.1657538222'}
http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
proxyDict = {
    "http": http_proxy,
    "https": https_proxy,
    "ftp": ftp_proxy}
data={
    'cat':2022,
    'q':'python'}
response = requests.get('https://www.douban.com/', headers=headers,params=data)
response.encoding='utf-8'
print(response.url)
print(response.headers['Content-Type'])
print(response.text)
