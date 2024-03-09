# -*- coding: utf-8 -*-
"""
文件：myblog/utils/path.py
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
from pathlib import Path
from hashlib import sha256


class FilePath:
    __image_path = Path(__file__).parent.parent.joinpath('data/images')
    __hash_path = Path(__file__).parent.parent.joinpath('data/hash.txt')

    @staticmethod
    def get_image_path():
        path = FilePath.__image_path
        hash_path = FilePath.__hash_path
        hash_list= []
        if not path.exists():
            path.mkdir(parents=True)
        if not hash_path.exists():
            hash_path.touch()
        with open(hash_path, 'r') as f:
            hash_list = f.read().split('\n')
        return path, hash_list
    @staticmethod
    def get_hash_path():
        return FilePath.__hash_path

    @staticmethod
    def calculate_hash(file):
        hash_obj = sha256()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_obj.update(chunk)
        file.seek(0)
        return hash_obj.hexdigest()
