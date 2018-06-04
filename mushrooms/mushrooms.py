m = int(input())

spots = list(int(i) for i in input().split())

output = list()

x = 0
j = 0

for i in range(len(spots)):
	if i:
		x -= spots[i-1]
	while x < m and j < len(spots) or j <= i:
		x = x + spots[j]
		j += 1
	if x >= m:
		output.append(j-i)
	else:
		output.append(0)

print(*output)
