# -*- coding: utf-8 -*-
"""
文件：myblog/cal/solve.py
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
from latex2sympy2 import latex2sympy, latex2latex
from sympy import integrate
def solve_latex(latex_str):
    return latex2latex(latex_str)
def solve_integral(expression, realm):
    integrate()

