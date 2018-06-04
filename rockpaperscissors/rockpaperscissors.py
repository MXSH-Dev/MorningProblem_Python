num_matches = int(input())

Bob_Match = 0
Alice_Match = 0

for i in range(num_matches):
    rounds = input().split()
    # print(rounds)
    Alice =0
    Bob = 0
    for match in rounds:
    	if match == "RS" or match == "PR" or match == "SP":
    		Alice = Alice +1
    	elif match == "SR" or match == "RP" or match == "PS":
    		Bob = Bob+1
    # print(Bob)
    # print(Alice)
    if Bob > Alice:
    	Bob_Match += 1
    	Alice =0
    	Bob = 0
    elif Alice >Bob:
    	Alice_Match += 1
    	Alice =0
    	Bob = 0
    # print(rounds)
    # now rounds is a list of the rounds in this match
    # example: if the line of input was "RR RP SR" then
    # rounds == ["RR", "RP", "SR"]
    # now do the rest!
if Bob_Match>Alice_Match:
	print("Bob",Bob_Match)
else:
	print("Alice",Alice_Match)

# print here whoever is the overall winner of all the matches and
# how many matches the winner won
