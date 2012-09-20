#!/usr/bin/python
#coding=utf-8

import config
from lib.utils_lib import run_test
from lib.utils_lib import get_object_name

# 导入需要执行的测试用例集
from test_suite import ts_all_test

# 可以在运行前设定统一的全局浏览器类型设置, 如果不指定, 则以 test suite 中的配置为准
# config.final_browser_tyep = "IE"

def main():
	run_test(ts_all_test())

# 执行测试用例
if __name__ == '__main__':
	run_test(ts_all_test(), get_object_name(ts_all_test, globals()), True)
