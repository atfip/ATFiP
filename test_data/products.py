#!/usr/bin/env python
#coding=utf-8

from accounts import super_usr, dev_usr, test_usr
#~ 定义测试数据
class Product(object):
    """ test data """
    
    def __init__ (self):
        """ Class initialiser """
        self.product_name = "" 
        self.product_alias = ""
        self.product_owner = ""
        self.test_owner = ""
        self.release_owner = ""
        self.product_desc = ""
        self.access_limit = ""


normal_product = Product()
normal_product.product_name = "test_name"
normal_product.product_alias = "test_alias"
normal_product.product_owner = super_usr.username
normal_product.test_owner = test_usr.username
normal_product.release_owner = dev_usr.username
#~ normal_product.product_desc = "afaflasljfajqowiuonlanlj&(&(69823hkh*&%#:K:<@?>#<$"
normal_product.access_limit = "open"
