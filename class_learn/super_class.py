# !usr/bin/env python3
# -*- coding: utf-8 -*-


class A(object):
	def __init__(self):
		print('enter A')
		super(A, self).__init__()
		print('leave A')


class B(object):
	def __init__(self):
		print('enter B')
		super(B, self).__init__()
		print('leave B')


class C(A):
	def __init__(self):
		print('enter C')
		super(C, self).__init__()
		print('leave C')


class D(A):
	def __init__(self):
		print('enter D')
		super(D, self).__init__()
		print('leave D')


class E(B, C):
	def __init__(self):
		print('enter E')
		super(E, self).__init__()
		# B.__init__(self)
		# C.__init__(self)
		print('leave E')


class F(E, D):
	def __init__(self):
		print('enter F')
		super(F, self).__init__()
		# E.__init__(self)
		# D.__init__(self)
		print('leave F')


if __name__ == '__main__':
	f = F()
	print(F.__mro__)