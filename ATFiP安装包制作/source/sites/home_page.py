#!/usr/bin/env python
#coding=utf-8

import global_vars
import config
from lib import utils_lib
# ------ ui object definition section ------ #
# 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
def _edt_search_box():
    """返回"首页"tab 页的 link 地址.
    
    Args:
        None.
        
    Returns:
        返回一个 webelement 对象
    
    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.   
    """
    return global_vars.browser.find_element_by_id("kw")

def _btn_search_button():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    return global_vars.browser.find_element_by_id("su")

# ------ page function definition section ------ #
# 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
# 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
# 不负责启动关闭浏览器实例
def search_by_keyword(keyword):
    """确认是否登录成功.    
    Args:None.
    Returns:None.
    Raises:None.
    """
    _edt_search_box().send_keys(keyword)
    _btn_search_button().click()
        
def goto():
    print config.base_url
    global_vars.browser.get(config.base_url)

if __name__ == '__main__':
    utils_lib.start_browser()
    goto()
    keyword = "auto test frameword in python."
    search_by_keyword(keyword)