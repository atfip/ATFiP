#!/usr/bin/env python
#coding=utf-8

# ---------------------------------------------------------------------
# [general config info]
base_url = "http://192.168.56.102/zentaopms/www"
"""base URL 通常为进入系统的最初入口"""

debug_mode = True
"""是否需要打印测试执行过程中的调试信息，缺省值为 False，通常仅用于框架自身的调试。"""



# ---------------------------------------------------------------------
# [浏览器相关的配置信息]
# 浏览器类型的作用顺序为：
# 	final_browser_tyep: 全局影响，在 Test Runner 中设定，对当次运行的所有 test case 产生影响
# 	browser_type: 局部影响，在 Test Suite 中设定，对某个 suite 中的所有 test case 产生影响
# 	defualt: 如果上述两项均未设定，则 Windows 缺省使用 IE，其他系统缺省使用 Firefox 为每个 
#			Test Case 执行所用的浏览器
browser_type = ""
"""定义测试所需使用的浏览器类型，如果在这里没有指定，可以在定义 test suite 的时候为每个test suite 指定
	IE for internet explore
	Chrome for Chrome
	Firefox for Firefox
"""
final_browser_tyep = ""
"""浏览器类型的全局控制，如果未设定，通常由 test runner 执行前设定覆盖 browser_type 中的设置，全局生效
	IE for internet explore
	Chrome for Chrome
	Firefox for Firefox
"""
# example for windows
ie_path = "c:\\ATFiP\\lib\\IEDriverServer_32.exe"
"""set browser driver path for IE"""

# example for linux
# chrome_path = "/home/jackei/ATFiP/lib/chromedriver"
# """set browser driver path for Chrome"""

# example for windows
# chrome_path = "c:\\ATFiP\\lib\\chromedriver.exe"
# """set browser driver path for Chrome"""



# ---------------------------------------------------------------------
# [测试结果与测试报告管理相关的配置信息]
# 该项由用户设定，windows 下需要注意 \\ 转义字符的使用
test_result_base_dir = "c:\\ATFiP\\report\\"

# example for linux
# test_result_base_dir = "/home/jackei/report/"

report_dir = ''
"""预留的参数，在执行测试时由程序自动填充。"""

video_dir = ''
"""预留的参数，在执行测试时由程序自动填充。"""

report_server_name = "localhost"
"""如果需要对外提供基于网络访问 report 的功能，则需要启动 HTTP server，并设置该项。"""

report_server_port = "80"
"""如果需要对外提供基于网络访问 report 的功能，则需要启动 HTTP server，并设置该项。"""

rec_service_port = 5900
"""设置视频录制服务的端口, 绝大多数VNC Server 的默认端口均为5900."""



# ---------------------------------------------------------------------
# [如果需要在执行测试后通过 email 方式发送邮件，则需要配置如下选项。]
email_sender = "sender@hostname.com"
email_reciver = "reciver@hostname.com"
smtp_server_name = "mail.hostname.com.cn"
smtp_server_port = "25"
smtp_username = "sender_user_name"
smtp_password = "sender_password"