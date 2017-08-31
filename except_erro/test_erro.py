# !usr/bin/env python3
# -*- coding: utf-8 -*-
# err_raise.py
import logging


def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' % s)
	return 10 / n


def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		logging.exception('log.txt \n begin: %s \n end' % e)
		# raise ValueError('input err!')
bar()
