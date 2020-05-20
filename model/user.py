# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-30 6:22:53
# 
# Project: model
# File: user.py
# Description: 
# 
'''

from sqlalchemy import Column, Integer, String, Time, Text, ForeignKey
from sqlalchemy.orm import relationship
from model.base import Base


class User(Base):
    '''用户表
    '''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    passwd = Column(String(32), comment="密码，MD5")
    email = Column(String(50), comment="邮件")
    usertype = Column(String(50), comment="账户类型,超级管理员，一级，二级")
    portrait = Column(Text, comment="头像图片路径")
    createtime = Column(Time, comment="创建时间")
    activetime = Column(Time, comment="活跃时间")
    # 用户和组织是多对一的关系
    org_id = Column(Integer, ForeignKey('org.id'))
    organization = relationship("Organization", back_populates="user")


class Organization(Base):
    '''组织表
    '''
    __tablename__ = "org"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    # 用户和组织是多对一的关系
    user = relationship("User", back_populates="organization")