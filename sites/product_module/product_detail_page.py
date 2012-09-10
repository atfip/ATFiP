#!/usr/bin/env python
#coding=utf-8

import global_vars
from selenium.webdriver.support.ui import Select
from lib.utils_lib import dropbox_select_by_value


# ------ ui object definition section ------ #
# 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
def _edt_prodcut_name():
    """返回 login 页面中输入用户名的 editbox.
    
    Args:
        None.
        
    Returns:
        返回一个 webelement 对象
    
    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.   
    """
    return global_vars.browser.find_element_by_name('name')

def _edt_product_alias():
    """返回 login 页面中输入用户密码的 editbox.
    
    Args:
        None.
        
    Returns:
        返回一个 webdelement 对象

    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.
    """
    return global_vars.browser.find_element_by_name('code')

def _dropbox_product_owner():
    """返回 login 页面中点击完成登录的 button.
    
    Args:
        None.
        
    Returns:
        返回一个 webdelement 对象

    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.
    """
    product_owner_list = Select(global_vars.browser.find_element_by_id('PO'))
    return product_owner_list

def _dropbox_test_owner():
    """返回 login 页面中的赞助商信息.
    
    Args:
        None.
        
    Returns:
        返回一个 webdelement 对象

    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.
    """
    test_owner_list = Select(global_vars.browser.find_element_by_id("QM"))
    return test_owner_list

def _dropbox_release_owner():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    rel_owner_list = Select(global_vars.browser.find_element_by_id("RM"))
    return rel_owner_list

def _edt_product_desc():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    pass

def _btn_save_product():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    return global_vars.browser.find_element_by_id("submit")
    
def _radio_access_control():
    return global_vars.browser.find_elements_by_name("acl")
    
# ------ page function definition section ------ #
# 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
# 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
# 不负责启动关闭浏览器实例
def set_access_control_by_value(acl_value):
    """实现具体的登录操作，包括输入用户名、密码，以及确认登录.
    
    Args:
        account: key-value 结构的数据对象，存放用户名和密码信息.
        
    Returns:
        None.

    Raises:
        None.
    """
    for radio in _radio_access_control():
        if radio.get_attribute("value") == acl_value:
            radio.click()
    

def fill_all_items_by(product):
    _edt_prodcut_name().send_keys(product.product_name)
    _edt_product_alias().send_keys(product.product_alias)
    dropbox_select_by_value(_dropbox_product_owner(), product.product_owner)
    dropbox_select_by_value(_dropbox_test_owner(), product.test_owner)
    set_access_control_by_value(product.access_limit)


def save_product():
    _btn_save_product().click()
