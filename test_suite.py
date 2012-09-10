#!/usr/bin/env python
#coding=utf-8

# 导入 unittest 测试用例管理模块
import unittest

# import ATFiP config info
import config

# 导入测试用例
from test_case.test_login import TestLogin

# 创建各种 test suite 对 test case 进行组织和打包

# 创建冒烟测试用例集
def ts_smoking_test():
    # 可以为每个 test suite 指定所适用的浏览器类型. 如果不指定, 则以 config.py 中的配置为准
    # config.browser_type = "Chrome"
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestLogin("test_login_as_super_user"))
    test_suite.addTest(TestLogin("test_login_as_dev"))
    test_suite.addTest(TestLogin("test_login_as_tester"))
    return test_suite
    
# 创建全量测试用例集
def ts_all_test():
    config.browser_type = "Firefox"
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestLogin("test_login_as_super_user"))
    test_suite.addTest(TestLogin("test_login_as_dev"))
    test_suite.addTest(TestLogin("test_login_as_tester"))
    return test_suite

# 组合多个用例集到一起
def ts_combine_test():
    test_suite = unittest.TestSuite([ts_smoking_test(), ts_all_test()])
    return test_suite

