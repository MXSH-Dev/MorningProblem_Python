# a queue may be helpful, but is not necessary
from collections import deque

# read the Inputs
n,q=input().split()
n = int(n)
q = int(q)

players = deque(range(n))
passes = q

players.extend([players[0]])
players.popleft()

while len(players) >1:
	for i in range(passes-1):
		players.extend([players[0]])
		players.popleft()
	players.popleft()

print(players[0])

# solve the problem

# print the answer

# Be mindful of running time, deleting an item in the middle of a list is
# too expensive! The intended running time is O(n*q).

# If the test center is taking forever, press ctrl-c from the terminal
# where you launched the test center to quit it prematurely.
