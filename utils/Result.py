# -*- coding: utf-8 -*-
"""
文件：myblog//Result.py
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
import json

class Result:
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data
    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }
    @staticmethod
    def success(data=None, message='操作成功'):
        return Result(0, message, data).to_dict()

    @staticmethod
    def error(message:str):
        return Result(1, message, None).to_dict()
