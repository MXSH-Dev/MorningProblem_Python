n = int(input())

arr = list(int(i) for i in input().split())

# print(n,*arr)
temp_max = arr[0]
maximun = arr[0]

for i in range(1,n):
	temp_max = max(arr[i],temp_max+arr[i])
	maximun = max(maximun,temp_max)

if maximun >0:
	print(maximun)
else:
	print(0)