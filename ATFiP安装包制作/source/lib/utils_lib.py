#!/usr/bin/env python
#coding=utf-8


import os
import platform
import time
import urllib2
import castro
from selenium import webdriver

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config
import global_vars
from lib.HTMLTestRunner2 import HTMLTestRunner


def start_browser():
    """统一封装启动浏览器的方法，根据配置文件中定义的浏览器类型，启动不同的浏览器实例
    Args: None
    return: browser object
    raise: None
    """
    if (not config.final_browser_tyep == ''):
        start_browser_by_config(config.final_browser_tyep)
    else:
        start_browser_by_config(config.browser_type)


def start_browser_by_config(browser_type=None):
    """根据配置信息启动浏览器，如果配置文件中未指定浏览器类型，则判断操作系统是否为 Windows。
    如果为 Windows，缺省启动 IE，否则缺省启动 Firefox。
    Args: 
        browser_type: 浏览器类型，IE/Firefox/Chrome
    return: None. 创建 global_vars.browser 对 browser 对象的引用
    raise: None.
    """
    # os_type = get_os_type()
    if (browser_type == 'IE'):
        browser = webdriver.Ie(config.ie_path)
    elif (browser_type == 'Chrome'):
        browser = webdriver.Chrome(config.chrome_path)
    elif (browser_type == 'Firefox'):
        browser = webdriver.Firefox()
    elif platform.architecture()[1] == "WindowsPE":
        browser = webdriver.Ie(config.ie_path)
    else:
        browser = webdriver.Firefox()

    browser.implicitly_wait(10)
    browser.maximize_window()
    global_vars.browser = browser

    # if (browser_type == 'IE'):
    #     if (os_type[1] == 'WindowsPE'):
    #         if (os_type[0] == '32bit'):
    #             browser = webdriver.Ie(config.ie_path_32bit)
    #         elif (os_type[0] == '64bit'):
    #             browser = webdriver.Ie(config.ie_path_64bit)
    #         else:
    #             print u"缺少所支持的浏览器版本."
    #     else:
    #         print u"IE浏览器仅支持运行在 Windows 操作系统上。"

    # elif (browser_type == 'Chrome'):
    #     browser = webdriver.Chrome(config.chrome_path)

    # elif (browser_type == 'Firefox'):
    #     browser = webdriver.Firefox()

    # else:
    #     browser = webdriver.Firefox()

    # browser.implicitly_wait(10)
    # browser.maximize_window()
    # global_vars.browser = browser


def stop_browser():
    """quit global browser process.
    Args: None
    Return: None
    Raise: None
    """
    global_vars.browser.quit()


def run_test(test_suite, test_suite_name, rec=False):
    """执行所有给定的 test suite/test case，并生成和通过邮件发送测试报告。
    Args: 
        test_suite: 需要执行的所有 test case 的集合
        test_suite_name: 上述 test_stuie 的 name 信息
        rec: Boolean。True=录制 case 执行过程中的屏幕录像; False=不录制
    return: None.
    raise: None.
    """
    set_report_path(test_suite, test_suite_name)
    print_debug_info("ready...")
    with open(os.path.join(config.report_dir, "summary_report.html"), "wb") as f:
        print_debug_info("report_file is: " + os.path.join(config.report_dir, "summary_report.html"))
        print_debug_info("create test runner")
        runner = HTMLTestRunner(
                    stream=f,
                    verbosity=2,
                    title="Test Suite: " + test_suite_name,
                    description=''
                    )
        print_debug_info("ready for run...")
        runner.run(test_suite)
    send_report_after_ran_test()


def set_report_path(test_suite, test_suite_name):
    """1. 在执行测试前，创建和设定测试报告/录像的存储位置。目前缺省按照 test_suite_name + time_stamp 
        的方式来分别存放每次执行的结果，录像文件则存放在 report/video 目录下。
        2. 设定 castro.DATA_DIR 
    Args:
        test_suite:
        test_suite_name:
    Return: None.
    Raise: None.
    """
    time_stamp = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    config.report_dir = os.path.join(config.test_result_base_dir, \
        (test_suite_name + '_' + time_stamp))
    config.video_dir = os.path.join(config.report_dir, 'video')
    print_debug_info("config.report_dir is: " + config.report_dir)
    print_debug_info("config.video_dir is: " + config.video_dir)

    if not os.path.exists(config.video_dir):
        print_debug_info("starting create video_dir")
        os.makedirs(config.video_dir)
        print_debug_info("created video_dir")

    castro.DATA_DIR = config.video_dir


def send_report_after_ran_test():
    """根据 config 中的配置信息，在完成测试后通过邮件方式发送 HTML 格式报告给相关人
    Args: None.
    return: None.
    raise: None.
    """
    msg = MIMEMultipart()
    msg['subject'] = u"软件测试报告"
    msg['from'] = config.email_sender
    msg['to'] = config.email_reciver

    url = "http://" + config.report_server_name + ":" + config.report_server_port + "/report/" \
        + os.path.split(config.report_dir)[1] + '/summary_report.html'
    print_debug_info("the report's url is: " + url)

    report_content = MIMEText(urllib2.urlopen(url).read().decode('utf-8'), 'html')
    msg.attach(report_content)
    print_debug_info("report attached.")

    try:
        smtp = SMTP()
        smtp.connect(config.smtp_server_name, config.smtp_server_port)
        smtp.login(config.smtp_username, config.smtp_password)
        smtp.sendmail(config.email_sender, config.email_reciver, \
            msg.as_string())
        print_debug_info("report has already sent.")
        smtp.quit()
    except Exception, e:
        raise e


def create_recorder(test_method_name):
    try:
        print_debug_info("set rec_file_name value.")
        rec_file_name = test_method_name + '.swf'
        print_debug_info("create recorder.")
        recorder = castro.Castro(filename=rec_file_name, port=config.rec_service_port)
        print_debug_info("recorder created...")
        return recorder
    except Exception, e:
        print e


def start_record(recorder):
    try:
        time.sleep(2)
        recorder.start()
        print_debug_info("record started.")
    except Exception, e:
        print e


def stop_record(recorder):
    try:
        time.sleep(2)
        recorder.stop()
        print_debug_info("record stopped.")
    except Exception, e:
        raise e


def print_debug_info(info):
    if config.debug_mode:
        print info


def dropbox_select_by_value(select_object, text):
    """ select and change current project/product/other. just only for Zentao.
    args: 
        select_object: selenium Select 对象实例, 一个包含一到多个选项的下拉列表
        text: 根据 text 值来选定某个具体的选项
    return: None
    raise: NoSuchObjectException.
    """
    visible_text = ""
    for i in select_object.options:
        if text in i.text:
            visible_text = i.text
    select_object.select_by_visible_text(visible_text)


def get_object_name(obj, namespace):
    """return name of the special object - varible or method"""
    names = [name for name in namespace if namespace[name] is obj]
    return names[0]


def get_os_type():
    """get current computer's os type
    Args: None
    return: a tuple. ("32bit/64bit", "WindowsPE for windows/ELF for linux")
    raise: None.
    """
    return platform.architecture()


if __name__ == '__main__':
    # config.final_browser_tyep = 'IE'
    start_browser()
