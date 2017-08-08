#!usr/bin/env python3
# -*- conding: utf-8 -*-

from collections import Iterable,Iterator

def g():
	yield 1
	yield 2
	yield 3

print('[1,2,3] 是否可迭代:',isinstance([1,2,3],Iterable))
print('\'abc\' 是否可迭代:',isinstance('abc',Iterable))
print('123 是否可迭代:',isinstance(123,Iterable))
print('g() 是否可迭代:',isinstance(g(),Iterable))

print('[1,2,3] 是否是迭代器:',isinstance([1,2,3],Iterator))
print('iter([1,2,3]) 是否是迭代器:',isinstance(iter([1,2,3]),Iterator))
print('\'abc\' 是否是迭代器:',isinstance('abc',Iterator))
print('123 是否是迭代器:',isinstance(123,Iterator))
print('g() 是否是迭代器:',isinstance(g(),Iterator))

#iter list
print('for x in [1,2,3,4,5]')
for x in [1,2,3,4,5]:
	print (x)

print('for x in iter([1,2,3,4,5])')
for x in iter([1,2,3,4,5]):
	print (x)

print('next():')
L = iter([1,2,3,4,5])
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))

d = {'a':1,'b':2,'c':3}
#iter each key
print('iter key:')
for k in d.keys():
	print('key is :',k)
#iter each value
print('iter value:')
for k in d.values():
	print('value is :',k)
#iter each item
print('iter item:')
for k,v in d.items():
	print('item is :',k,v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)