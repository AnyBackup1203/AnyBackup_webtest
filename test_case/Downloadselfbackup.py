#下载自备份文件
import unittest2
from selenium import webdriver
import os
import time
class Downloadselfbackup(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.test_ip = "10.2.22.61"
        cls.product_id = "7.0.8.0"
    #登录
    def test_1(self):
        self.driver.get("https://10.2.22.61:9600")
        self.driver.find_element_by_name("userName").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("password123")
        self.driver.find_element_by_xpath(
            "//*[@id='app']/div[2]/div/ng-include/div/div/div/form/div[2]/button").click()
        time.sleep(3)
        #text = self.driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div/div[3]/div[2]').text
        #print(text)
        # self.assertEqual("登录成功", text)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/div[2]/div[3]/button[1]").click()

    #发起自备份(未完待续，先要发起一个自备份）
    def test_2(self):
        self.driver.find_element_by_link_text("系统").click()
        self.driver.find_element_by_link_text("自备份").click()

    # 下载自备份
    def test_9(self):
        time.sleep(5)
        self.driver.find_element_by_xpath('//table[@name="selfBackupTable-table-body"]/tbody/tr[1]/td[1]').click()
        text = self.driver.find_element_by_xpath(
            '//table[@name="selfBackupTable-table-body"]/tbody/tr[1]/td[1]').text
        # print(text)
        str = text.replace(':', "_")
        print(str)
        filename = self.test_ip + '_' + self.product_id + '_' + str + ".zip"
        # filename="10.2.22.61_7.0.8.0_2020-03-10-09_27_44.zip"
        download_file = os.path.expanduser('~') + "\\Downloads\\" + filename
        print(download_file)
        if (os.path.isfile(download_file)):
            os.remove(download_file)
        self.driver.find_element_by_link_text('导出').click()
        time.sleep(3)
        self.assertTrue(os.path.isfile(download_file), 'file not exist!')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
if __name__ == '__main__':
    unittest2.main()