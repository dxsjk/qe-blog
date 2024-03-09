# -*- coding: utf-8 -*-
"""
文件：myblog/草稿/2.py
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
from sympy import symbols, integrate
import ast
def convert_to_tuple2(input_str: str):
    input_str = input_str.replace('（', '(').replace('）', ')').replace('，', ',').replace('x', '0')
    tuple_strs = input_str.split('),')
    tuple_strs = [s + ')' for s in tuple_strs[:-1]] + [tuple_strs[-1]]
    tuples = [ast.literal_eval(s) for s in tuple_strs]
    return [(x if x != 0 else 'x', y) for x, y in tuples]

def can_cal(params: list, expression: str, realm: str):
    x, y = symbols(' '.join(params))
    realm_tuples = convert_to_tuple2(realm)
    res = integrate(expression, (x, realm_tuples[0][0], realm_tuples[0][1]), (y, realm_tuples[1][0], realm_tuples[1][1]))
    return res

params = ["x", "y"]
expression = "xy"
realm = "（1，2），（1，x）"
result = can_cal(params, expression, realm)
print(result)
# def can_cal(params: list, expression: str,realm: str):
#     length = len(params)
#     if length == 1:
#         x = symbols(params[0])
#         params = convert_to_tuple(realm)
#         res=integrate(expression,(x,params[0],params[1]))
#         return res
#     elif length == 2:
#         x, y = symbols(' '.join(params))
#         res=integrate(expression,(x,params[0],params[1]),(y,params[2],params[3]))
#         return x, y
#     elif length == 3:
#         x, y, z = symbols(' '.join(params))
#         return x, y, z
# a=can_cal(["x", "y"], "（1，2），（1，x）", "xy")
# print(a)