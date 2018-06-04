# read the first line

# read the calls

# read and process each query

n,q = list(int(i) for i in input().split())


call = list(int(i) for i in input().split())

call_count = list()
call_count.append(0)

for i in range(1,n+1):
	call_count.append(call_count[i-1]+call[i-1])

for i in range(q):
	temp = list(input().split())
	start = int(temp[0])
	end = int(temp[1])
	print(call_count[end] - call_count[start-1])

# too slow~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# for i in rnage (1,n+1):
# 	new_call.append(int(call[i-1])+)