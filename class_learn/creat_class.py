# !usr/bin/env python3
# -*- coding: utf-8 -*-


""" a text class """


__author__ = 'Jump'


class Person(object):
	def __init__(self, name, age, **kw):
		self.__name = name
		self.__age = age
		for k, v in kw.items():
			setattr(self, k, v)

	def info(self):
		print('name:', self.__name)
		print('age:', self.__age)
		print('-----------------------')
p = Person('Jump', 22, sex='boy', Job='Apex')
p.info()
print('sex:', getattr(p, 'sex', None))
print('Job:', getattr(p, 'Job', None))
