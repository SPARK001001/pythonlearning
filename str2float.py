from functools import reduce
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}
def str2float(s):
	str = s.split('.')
	def f(x,y):
		if y == '.':
			return x
		return x * 10 + y
	def f2(x,y):
		return x * 0.1 + y
	def char2num(s):
		return DIGITS[s]
	return reduce(f,map(char2num,str[0])) + 0.1*reduce(f2,map(char2num,str[1][::-1]))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
