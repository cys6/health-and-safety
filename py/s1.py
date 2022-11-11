import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
         'Cookie':'clickbids=null,256633; Hm_lvt_39d0ce19435c71b8f03cc434eab7b9b7=1657595979; Hm_lpvt_39d0ce19435c71b8f03cc434eab7b9b7=1657595991'}
data={
    'dog':'2019',
    'a':'python'}
response=requests.get('http://www.gebiqu.com/biquge_256633/62905551.html',headers=headers,params=data)
response.encoding='utf-8'
print(response.headers)
print(response.url)
#print(response.text)
#print(response.content)