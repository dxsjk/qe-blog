# -*- coding: utf-8 -*-
"""
文件：myblog/routes/cal_routes.py
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
from form.cal_form import CalForm
from form.Integral import IntegralForm
from cal.solve import solve_latex
from utils.Result import Result

import ast
from sympy import integrate,Integral,latex


def convert_to_tuple(input_str: str):
    input_str = input_str.replace('（', '(').replace('）', ')').replace('，', ',')
    return ast.literal_eval(input_str)


@app.route('/cal/solve', methods=['POST'])
def cal_solve():
    cal_form = CalForm()
    if cal_form.validate_on_submit():
        latex = cal_form.latex.data
        result = solve_latex(latex)

        return Result.success(data=result)
    return '参数错误', 400


@app.route('/math/integral', methods=['POST'])
def make_integral():
    integral_form = IntegralForm()
    if integral_form.validate_on_submit():
        params = integral_form.params.data
        realm = integral_form.realm.data
        expression = integral_form.expression.data
        if realm:
            realm = convert_to_tuple(realm)
        else:
            expression_latex = latex(Integral(expression))
            result = latex(integrate(expression, params))
            res=[result,expression_latex]
            return Result.success(data=res)
    return '参数错误', 400
