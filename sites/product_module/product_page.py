#!/usr/bin/env python
#coding=utf-8

import global_vars
from selenium.webdriver.support.ui import Select
from lib.utils_lib import dropbox_select_by_value
# ------ ui object definition section ------ #
# 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
def _lnk_create_product():
    """ """
    return global_vars.browser.find_element_by_link_text(u"新增产品")

def _lnk_product_list():
    """"""
    return global_vars.browser.find_element_by_link_text(u"产品列表")

def _list_products():
    """ """
    product_list = Select(global_vars.browser.find_element_by_id("productID"))
    return product_list


# ------ page function definition section ------ #
# 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
# 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
# 不负责启动关闭浏览器实例
def change_product_by_name(product):
    """
    """
    dropbox_select_by_value(_list_products(), product.name)


def create_product():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    _lnk_create_product().click()


if __name__ == "__main__":
    pass