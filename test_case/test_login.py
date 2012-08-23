#!/usr/bin/env python
#coding=utf-8

# 导入基本环境
import unittest
import sys
sys.path.append("..")
from test_data import accounts
from sites.login_page import LoginPage
from sites.home_page import HomePage
from lib.utils_lib import start_browser


# 定义测试类和测试方法
class TestLogin(unittest.TestCase):
	
	#~ 第一个测试用例
	def test_login_as_super_user(self):
		login_page = LoginPage(self.browser)
		login_page.go()
        login_page.loaded()
		login_page.do_login_as(accounts.super_usr)
		home_page = HomePage(self.browser)
		home_page.loaded()
		home_page.comfirm_login_succeed(accounts.super_usr)
	
	#~ 第二个测试用例
	def test_login_as_dev(self):
		login_page = LoginPage(self.browser)
		login_page.go()
		login_page.do_login_as(accounts.dev_usr)
		home_page = HomePage(self.browser)
		home_page.go()
		home_page.comfirm_login_succeed(accounts.dev_usr)
	
	#~ 第三个测试用例
	def test_login_as_tester(self):
		login_page = LoginPage(self.browser)
		login_page.go()
		login_page.do_login_as(accounts.test_usr)
		home_page = HomePage(self.browser)
		home_page.go()
		home_page.comfirm_login_succeed(accounts.test_usr)		

	# 每个测试用例执行前均会执行一次
	def setUp(self):
		self.browser = start_browser()

	# 每个测试用例执行后均会执行一次
	def tearDown(self):
		self.browser.quit()

if __name__ == "__main__":
	unittest.main()
