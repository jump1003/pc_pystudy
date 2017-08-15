# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
	return t[0]


def by_score(t):
	return t[1]


L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse=True)
print('L2=', L2, '\nL3=', L3)
L4 = sorted(L, key=lambda x: x[0])
L5 = sorted(L, key=lambda x: x[1], reverse=True)
print('L4=', L4, '\nL5=', L5)
