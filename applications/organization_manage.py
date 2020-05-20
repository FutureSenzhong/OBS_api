#!/usr/bin/python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()


@router.get('/org')
def obs_login():
    return {"msg": "登录成功,这是组织管理模块"}