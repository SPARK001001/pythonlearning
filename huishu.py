# _*_ coding: utf-8 _*_
def is_palindrome(n):
	s = str(n)
	l = len(s)
	flag = True
	for i in range(l//2):
		if s[i] != s[l-i-1]:
			flag = False

	return flag
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
