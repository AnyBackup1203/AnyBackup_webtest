# import unittest2
#
# from test.lib.HTMLTestRunner import HTMLTestRunner
#
# if __name__ == '__main__':
#     # 1.找到所有需要执行的测试用例
#
#     suite = unittest2.defaultTestLoader.discover("./test_case","test*.py")
#     # 2.执行找到的测试用例集
#     # unittest2.TextTestRunner().run(suite)
#     # 3.生成测试报告
#     # 3.1.指定测试报告的位置
#     path = "report/TestReport.html"
#     with open(path, 'wb') as file: # w表示写，b表示二进制
#         HTMLTestRunner(stream=file, verbosity=1,title="自动化测试报告",description="测试环境：Chrome",).run(suite)
#     print("这是测试")

print("1")