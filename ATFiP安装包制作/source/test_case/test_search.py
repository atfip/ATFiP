#!/usr/bin/env python
#coding=utf-8

# 导入基本环境
import unittest
from test_data import keywords
from sites import home_page
from lib.utils_lib import start_browser
from lib.utils_lib import stop_browser
from lib.testcase2 import TestCase2


# 定义测试类和测试方法
class TestSearch(TestCase2):
    
    #~ 第一个测试用例
    def test_search_use_keyword1(self):
        home_page.goto()
        home_page.search_by_keyword(keywords.keyword1)
    
    #~ 第二个测试用例
    def test_search_use_keyword2(self):
        home_page.goto()
        home_page.search_by_keyword(keywords.keyword2)
    
    # #~ 第三个测试用例
    def test_search_use_keyword3(self):
        home_page.goto()
        home_page.search_by_keyword(keywords.keyword3)

    # 每个测试用例执行前均会执行一次
    def setUp(self):
        start_browser()

    # 每个测试用例执行后均会执行一次
    def tearDown(self):
        stop_browser()

if __name__ == "__main__":
    unittest.main()
