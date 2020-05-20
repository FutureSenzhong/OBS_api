# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-25 2:21:35
# 
# Project: FastAPI-Project-Template
# File: main.py
# Description: 
# 
'''
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from settings.config import Config
from model.user import User
from model.database import Database
from applications import account_manage, app_manage, content_manage, device_manage, organization_manage


app = FastAPI()

conf = Config()
conf.parse("settings/config.ini")
db = Database(conf.mysqldb)

app.include_router(account_manage.router, prefix="/api/obs",)
app.include_router(app_manage.router, prefix="/api/obs",)
app.include_router(content_manage.router, prefix="/api/obs",)
app.include_router(device_manage.router, prefix="/api/obs",)
app.include_router(organization_manage.router, prefix="/api/obs",)


app.mount("/static", StaticFiles(directory="static"), name="static")


class ModelUser(BaseModel):
    name: str
    passwd: str
    email: str
    usertype: str
    organization: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/login")
def login(username: str, passwd: str):
    record = db.session.query(User).filter_by(name=username).first()
    print(record)
    if not record:
        return {"result": "用户不存在"}
    return {"token": "xxxxxxx"}


@app.post("/user/add")
def add_user(user: ModelUser):
    return {"user": ModelUser}


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1",port=8000)