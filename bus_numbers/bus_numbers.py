N = int(input())

bus = list(int(i) for i in input().split())

bus.sort()

seq = list()

seq.append([bus[0]])

for i in range(1,len(bus)):
	if bus[i] - bus[i-1] == 1:
		seq[-1].append(bus[i])
	else:
		seq.append([bus[i]])

output = ''

for s in seq:
	if len(s) <=2:
		output += ' '.join(str(i) for i in s)
	else:
		output += '{}-{}'.format(s[0],s[-1])
	output += ' '

print(output[:len(output)-1])