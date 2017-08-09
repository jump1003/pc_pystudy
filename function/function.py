#!usr/bin/env python3
# -*- coding: utf-8 -*-


def area_of_circle(r):
	PI = 3.14159
	return PI * r ** 2


def sum1(start, end, func):
	total = 0
	for x in range(start, end):
		total += func(x)
	return total


def func1(x):
	return x


def func2(x):
	return 2 * x + 1


print(area_of_circle(3))
print(sum1(1, 6, func1))
print(sum1(1, 4, func2))
