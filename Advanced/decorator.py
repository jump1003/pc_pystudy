# -*- coding: utf-8 -*-
import functools


def log1(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call %s' % func.__name__)
		f = func(*args, **kw)
		print('end call %s' % func.__name__)
		return f
	return wrapper


@log1
def hello():
	print('%s is running' % hello.__name__)


def deco(*msg):
	text = msg[0] if isinstance(msg[0], str) else None
	if text:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('%s,begin call %s' % (text, func.__name__))
				f = func(*args, **kw)
				print('%s,end call %s' % (text, func.__name__))
				return f
			return wrapper
		return decorator
	else:
		@functools.wraps(msg[0])
		def wrapper(*args, **kw):
			print('begin call %s' % msg[0].__name__)
			f = msg[0](*args, **kw)
			print('end call %s' % msg[0].__name__)
			return f
		return wrapper


@deco
def deco1():
	print('%s is running' % deco1.__name__)


@deco('deco')
def deco2():
	print('%s is running' % deco2.__name__)
# hello()
# print('-------------------')
# deco1()
# print('-------------------')
# deco2()
