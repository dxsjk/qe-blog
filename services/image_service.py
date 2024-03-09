# -*- coding: utf-8 -*-
"""
文件：myblog/services/image_service.py
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
from utils.path import FilePath


class ImageService:
    @staticmethod
    def get_image_list():
        path, _ = FilePath.get_image_path()
        pic_path=[f'/image/{p.name}' for p in path.iterdir()]
        pic_name=[p.name for p in path.iterdir()]
        return pic_path,pic_name
