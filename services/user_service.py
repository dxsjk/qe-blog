# -*- coding: utf-8 -*-
"""
文件：myblog/services/user_service.py
创建者：QE
诗：
    鲸鱼安慰了大海
            - 燕七
    不是所有的树
    都能在自己的家乡终老
    不是所有的轨道
    都通往春暖花开的方向
    不是所有的花都会盛开
    不是所有约定的人都会到来
    我知道，是流星赞美了黑夜
    鲸鱼安慰了大海
"""
# -*- coding: utf-8 -*-
"""
文件：myblog/services/arcticle_service.py
创建者：QE
诗：
    鲸鱼安慰了大海
            - 燕七
    不是所有的树
    都能在自己的家乡终老
    不是所有的轨道
    都通往春暖花开的方向
    不是所有的花都会盛开
    不是所有约定的人都会到来
    我知道，是流星赞美了黑夜
    鲸鱼安慰了大海
"""
from models.users import Users
from flask import session
from flask_login import login_user
from routes import db
from typing import Union,Dict,List


class UserService:
    @staticmethod
    def login(username, password) -> Union[List[Dict[str, str]], None]:
        user = db.session.query(Users).filter(Users.username == username).first()
        if user and user.password_true(password):
            login_user(user)
            return True
        else:
            return False

