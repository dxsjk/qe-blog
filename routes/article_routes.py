# -*- coding: utf-8 -*-
"""
文件：myblog/routes/article_routes.py
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
from flask import render_template, jsonify
from flask_login import login_required
from services.arcticle_service import ArticleService
from form.article_form import ArticleForm
from models.article import Article
from utils.Result import Result


@app.route('/article', methods=['GET'])
@login_required
def article_page():
    articles = ArticleService.get_articles()
    if articles:
        result = Result.success(articles)
        return jsonify(result)
    else:
        result = Result.error('服务异常')
        return jsonify(result), 404


@app.route('/list/article/<int:article_id>', methods=['GET'])
@login_required
def article(article_id):
    article = ArticleService.get_article(article_id)
    if article:
        result = Result.success(article)
        return jsonify(result)
    else:
        result = Result.error('没有这篇文章')
        return jsonify(result), 404


# 发布文章
@app.route('/add/article', methods=['POST'])
@login_required
def create_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article = Article()
        article.title =article_form.title.data
        article.content = article_form.content.data
        ok, message = ArticleService.insert_article(article)
        if ok:
            return jsonify(Result.success(message=message))
        else:
            return jsonify(Result.error(message)), 400
    return jsonify(Result.error('参数错误')), 400


# 编辑文章
@app.route('/edit/article/<int:article_id>', methods=['PUT'])
@login_required
def edit_article(article_id):
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article = Article()
        article.title = article_form.title.data
        article.content = article_form.content.data
        article.id=article_id
        ok, message = ArticleService.update_article(article)
        if ok:
            return jsonify(Result.success(message=message))
        else:
            return jsonify(Result.error(message)), 400
# 删除文章
@app.route('/del/article/<int:article_id>', methods=['DELETE'])
@login_required
def delete_article(article_id):
    ok, message = ArticleService.delete_article(article_id)
    if ok:
        return jsonify(Result.success(message=message))
    else:
        return jsonify(Result.error(message)), 400