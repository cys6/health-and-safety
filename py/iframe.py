from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
a=webdriver.Edge()
a.get('https://126.com/')
a.maximize_window()
sleep(3)
#a.find_element(By.XPATH,'//*[@id="lbApp"]').click()
def fra():
    iframe=a.find_element(By.CSS_SELECTOR,'[scrolling="no"]')
    a.switch_to.frame(iframe)
    sleep(3)
    a.find_element(By.CSS_SELECTOR,"[name= 'email']").send_keys('vv')
    a.switch_to.default_content()#返回最外层iframe
    sleep(9)
    a.quit()
fra()
#from zdhjubing import t
#t()
'''
总结：
    iframe标签的切换使用:
        嵌套在一个HTML里面的另一个HTML
        如果想定位到嵌套的HTML，要先定位iframe标签(iframe=a.find_element(By.CSS_SELECTOR,''))
        在切换到该HTML页面(a.switch_to.frame(iframe))
        操作完成，想操作外面的HTML，就需要推出当前的HTML(a.switch_to.default_content())
'''