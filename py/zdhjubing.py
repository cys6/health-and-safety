from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
def t():
    a=webdriver.Edge()
    a.get('https://www.baidu.com')
    a.maximize_window()
    a.refresh()
    #a.find_element(By.ID,'kw').send_keys('nihaoa')
    a.find_element(By.XPATH,'//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()
    ah=a.current_window_handle#获取当前句柄
    ahs=a.window_handles#获取全部句柄
    for bh in ahs:
        if ah!=bh:
            a.switch_to.window(bh)#确定是新句柄时，切换到新句柄
            #a.switch_to.window(ahs[1])
            a.find_element(By.XPATH,'//*[@id="1"]/div/div/div[1]/div').click()
            a.find_element(By.XPATH,'//*[@id="tsn_inner"]/div[2]/div').click()
            a.find_element(By.XPATH,'//*[@id="1"]/div/div/div/div/div[2]/p[1]/a/em').click()
            #sleep(3)
    #aha=a.current_window_handle
    ahas=a.window_handles
    #print(ahas)
    a.switch_to.window(ahas[2])
    #a.find_element(By.CSS_SELECTOR,'[class=styles-module_content_tf9vk]').click()
    if __name__=='__main__':
        print(ahs)
        print(ah)
    sleep(9)
    a.quit()
t()
'''
总结：
    句柄的操作：a.current_window_handle(获取当前句柄)
              a.window_handles(获取全部句柄)
              a.switch_to.window(新句柄[])切换到新句柄，可以for循环,可以利用索引
'''