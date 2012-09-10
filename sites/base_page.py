#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append("..")
import config

class BasePage(object):
    """所有 page object 的基类，实现所有页面共性的方法。"""
    
    def __init__(self, browser):
        self.browser = browser
        self.base_url = config.base_url
        self.page_path = "/"
        self.url = self.base_url + self.page_path
    
    #~ def go(self):
        #~ self.browser.get(self.url)
        
    @property
    def current_url(self):
        """返回当前页面的 url 地址.
        
        Args:
            None.
            
        Returns:
            一个 string 对象，包含当前页面的 title 信息
        
        Raises:
            None.
        """
        return self.browser.current_url
        
    @property
    def title(self):
        """返回当前页面的 title 值.
        
        Args:
            None.
            
        Returns:
            一个 string 对象，包含当前页面的 title 信息
        
        Raises:
            None.   
        """
        return self.browser.title
    
    @property
    def source_code(self):
        """返回当前页面的源代码。
        
        Args:
            None.
            
        Returns:
            String 对象，包含当前页面的源代码。
        
        Raises:
            None.   
        """
        return self.browser.page_source
        
    @property
    def loaded(self):
        """验证当前页面是否正确加载.
        
        Args:
            None.
            
        Returns:
            None.
        
        Raises:
            Exception exception: xxx页面加载失败.   
        """
        pass
        
    def refresh(self):
        """刷新当前页面. 通常与 page.loaded 方法同时使用。
        
        Args:
            None.
            
        Returns:
            None.
        
        Raises:
            None.   
        """
        self.browser.refresh
        
        
if __name__ == "__main__":
    from selenium import webdriver
    bb = webdriver.Firefox()
    b = BasePage(bb)
    b.go()
    print b.url
    print b.title
    print b.source_code
    
