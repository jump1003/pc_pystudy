#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = float(input('上次考试分数：'))
s2 = float(input('本次考试分数：'))
r = 100 * abs((s2 - s1)) / s1
if s1 > s2:
	print('你的成绩下降了%.2f%%！' % r)
elif s1 == s2:
	print('你的成绩很稳定！')
else:
	print('你的成绩上升了%.2f%%！' % r)
