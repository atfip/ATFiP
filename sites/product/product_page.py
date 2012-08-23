#!/usr/bin/env python
#coding=utf-8

from base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, browser):
        BasePage.__init__(self, browser)
        page_path = "index.php?m=product&f=browse"
        self.url = self.base_url + page_path
            
    # ------ ui object definition section ------ #
    # 每个 页面对象 通过定义一个个方法，完成对当前页面对象的获取和维护等操作
    @property
    def lnk_create_product(self):
        """ """
        return self.browser.find_element_by_link_text(u"新增产品")

    @property
    def lnk_product_list(self):
        """"""
        return self.browser.find_element_by_link_text(u"产品列表")

    @property
    def list_products(self):
        """ """
        product_list = Select(self.browser.find_element_by_id("productID"))
        return product_list


    # ------ page function definition section ------ #
    # 每个页面对象定义一个个方法，完成对当前页面内可以进行的各项操作的定义
    # 仅负责定义操作，不负责校验操作结果，也不负责完成具体跟 test case 相关的逻辑
    # 不负责启动关闭浏览器实例
    def change_product_by_name(self, product):
        """
        """
        
        product_name = [t for t in self.drp_product_list.options if product.name in t.text]
        self.drp_product_list.select_by_visiable_text(product_name[0].text)

    def create_product(self):
        """ Function doc
    
        @param PARAM: DESCRIPTION
        @return RETURN: DESCRIPTION
        """
        self.lnk_create_product.click()


if __name__ == "__main__":
    from login_page import LoginPage
    from home_page import HomePage
    import sys
    sys.path.append("..")
    from test_data import accounts, products
    from selenium import webdriver
    b = webdriver.Chrome("/home/jackei/chromedriver")
    b.get("http://192.168.56.101/zentaopms/www/")
    login = LoginPage(b)
    login.do_login_as(accounts.super_usr)
    
