import web
urls = (
     '/(.*)', 'index'
)
safety = web.application(urls, globals())
class index:
    def GET(self,name):
        with open(r'/mnt/d/Python/datapyocmeon/web/index.html','r')as f:
            index_text=f.read()
        return index_text
if __name__ == "__main__":
    safety.run()