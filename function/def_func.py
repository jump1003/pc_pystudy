#!usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def quadratic(a, b, c):
	if not isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
		raise TypeError("Error-0:参数数据类型错误！")
	elif a == 0:
		if b == 0:
			raise TypeError("Error-1:参数a,b不能全为0！")
		else:
			x1 = x2 = -b / c
	elif (b ** 2 - 4 * a * c) < 0:
		raise TypeError("Error-2:该方程无解！")
	else:
		x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
		x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
	return x1, x2


# print('输入参数求解一元二次方程：ax^2 + bx + c = 0\n')
# l=input('请设置参数a的数值：')
# m=input('请设置参数b的数值：')
# n=input('请设置参数c的数值：')
# print('该方程的解为：\n(x1,x2) = (%.2f, %.2f)'%quadratic(0,0,-4))
def my_abs(x):
	if not isinstance(x, (int, float)) and isinstance(y, (int, float)):
		raise TypeError('error 0')
	if x > 0:
		return x
	else:
		return -x
