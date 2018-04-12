#!/usr/bin/env python3
def product(*w):
	for i in w:
		if not isinstance(i,(int,float)):
			raise TypeError('填数字') 
	if(len(w)>0):
		p = 1
		for i in w:
			p = p*i
		return p
	else:
		raise TypeError('天数')
