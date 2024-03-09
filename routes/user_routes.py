# -*- coding: utf-8 -*-
"""
文件：myblog/routes/user_routes.py
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
from routes import app
from form.login_form import LoginForm
from services.user_service import UserService
from flask import request, jsonify, session
from utils.Result import Result


@app.route('/user/login', methods=['POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        result = UserService.login(login_form.username.data, login_form.password.data)
        if result:
            dict_session = dict(session)
            return jsonify(Result.success(data=dict_session))
        else:
            return jsonify(Result.error('用户名或密码错误')), 400
    return jsonify(Result.error('参数错误')), 400


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify(Result.success('退出成功'))
