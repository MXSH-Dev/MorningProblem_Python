words = list(input().split())

# words is now a list of all strings in the input
# print(words)
# finish the problem!
morning = dict()

count = 0

output = list()

for word in words:
	if word not in morning:
		morning[word] = 1
	else:
		morning[word] +=1

# print(moring)

for key in morning:
	if morning[key] > count:
		count = morning[key]

for key in morning:
	if morning[key] == count:
		output.append(key)

output = sorted(output)

for item in output:
	print(item)