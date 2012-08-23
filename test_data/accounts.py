#!/usr/bin/env python
#coding=utf-8


#~ 定义测试数据
class Account(object):
    """ test data """
    
    def __init__ (self):
        """ Class initialiser """
        self.username = "" 
        self.password = ""

        
super_usr = Account()
super_usr.username = "admin"
super_usr.password = "admin"


dev_usr = Account()
dev_usr.username = "dev"
dev_usr.password = "dev_password"


test_usr = Account()
test_usr.username = "tester"
test_usr.password = "test_password"

if __name__ == "__main__":
    print super_usr.username, super_usr.password
