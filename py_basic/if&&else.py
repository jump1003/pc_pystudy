#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# h=float(input('身高（m）：'))
# w=float(input('体重(kg)：'))
# bmi=w/h**2
# if bmi<18.5:
# 	print('您的BMI值为：%f,过轻。'%bmi)
# elif bmi<25:
# 	print('您的BMI值为：%f,正常。' % bmi)
# elif bmi<28:
# 	print('您的BMI值为：%f,过重。' % bmi)
# elif bmi<32:
# 	print('您的BMI值为：%f,肥胖。' % bmi)
# else:
# 	print('您的BMI值为：%f,严重肥胖。' % bmi)

L = ['name', 'sex', 'birthday']
for i in L:
	print('text1:%s' % i)
a = list(range(len(L)))
for i in a:
	print('text2:' + L[i])
i = -3
while i < 0:
	print('text3:' + L[i])
	i = i + 1
