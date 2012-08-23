#!/usr/bin/env python
#coding=utf-8

from base_page import BasePage
from selenium.webdriver.support.ui import Select
from lib.utils_lib import dropbox_select_by_value

class ProductDetailPage(BasePage):

    def __init__(self, browser):
        BasePage.__init__(self, browser)
        page_path = "index.php?m=user&f=login"
        self.url = self.base_url + page_path
            
    # ------ ui object definition section ------ #
    # 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
    @property
    def edt_prodcut_name(self):
        """返回 login 页面中输入用户名的 editbox.
        
        Args:
            None.
            
        Returns:
            返回一个 webelement 对象
        
        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.   
        """
        return self.browser.find_element_by_name('name')

    @property
    def edt_product_alias(self):
        """返回 login 页面中输入用户密码的 editbox.
        
        Args:
            None.
            
        Returns:
            返回一个 webdelement 对象

        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.
        """
        return self.browser.find_element_by_name('code')

    @property
    def list_product_owner(self):
        """返回 login 页面中点击完成登录的 button.
        
        Args:
            None.
            
        Returns:
            返回一个 webdelement 对象

        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.
        """
        product_owner_list = Select(self.browser.find_element_by_id('PO'))
        return product_owner_list

    @property
    def list_test_owner(self):
        """返回 login 页面中的赞助商信息.
        
        Args:
            None.
            
        Returns:
            返回一个 webdelement 对象

        Raises:
            NoSuchWebEelement exception: 无法找到指定的页面对象.
        """
        test_owner_list = Select(self.browser.find_element_by_id("QM"))
        return test_owner_list
    
    @property
    def list_rel_owner(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        rel_owner_list = Select(self.browser.find_element_by_id("RM"))
        return rel_owner_list

    @property
    def edt_product_des(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        pass
    
    @property
    def btn_save_product(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        return self.browser.find_element_by_id("submit")
        
    @property
    def radios_acl(self):
        return self.browser.find_elements_by_name("acl")
        
    # ------ page function definition section ------ #
    # 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
    # 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
    # 不负责启动关闭浏览器实例
    def set_access_control_by_value(self, acl_value):
        """实现具体的登录操作，包括输入用户名、密码，以及确认登录.
        
        Args:
            account: key-value 结构的数据对象，存放用户名和密码信息.
            
        Returns:
            None.

        Raises:
            None.
        """
        for radio in self.radios_acl:
            if radio.get_attribute("value") == acl_value:
                radio.click()
        

    def fill_all_items(self, product):
        self.edt_prodcut_name.send_keys(product.product_name)
        self.edt_product_alias.send_keys(product.product_alias)
        dropbox_select_by_value(self.list_product_owner, product.product_owner)
        dropbox_select_by_value(self.list_test_owner, product.test_owner)
        self.set_access_control_by_value(product.access_limit)


    def save_product(self):
        self.btn_save_product.click()
