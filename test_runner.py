#!/usr/bin/env python
#coding=utf-8

# 导入 unittest 测试用例管理模块
import unittest
import config
from lib.HTMLTestRunner import HTMLTestRunner


# 导入需要执行的测试用例集
from test_suite import ts_all_test, ts_smoking_test

# 可以在运行前设定统一的全局浏览器类型设置, 如果不指定, 则以 test suite 中的配置为准
#~ config.final_browser_tyep = "Chrome"


# 定义统一的测试执行方法
def run_test(test_suite):
	with open("./report/my_report.html", "wb") as f:
		runner = HTMLTestRunner(
					stream=f,
					verbosity=2,
					title='My test',
					description='This demonstrates the report output by HTMLTestRunner.'
					)
		runner.run(test_suite)
	

# 执行测试用例
if __name__ == '__main__':
	run_test(ts_smoking_test())

