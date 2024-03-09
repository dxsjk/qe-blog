# -*- coding: utf-8 -*-
"""
文件：myblog/routes/image_routes.py
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
from flask import jsonify, send_from_directory
from flask_login import login_required
from form.image_upload_form import ImageUploadForm
from models.article import Article
from utils.Result import Result
from utils.path import FilePath
from werkzeug.utils import secure_filename
from services.image_service import ImageService


@app.route('/image/upload', methods=['POST'])
@login_required
def image_upload():
    image_form = ImageUploadForm()
    if image_form.validate_on_submit():
        image_file = image_form.file.data
        image_name = image_form.name.data
        image_path, hash_list = FilePath.get_image_path()
        file_hash = FilePath.calculate_hash(image_file)
        if file_hash in hash_list:
            result = Result.error('图片已存在')
            return jsonify(result), 400
        hash_list.append(file_hash)
        # 生成安全的文件名
        image_filename = secure_filename(image_file.filename)
        # 保存图片
        try:
            image_file.save(image_path.joinpath(image_filename))
            with open(FilePath.get_hash_path(), 'w') as f:
                f.write('\n'.join(hash_list))
        except Exception as e:
            result = Result.error('保存图片失败')
            return jsonify(result), 500
        # 返回结果
        result = Result.success(message='图片上传成功')
        return jsonify(result)
    return jsonify(Result.error('参数错误')), 400


@app.route('/image/<image_name>', methods=['GET'])
def image(image_name):
    image_path, _ = FilePath.get_image_path()
    image = image_path.joinpath(image_name)
    if image.exists():
        return send_from_directory(image_path, image_name)
    else:
        result = Result.error('图片不存在')
        return jsonify(result), 404


@app.route('/image/list', methods=['GET'])
@login_required
def image_list():
    images_path, images_name = ImageService.get_image_list()
    res = {
        'images_name': images_name,
        'images_path': images_path
    }
    result = Result.success(data=res)
    return jsonify(result)
