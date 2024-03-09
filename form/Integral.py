# -*- coding: utf-8 -*-
"""
文件：myblog/form/Integral.py
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
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectMultipleField
from wtforms.validators import DataRequired


class IntegralForm(FlaskForm):
    class Meta:
        csrf = False  # 关闭 CSRF 校验

    params = SelectMultipleField('参数', choices=[('x', 'x'), ('y', 'y'), ('z', 'z')])
    realm = StringField('范围')
    expression = StringField('表达式', validators=[DataRequired()])
