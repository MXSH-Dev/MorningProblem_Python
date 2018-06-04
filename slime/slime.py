# read the input
n  = int(input())
row = [1]

def check(row):
	while len(row)>1 and row[-1] == row[-2]:
		row.pop()
		row[-1]+=1
	return row

for  i in range(n-1):
	row.append(1)
	check(row)



print(*row)

# print(row)

# solve the problem

# print the answer

# ????

# profit!
