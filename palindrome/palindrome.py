# read the input
read =input().lower()


out = 1

for i in range(len(read)):
	left = i
	right = i

	while left >= 0 and right <len(read):
		if read[left] != read[right]:
			break
		out = max(out, right - left +1)
		left -= 1
		right += 1

print(out)