#!/usr/bin/python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()


@router.get('/app')
def obs_login():
    return {"msg": "登录成功,这是app模块"}