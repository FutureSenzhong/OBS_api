# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-31 11:04:51
# 
# Project: settings
# File: config.py
# Description: 
# 
'''

import configparser


class Config:
    '''配置
    '''
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.mysqldb = ""
        self.redis = ""
    
    def parse(self, path):
        self.config.read(path)
        if "db" not in self.config.sections():
            raise ValueError("config file can not find db section")
        host = self.config.get("db", "host")
        port = self.config.get("db", "port")
        username = self.config.get("db", "username")
        passwd = self.config.get("db", "passwd")
        self.mysqldb = "mysql+pymysql://%s:%s@%s:%s/ovision"%(username,passwd,host,port)