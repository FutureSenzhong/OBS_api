#!/usr/bin/python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()


@router.get('/dev')
def obs_login():
    return {"msg": "登录成功,这是设备模块"}