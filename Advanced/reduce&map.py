# !usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def normalize(name):
	result = name[0].upper() + name[1:].lower()
	return result


L1 = ['adam', 'LISA', 'barT', 'jUmP']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
	return reduce(lambda x, y: x*y, L)

print('3* 5* 7* 9 =', prod([3, 5, 7, 9]))


def str2float(s):
	def f1(f):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[f]
	n = s.split('.')
	return reduce(lambda x, y: x*10+y, map(f1, n[0]))+reduce(lambda x, y: x*0.1 + y, map(f1, n[1][::-1])*0.1

print('str2float(\'123.456\')=', str2float('123.456'))
