# -*- coding: utf-8 -*-


def _iter():
	i = 10
	while True:
		i = i + 1
		yield i
#
#
# def _not_divisible(n):
# 	return lambda x: x % n > 0
#
#
# def primes():
# 	it = _iter()  # 初始序列
# 	while True:
# 		n = next(it)  # 返回序列的第一个数
# 		yield n
# 		it = filter(_not_divisible(n), it)  # 构造新序列
#
#
# for n in primes():
# 	if n < 50:
# 		print(n)
# 	else:
# 		break


def is_palindrome(n):
	return n == int(str(n)[::-1])


def back_num(end):
	return list(filter(is_palindrome, range(1, end)))

print(back_num(100))
