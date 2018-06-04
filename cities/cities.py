n = int(input())

dest = dict()
for i in range(n):
    start, end = input().split("---")
    # now we have the two strings for each of the first n lines
    # do something with them!
    dest[start] = end


num = int(input())

cities = list()

for i in range(num):
	i = input()
	cities.append(i)

count = list()

for c in cities:
	key = c
	temp = 0
	while(key!='Edmonton'):
		key = dest[key]
		temp += 1
	count.append(temp)

for i in count:
	print(i)


# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines

# for each query, calculate and print the answer
