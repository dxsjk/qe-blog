# -*- coding: utf-8 -*-
"""
文件：myblog/models/article.py
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
from routes import db, ma
from marshmallow import post_dump
from datetime import datetime
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from typing import List, Dict


class Article(db.Model):
    __tablename__ = 'article'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    __content: Mapped[bytes] = mapped_column(BLOB, name='content', nullable=False)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now(), onupdate=func.now())


    @property
    def content(self):
        return self.__content.decode('utf-8')

    @content.setter
    def content(self, content: str):
        self.__content = content.encode('utf-8')


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article

    @post_dump
    def decode_content(self, data, **kwargs):
        if isinstance(data, list):
            for item in data:
                item['content'] = item['_Article__content']
                del item['_Article__content']
        else:
            data['content'] = data['_Article__content']
            del data['_Article__content']
        return data


def handle_articles(article: Article,
                    many: bool = False
                    ) -> List[Dict[str, str]]:
    article_schema = ArticleSchema(many=many)
    return article_schema.dump(article)
