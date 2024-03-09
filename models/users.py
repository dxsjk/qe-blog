# -*- coding: utf-8 -*-
"""
文件：myblog/models/users.py
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
from routes import db, ma, login_manager
from flask_login import UserMixin
from marshmallow import post_dump
from datetime import datetime
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from typing import List, Dict
from utils.pwd import check_password,set_password


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(162), nullable=False)
    full_name: Mapped[str] = mapped_column(String(32), nullable=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)


    def password_true(self, password):
        hash_password = set_password(password)
        return check_password(password, hash_password)