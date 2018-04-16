# _*_ coding:utf-8 _*_
def createCounter():
	s = [0]
	def counter():
		s[0] += 1
		return s[0]
	return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

L = list(filter(lambda n : n % 2 == 0,range(1,20)))
print(L)
