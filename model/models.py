# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-31 9:42:19
# 
# Project: model
# File: models.py
# Description: 
# 
'''

from sqlalchemy import Column, Integer, SmallInteger, String, Time, Text, Table, Float, ForeignKey
from sqlalchemy.orm import relationship

from model.base import Base


association_table = Table('association', Base.metadata,
    Column('model_id', Integer, ForeignKey('models.id')),
    Column('material_id', Integer, ForeignKey('material.id'))
)

class Model(Base):
    '''模型训练任务表
    '''
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    traintype = Column(SmallInteger, comment="模型训练类型,新增模型、优化模型")
    status = Column(SmallInteger, comment="模型状态,待训练，训练失败，训练完成")
    savemodel = Column(Text, comment="模型存储路径")
    # 训练结果
    precision = Column(Float, comment="准确率,百分比")
    high_reliability = Column(Text, comment="高可信图片存储路径")
    low_reliability = Column(Text, comment="低可信图片存储路径")
    # 模型和训练素材多对多关系
    matreial = relationship(
        "Material",
        secondary=association_table,
        back_populates="model")



class Material(Base):
    '''训练素材表
    '''
    __tablename__ = "material"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(50), comment="名称")
    path = Column(Text, comment="素材图片存储路径")
    createtime = Column(Time, comment="录入时间")
    # 模型和训练素材多对多关系
    model = relationship(
        "Model",
        secondary=association_table,
        back_populates="matreial")

