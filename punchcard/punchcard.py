import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        print()
        continue
    line = ''.join(map(lambda ch: '1' if ch == 'X' else '0', line))
    print(chr(int(line, 2)), end='')

