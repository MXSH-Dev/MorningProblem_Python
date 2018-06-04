n = int(input())

mydict  = dict()

for i in range(n):
    x, y = input().split()
    mydict[x] = y
    # now x is the binary encoding for sequence of word y
    # how do you want to store this?

code = input()

wordlist = list()

temp = ''

for bit in code:
	temp+=bit
	if temp in mydict:
		wordlist.append(mydict[temp])
		temp = ''

# or just simply print(*wordlist)
# this unpacks the list

mystring = ' '.join(wordlist)

print(mystring)
# decode sentence
