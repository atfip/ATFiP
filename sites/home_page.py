#!/usr/bin/env python
#coding=utf-8

from base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self, browser):
        BasePage.__init__(self, browser)
        self.page_path = "index.php?m=my&f=index"
        self.url = self.base_url + self.page_path
        
    # ------ ui object definition section ------ #
    # 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
    @property
    def lnkHomePage(self):
        """返回"首页"tab 页的 link 地址.
        
        Args:
            None.
            
        Returns:
            返回一个 webelement 对象
        
        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.   
        """
        return self.browser.find_element_by_link_text(u"首页")

    @property
    def lnkProductPage(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        return self.browser.find_element_by_link_text(u"产品视图")
    # ------ page function definition section ------ #
    # 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
    # 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
    # 不负责启动关闭浏览器实例
    def comfirm_login_succeed(self, account):
        """确认是否登录成功.
        
        Args:
            account: key-value 结构的数据对象，存放用户名和密码信息.
            
        Returns:
            None.

        Raises:
            None.
        """
        if self.lnkHomePage:
            print "Login successed. ", "The username is: " + account.username, \
                ", and the password is: " + account.password
        else:
            raise Exception("login failed.")
            

    def loaded(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        if self.lnkHomePage:
            pass
        else:
            raise Exception("the page load failed.")

    def goto_product_page(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        self.lnkProductPage.click()
