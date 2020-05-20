# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-30 8:11:37
# 
# Project: model
# File: device.py
# Description: 
# 
'''

from sqlalchemy import Column, Integer, SmallInteger, String, Time, Text, ForeignKey
from sqlalchemy.orm import relationship
from model.base import Base


class Device(Base):
    '''设备表
    '''
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    sn = Column(String(50), comment="设备sn码")
    desc = Column(Text, comment="设备描述")
    status = Column(SmallInteger, comment="设备状态,离线,活跃")
    createtime = Column(Time, comment="录入时间")
    edittime = Column(Time, comment="编辑时间")
    # 设备和APP是多对一的关系
    app_id = Column(Integer, ForeignKey('app.id'))
    app = relationship("APP", back_populates="device")
    # 设备和内容是一对多的关系
    content_id = Column(Integer, ForeignKey('contents.id'))
    content = relationship("Content", back_populates="device")


class Content(Base):
    '''内容管理表
    '''
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    createtime = Column(Time, comment="创建时间")
    edittime = Column(Time, comment="编辑时间")
    pic = Column(Text, comment="主图片路径")
    music = Column(Text, comment="音乐文件路径")
    desc = Column(Text, comment="内容描述")
    display = Column(Text, comment="展示版式")
    # 设备和内容是一对多的关系
    device = relationship("Device", back_populates="content")


class APP(Base):
    '''APP管理表
    '''
    __tablename__ = "app"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    createtime = Column(Time, comment="创建时间")
    edittime = Column(Time, comment="编辑时间")
    app_pic = Column(Text, comment="APP图片路径")
    desc = Column(Text, comment="说明")
    background = Column(SmallInteger, comment="背景类型")
    pic = Column(Text, comment="引导页图片路径")
    music = Column(Text, comment="音乐文件路径")
    video = Column(Text, comment="视频文件路径")
    # 设备和APP是多对一的关系
    device = relationship("Device", back_populates="app")