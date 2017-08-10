# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l, str)]
print('L2 :', L2)
L3 = [m.upper() if isinstance(m, str) else str(m) for m in L1]
print('L3 :', L3)


# 斐波那契数列
def fib(N):
	n, a, b = 0, 0, 1
	while n < N:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'FINAL'


f = fib(5)
while True:
	try:
		x = next(f)
		print('f:', x)
	except StopIteration as e:
		print('Generator return value is :', e.value)
		break


# 杨辉三角
def y_triangles():
	T = [1]
	while True:
		yield T
		T.append(0)
		T = [T[i-1] + T[i] for i in range(len(T))]


n = 0
for t in y_triangles():
	print (t)
	n +=1
	if n == 10:
		break