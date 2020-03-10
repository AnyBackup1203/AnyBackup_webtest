#切换语言测试
import unittest2
import time
from selenium import webdriver
import os
class ChangeLanguage(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.path=os.getcwd()
        cls.screenshot_dir = os.path.abspath(os.path.dirname(cls.path) + os.path.sep + ".")

    # 登录
    def test_1(self):
        print(self.path)
        self.driver.get("https://10.2.22.61:9600")
        self.driver.find_element_by_name("userName").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("password123")
        self.driver.find_element_by_xpath(
            "//*[@id='app']/div[2]/div/ng-include/div/div/div/form/div[2]/button").click()
        time.sleep(3)
        text = self.driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div/div[3]/div[2]').text
        #        print(text)
        # self.assertEqual("登录成功", text)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/div[2]/div[3]/button[1]").click()

    #切换语言成英文
    def test_2(self):
        time.sleep(5)
        # m=PyMouse()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/ht-top-nav/nav/div[2]/ul/li[4]/a').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/ht-top-nav/nav/div[2]/ul/li[4]/ul/li[2]/a').click()
        self.driver.find_element_by_css_selector('.btn.btn-es-red.ng-scope').click()
        time.sleep(3)
        # ActionChains(self.driver).move_to_element(ele1).perform()
        #检查语言是否切换成英语
        text=self.driver.find_element_by_css_selector('.title.ng-scope').text
        print(text)
        self.assertEqual("Node Status",text)
        self.driver.save_screenshot(self.screenshot_dir+'\\report\ChangeLanguage_to_english.png')

    #切换语言成中文
    def test_3(self):
        time.sleep(5)
        # m=PyMouse()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/ht-top-nav/nav/div[2]/ul/li[4]/a').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/ht-top-nav/nav/div[2]/ul/li[4]/ul/li[1]/a').click()
        self.driver.find_element_by_css_selector('.btn.btn-es-red.ng-scope').click()
        time.sleep(3)
        # ActionChains(self.driver).move_to_element(ele1).perform()
        #检查语言是否切换成英语
        text=self.driver.find_element_by_css_selector('.title.ng-scope').text
        print(text)
        self.assertEqual("设备状态",text)
        self.driver.save_screenshot(self.screenshot_dir + '\\report\ChangeLanguage_to_chinese.png')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
if __name__ == '__main__':
    unittest2.main()




