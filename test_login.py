#测试用户登录功能
import time
# import PyMouse as PyMouse
from  selenium import webdriver
import unittest2
import os
from selenium.webdriver import ActionChains


class LoginTest(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.test_ip = "10.2.22.61"
        cls.product_id = "7.0.8.0"
    #登录
    def test_1(self):
        #打开网址
        self.driver.get("https://10.2.22.61:9600")
        self.driver.find_element_by_name("userName").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("password123")
        self.driver.find_element_by_xpath("//*[@id='app']/div[2]/div/ng-include/div/div/div/form/div[2]/button").click()
        time.sleep(3)
        text=self.driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[2]/div/div/div[3]/div[2]').text
#        print(text)
        self.assertEqual("登录成功",text)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/div[2]/div[3]/button[1]").click()

    #新建RAID
    def tst_2(self):
        self.driver.find_element_by_link_text("存储").click()
        # 点击节点管理
        self.driver.find_element_by_link_text("节点管理").click()
        time.sleep(3)
        # 点击配置
        self.driver.find_element_by_xpath('//*[@id="node_mgm"]/div[1]/a[3]').click()
        # time.sleep(5)
        # self.driver.find_element_by_link_text("RAID管理").click()
        # time.sleep(5)
        # self.driver.find_element_by_link_text("创建RAID").click()
        # time.sleep(5)
        # #点击下一步
        # self.driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/es-wizard/div/div/div[3]/button[2]').click()
        # time.sleep(5)
        # #勾选
        # self.driver.find_element_by_class_name('es-checkbox-ico').click()
        # #点击创建
        # self.driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/es-wizard/div/div/div[3]/button[3]').click()
        # self.driver.save_screenshot("shot.png")
        # time.sleep(10)
    #新建卷
    def tet_3(self):
        #点击卷管理
        self.driver.find_element_by_xpath('//*[@id="content"]/section/div/div/div/div/div[2]/div/ul/li[3]/a').click()
        time.sleep(5)
        self.driver.find_element_by_link_text("自备份卷").click()
        # time.sleep(5)
        self.driver.find_element_by_link_text("新建").click()
        self.driver.find_element_by_name("volumeName").send_keys("self")
        self.driver.find_element_by_name('number').send_keys("20")
        # self.driver.find_element_by_css_selector(".ng-binding.ng-scope").click()
        self.driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[2]/ng-form/div[4]/div/div/div/div[2]/table/tbody/tr/td[1]/div').click()
        # time.sleep(5)
        self.driver.find_element_by_css_selector('.btn.btn-es-red.ng-scope').click()
        time.sleep(3)
        text=self.driver.find_element_by_xpath('//*[@id="storage_node_volume_selfbackup"]/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[1]/div/span').text
        self.assertEqual("self",text)
    #设置副本数
    def test_4(self):
        self.driver.find_element_by_link_text("系统").click()
        self.driver.find_element_by_link_text("自备份").click()
        self.driver.find_element_by_link_text("策略配置").click()
        js1='document.getElementsByName("beignRunTime")[0].removeAttribute("readonly")'
        self.driver.execute_script(js1)
        self.driver.find_element_by_name('beignRunTime').clear()
        self.driver.find_element_by_name('beignRunTime').send_keys("18:00")
        self.driver.find_element_by_name('number').clear()
        self.driver.find_element_by_name('number').send_keys("7")
        self.driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[3]/button[1]').click()
        time.sleep(3)
    #发起自备份
    def tst_5(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/a[2]').click()
        self.driver.find_element_by_name('desc').send_keys("self")
        self.driver.find_element_by_css_selector('.btn.btn-es-red.ng-scope').click()
        #检查自备份是否发起成功
        tr_list=self.driver.find_element_by_name("selfBackupTable-table-body").find_elements_by_tag_name('tr')
        print(len(tr_list)-1)
        self.assertGreater(len(tr_list)-1,0)
        time.sleep(10)
        self.driver.find_element_by_css_selector('.webfont.icon-refresh').click()
    #删除自备份
    def tet_6(self):
        time.sleep(5)
        tr_list = self.driver.find_element_by_name("selfBackupTable-table-body").find_elements_by_tag_name('tr')
        #表头有个tr标签
        print(len(tr_list)-1)
        for i in range(len(tr_list)-1,0,-1):
            time.sleep(5)
            self.driver.find_element_by_xpath('//table[@name="selfBackupTable-table-body"]/tbody/tr['+str(i)+']/td[2]').click()
            self.driver.find_element_by_css_selector('.btn.btn-es-white.btn-sm.margin-control').click()
            self.driver.find_element_by_css_selector('.btn.btn-es-red.ng-scope').click()
        tr_list = self.driver.find_element_by_name("selfBackupTable-table-body").find_elements_by_tag_name('tr')
        self.assertEqual(len(tr_list) - 1, 0)

        # for row in tr_list:
        #     tdlist=row.find_elements_by_tag_name('td')
        #     for col  in tdlist:
        #         print(col.text)

    #切换语言成英文
    def tet_7(self):
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

    #切换语言成中文
    def tet_8(self):
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

    # 下载自备份
    def test_9(self):
        time.sleep(5)
        self.driver.find_element_by_xpath('//table[@name="selfBackupTable-table-body"]/tbody/tr[1]/td[1]').click()
        text=self.driver.find_element_by_xpath('//table[@name="selfBackupTable-table-body"]/tbody/tr[1]/td[1]').text
        # print(text)

        str = text.replace(':', "_")
        print(str)
        filename = self.test_ip + '_' + self.product_id + '_' + str + ".zip"
        # filename="10.2.22.61_7.0.8.0_2020-03-10-09_27_44.zip"
        download_file = os.path.expanduser('~') + "\\Downloads\\" + filename
        if (os.path.isfile(download_file)):
            os.remove(download_file)
        self.driver.find_element_by_link_text('导出').click()
        time.sleep(3)
        # print(os.path.isfile(download_file))

        self.assertTrue(os.path.isfile(download_file),'file not exist!')


    @classmethod
    def tearDownClass(cls):
        pass

        # cls.driver.quit()
if __name__ == '__main__':
    unittest2.main()

#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/div
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/div
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[1]
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[5]
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]/td[1]
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[8]
#//*[@id="content"]/section/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/table/tbody/tr[7]