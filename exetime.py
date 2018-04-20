# _*_ coding: utf-8 _*_
import time, functools
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		start = time.clock()
		fn(*args,**kw)
		elapsed = (time.clock() - start)
		print('%s executed in %s ms ' % (fn.__name__,elapsed))
		return fn(*args,**kw)
	return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f == 33:
    print('测试成功!')
elif s != 7986:
    print('测试失败!')
