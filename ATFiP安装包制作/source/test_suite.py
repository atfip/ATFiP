#!/usr/bin/env python
#coding=utf-8

# 导入 unittest 测试用例管理模块
import unittest

# import ATFiP config info
import config

# 导入测试用例
from test_case.test_search import TestSearch

# 创建各种 test suite 对 test case 进行组织和打包       
# 创建全量测试用例集
def ts_all_test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestSearch("test_search_use_keyword1"))
    test_suite.addTest(TestSearch("test_search_use_keyword2"))
    test_suite.addTest(TestSearch("test_search_use_keyword3"))
    return test_suite