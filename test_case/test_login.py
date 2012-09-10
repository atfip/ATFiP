#!/usr/bin/env python
#coding=utf-8

# 导入基本环境
# import unittest
from test_data import accounts
from sites import login_page
from lib.utils_lib import start_browser
from lib.utils_lib import stop_browser
from lib.testcase2 import TestCase2


# 定义测试类和测试方法
class TestLogin(TestCase2):
    
    #~ 第一个测试用例
    def test_login_as_super_user(self):
        login_page.go()
        login_page.do_login_as(accounts.super_usr)
    
    #~ 第二个测试用例
    def test_login_as_dev(self):
        login_page.go()
        login_page.do_login_as(accounts.dev_usr)
    
    # #~ 第三个测试用例
    def test_login_as_tester(self):
        login_page.go()
        login_page.do_login_as(accounts.test_usr)

    # 每个测试用例执行前均会执行一次
    def setUp(self):
        start_browser()

    # 每个测试用例执行后均会执行一次
    def tearDown(self):
        stop_browser()

# if __name__ == "__main__":
#     unittest.main()
