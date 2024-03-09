# -*- coding: utf-8 -*-
"""
文件：myblog/utils/pwd.py
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
from werkzeug.security import generate_password_hash, check_password_hash


def set_password(password):
    password = generate_password_hash(password)
    return password


def check_password(password, pwhash):
    return check_password_hash(password=password, pwhash=pwhash)


