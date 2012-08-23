#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append("..")
import config
from selenium import webdriver


# 统一封装启动浏览器的方法，根据配置文件中定义的浏览器类型，启动不同的浏览器实例
def start_browser():
    if (config.final_browser_tyep == 'IE'):
        browser = webdriver.Ie()
    elif (config.final_browser_tyep == 'Chrome'):
        browser = webdriver.Chrome(config.chrome_path)
    elif (config.final_browser_tyep == 'Firefox'):
        browser = webdriver.Firefox()
    elif (config.browser_type == 'IE'):
        browser = webdriver.Ie()
    elif (config.browser_type == 'Chrome'):
        browser = webdriver.Chrome(config.chrome_path)
    elif (config.browser_type == 'Firefox'):
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Firefox()

    browser.implicitly_wait(10)

    return browser


def dropbox_select_by_value(select_object, text):
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    visible_text = ""
    for i in select_object.options:
        if text in i.text:
            visible_text = i.text
            
    select_object.select_by_visible_text(visible_text)
