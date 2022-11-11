import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#from HTMLTestRunner import HTMLTestRunner
a=webdriver.Edge()
class unitest(unittest.TestCase):
    def setUp(self):
        a.get('https://developer.aliyun.com/article/895567')
        a.maximize_window()
        a.refresh()
        print('用例{}开始执行'.format(self))
        sleep(3)
    def tearDown(self):
        a.quit()
        print('用例{}执行结束'.format(self))
    @classmethod
    def setUpClass(cls):
        print('start')
    @classmethod
    def tearDownClass(cls):
        print('off')
    def test_01(self):
        b=a.find_element(By.CSS_SELECTOR,"[class='sc-nav-menu-rec-item-text']").click()
        c=a.find_element(By.CSS_SELECTOR,"[class='sc-nav-menu-message']").click()
        self.assertEqual(b,c)
if __name__=='__main__':
    unittest.main()