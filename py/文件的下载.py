import requests
from clint.textui import progress
url = 'https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg'
res = requests.get(url, stream=True)
with open("D:\py.pkg", "wb") as pypkg:
    for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=len(res.content), width=100):
        if chunk:
            pypkg.write(chunk)
"""下载用request库，使用progress进度条"""




