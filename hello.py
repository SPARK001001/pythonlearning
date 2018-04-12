#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
print('hello world!')


name = input('please enter your name: ')
print('hello', name)

s1 = 72
s2 = 85
r = (s2-s1)/s2
print('小明成绩提升的百分点%.4f'%r)

s = input('birth:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')

sum = 0
for x in range(101):
	sum = sum + x
print(sum)


def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
