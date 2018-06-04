# read the Inputs

# solve the problem

# print the answer

# be mindful of the running time: O(n^3) is not fast enough

n = int(input())

list1 = list(int(i) for i in input().split())
list2 = list(int(i) for i in input().split())

sums = list()
for i in list1:
	for j in list2:
		sums.append(i+j)

sums = set(sums)
count = 0

list3 = list(int(i) for i in input().split())

for k in list3:
	if k in sums:
		count+=1

print(count)