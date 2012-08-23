#!/usr/bin/env python
#coding=utf-8

from _base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, browser):
        BasePage.__init__(self, browser)
        self.page_path = "/index.php?m=user&f=login"
        self.url = self.base_url + self.page_path
            
    # ------ ui object definition section ------ #
    # 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
    @property
    def _edtUsername(self):
        """返回 login 页面中输入用户名的 editbox.
        
        Args:
            None.
            
        Returns:
            返回一个 webelement 对象
        
        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.   
        """
        return self.browser.find_element_by_name('account')

    @property
    def _edtPassword(self):
        """返回 login 页面中输入用户密码的 editbox.
        
        Args:
            None.
            
        Returns:
            返回一个 webdelement 对象

        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.
        """
        return self.browser.find_element_by_name('password')

    @property
    def _loginButton(self):
        """返回 login 页面中点击完成登录的 button.
        
        Args:
            None.
            
        Returns:
            返回一个 webdelement 对象

        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.
        """
        return self.browser.find_element_by_id('submit')

    @property
    def _sponsorsName(self):
        """返回 login 页面中的赞助商信息.
        
        Args:
            None.
            
        Returns:
            返回一个 webdelement 对象

        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.
        """
        sponsorsName = u'以太科技赞助'
        return self.browser.find_element_by_link_text(sponsorsName).text
    
    @property
    def _loaded(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        if self.page_path in self.url:
            return 1
        else:
            raise "the page load failed."
    # ------ page function definition section ------ #
    # 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
    # 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
    # 不负责启动关闭浏览器实例
    def do_login_as(self, account):
        """实现具体的登录操作，包括输入用户名、密码，以及确认登录.
        
        Args:
            account: 存放用户名和密码信息.
            
        Returns:
            None.

        Raises:
            None.
        """
        self.browser.get(self.url)
        self._edtUsername.send_keys(account.username)
        self._edtPassword.send_keys(account.password)
        self._loginButton.click()
        
        
    def checkSystemVersion(self):
        pass


    def checkSponsorsName(self):
        print sponsorsName

