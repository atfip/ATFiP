#!/usr/bin/env python
#coding=utf-8

import global_vars
# ------ ui object definition section ------ #
# 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
def _lnk_home_page():
    """返回"首页"tab 页的 link 地址.
    
    Args:
        None.
        
    Returns:
        返回一个 webelement 对象
    
    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.   
    """
    return global_vars.browser.find_element_by_link_text(u"首页")

def _lnk_product_page():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    return global_vars.browser.find_element_by_link_text(u"产品视图")

# ------ page function definition section ------ #
# 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
# 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
# 不负责启动关闭浏览器实例
def comfirm_login_succeed(, account):
    """确认是否登录成功.
    
    Args:
        account: key-value 结构的数据对象，存放用户名和密码信息.
        
    Returns:
        None.

    Raises:
        None.
    """
    if _lnk_home_page():
        print "Login successed. ", "The username is: " + account.username, \
            ", and the password is: " + account.password
    else:
        raise Exception("login failed.")
        

def goto_product_page():
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    _lnk_product_page().click()
