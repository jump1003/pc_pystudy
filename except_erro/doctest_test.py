# -*- coding: utf-8 -*-


def fact(n):
	'''
	function fact
	example:
	>>> fact(1)
	1
	>>> fact(0)
	Traceback (most recent call last):
        ...
	ValueError
	>>> fact(5)
	120
	>>> fact(1000)
	Traceback (most recent call last):
        ...
	RecursionError: maximum recursion depth exceeded in comparison
	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	return n * fact(n-1)


if __name__ == '__main__':
	import doctest
	doctest.testmod()
