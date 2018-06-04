heights = input().split()
heights = list(map(int,heights))

length = len(heights)

result = list()

for i in range(length):
	if i == 0:
		result.append("X")
	else:
		index = i-1
		while(heights[i] > heights[index] and index >=0):
			if result[index] == 'X':
				index = -1
			else:
				index = result[index]
		if index <0:
			result.append("X")
		else:
			result.append(index)

print(*result)