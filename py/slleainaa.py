from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
import requests
from bs4 import BeautifulSoup

a = webdriver.Edge()


def local(u, m):
    a.get('https://tag.planning.momenta.works/#/mark_task_hall?tag_type=HNP_MS1')
    a.maximize_window()
    a.refresh()
    a.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/form/div[1]/div/div/div/div/span/input').send_keys(u)
    a.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/form/div[2]/div/div/div/div/span/input').send_keys(m)
    a.find_element(By.CSS_SELECTOR, "[class='ant-btn ant-btn-primary ant-btn-lg']").click()
    sleep(3)


local('yongshun.cao.ext', 'cYS686858')
"""登录momenta数据标注平台"""


def jubing():
    qy = a.current_window_handle
    print(qy)
    QY = a.window_handles
    print(QY)
    for Qy in QY:
        if Qy != qy:
            a.switch_to.window(Qy)


jubing()
sleep(3)
"""获取页面跳转的句柄"""


def tag():
    a.find_element(By.CSS_SELECTOR, '/html/body/div[1]/section/header/ul/li[2]').click()
    a.find_element(By.CSS_SELECTOR, "[class='ant-select-selection-search-input']").click()
    # a.find_element(By.CSS_SELECTOR,"[class='ant-btn ant-btn-primary ant-btn-block']").click()


tag()
"""元素定位，元素操作"""
sleep(3)
if __name__ == '__main__':
    texa = []
    title = []
    ur = []


    def momenta_shuju():
        url = 'https://tag.planning.momenta.works/#/abnormal'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.text
        titlt = soup.title.string
        ul = soup.url
        texa.append(text)
        title.append(titlt)
        ur.append(ul)


    momenta_sj()
    # 获取数据标注平台需要的数据
with open('D:\sll.csv', 'w', encoding='utf-8') as f:
    try:
        write = csv.writer(f)
        write.writerow(['文本', '开头', '链接'])
        write.writerow(
            [texa,
             title,
             ur
             ])
        print('成功创建sll表格sll')
    except:
        print('sll未成功创建，出了点小状况')
    """创建表格保存数据"""
a.quit()
