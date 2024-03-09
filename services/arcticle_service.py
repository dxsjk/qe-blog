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
from models.article import Article, handle_articles
from routes import db
from sqlalchemy import Select
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from typing import Union, Dict, List


class ArticleService:
    @staticmethod
    def get_article(article_id) -> Union[List[Dict[str, str]], None]:
        """
        get one article by article_id
        :param article_id:
        :return:
        """
        article = db.session.get(Article, article_id)
        if article:
            return handle_articles(article)
        else:
            return None

    @staticmethod
    def get_articles() -> Union[List[Dict[str, str]], None]:
        articles = db.session.query(Article).all()
        if articles:
            return handle_articles(articles, many=True)

    @staticmethod
    def insert_article(article: Article) -> bool:
        result = db.session.query(Article).filter(Article.title == article.title).first()
        if result:
            return False, '文章标题重复'
        else:
            try:
                db.session.add(article)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                return False, '文章标题重复'
            else:
                return True, '发布成功'

    @staticmethod
    def update_article(article: Article) -> bool:
        result = db.session.query(Article).filter(Article.id == article.id).first()
        if result is None:
            return False, '文章不存在'
        else:
            try:
                existing_article = db.session.query(Article).filter(Article.title == article.title,
                                                                    Article.id != article.id).first()
                if existing_article:
                    return False, '文章标题重复'
                result.title = article.title
                result.content = article.content
                result.update_time = func.now()
            except Exception as e:
                db.session.rollback()
                return False, f'更新 {article.title} 失败'
            else:
                db.session.commit()
                return True, f'更新 {article.title} 成功'
    @staticmethod
    def delete_article(article_id: int) -> bool:
        result = db.session.query(Article).filter(Article.id == article_id).first() # type: Article
        if result is None:
            return False, '文章不存在'
        else:
            try:
                db.session.delete(result)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return False, f'删除 {result.title} 失败'
            else:
                return True, f'删除 {result.title} 成功'
