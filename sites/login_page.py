#!/usr/bin/env python
#coding=utf-8
import config
import global_vars

# ------ ui object definition section ------ #
# 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
def _edtUsername():
    """返回 login 页面中输入用户名的 editbox.
    
    Args:
        None.
        
    Returns:
        返回一个 webelement 对象
    
    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.   
    """
    return global_vars.browser.find_element_by_name('account')

def _edtPassword():
    """返回 login 页面中输入用户密码的 editbox.
    
    Args:
        None.
        
    Returns:
        返回一个 webdelement 对象

    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.
    """
    return global_vars.browser.find_element_by_name('password')

def _btnLogin():
    """返回 login 页面中点击完成登录的 button.
    
    Args:
        None.
        
    Returns:
        返回一个 webdelement 对象

    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.
    """
    return global_vars.browser.find_element_by_id('submit')

def _sponsorsName():
    """返回 login 页面中的赞助商信息.
    
    Args:
        None.
        
    Returns:
        返回一个 webdelement 对象

    Raises:
        NoSuchWebEelement exception: 无法找到指定的页面对象.
    """
    sponsorsName = u'以太科技赞助'
    return global_vars.browser.find_element_by_link_text(sponsorsName).text
        
# ------ page function definition section ------ #
# 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
# 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
# 不负责启动关闭浏览器实例
def go():
    global_vars.browser.get(config.base_url)


def do_login_as(account):
    """实现具体的登录操作，包括输入用户名、密码，以及确认登录.
    
    Args:
        account: 存放用户名和密码信息.
        
    Returns:
        None.

    Raises:
        None.
    """
    _edtUsername().send_keys(account.username)
    _edtPassword().send_keys(account.password)
    _btnLogin().click()
    
    
def checkSystemVersion():
    pass


def checkSponsorsName():
    print sponsorsName
