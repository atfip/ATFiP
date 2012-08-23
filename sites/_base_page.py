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
        return self.browser.current_url
        
    @property
    def title(self):
        return self.browser.title
    
    @property
    def source_code(self):
        return self.browser.page_source
        
    @property
    def loaded(self):
        pass
        
    def refresh(self):
        self.browser.refresh
        
        
if __name__ == "__main__":
    from selenium import webdriver
    bb = webdriver.Firefox()
    b = BasePage(bb)
    b.go()
    print b.url
    print b.title
    print b.source_code
    
