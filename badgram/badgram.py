import sys

bad_letters = ['v','k','j','x','q','z']

for line in sys.stdin:
	if line.strip() !='':
		counter = 0
		reached = list()

		for char in line.strip().lower():
			if (char in bad_letters) and (char not in reached):
				counter = counter +1
				reached.append(char)
		if counter>4:
			print('BAD')
		else:
			print('OK')


