n = int(input())

sizes = list(int(i) for i in input().split())

def subsum(array, n, SUM):
	if SUM == 0:
		return True
	if n == 0 and SUM != 0:
		return False
	if array[n-1] > SUM:
		return subsum(array,n-1,SUM)
	return subsum(array,n-1, SUM) or subsum (array,n-1, SUM - array[n-1])

def findp(array,n):
	SUM = 0
	for i in range(0,n):
		SUM += array[i]
	if SUM %2 != 0:
		return False
	return subsum(array,n,SUM/2)

if findp(sizes,n) == True:
	print("True")
else:
	print("False")