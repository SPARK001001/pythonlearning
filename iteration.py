# _*_ coding:utf-8 _*_
def findMinAndMax(l):
	if(len(l)==0):
		return(None,None)
	max = l[0]
	min = l[0]
	for i in l:
		if i<=min:
			min = i
		if i>=max:
			max = i
	return (min,max)

def triangles():
	L = L[1]
	while true:
		yield L 
		L = [L[x]+L[x+1] for x in range(len(L)-1)]
		L.insert(0,1)
		L.append(1)

