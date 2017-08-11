# !usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def normalize(name):
	result = name[0].upper() + name[1:].lower()
	return result


L1 = ['adam', 'LISA', 'barT', 'jUmP']
L2 = list(map(normalize, L1))
print(L2)
