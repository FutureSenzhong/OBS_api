# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-30 6:29:02
# 
# Project: model
# File: database.py
# Description: 
# 
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.models import *
from model.device import *
from model.user import *

class Database:
    '''数据库
    '''
    def __init__(self, schema):
        self.engine = create_engine(schema, echo=True, pool_size=10)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_table(self):
        '''创建表之前要先创建数据库：
        CREATE DATABASE IF NOT EXISTS ovision DEFAULT CHARACTER SET utf8 
        DEFAULT COLLATE utf8_general_ci;
        '''
        Base.metadata.create_all(self.engine)
    
    def drop_table(self):
        Base.metadata.drop_all(self.engine)

