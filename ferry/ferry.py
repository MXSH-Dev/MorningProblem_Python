import math
west=list(int(i) for i in input().split())
east=list(int(i) for i in input().split())

position='w'

time=0

while west or east:
    if west:
        w_head=west[0]
    else:
        w_head=math.inf

    if east:
        e_head=east[0]

    else:
        e_head=math.inf

    if w_head<e_head:
        west.pop(0)
        if position=='w':
            if time>w_head:
                time=time+100
            else:
                time=w_head+100
            position='e'
        elif position=='e':
            if time>w_head:
                time=time+200
            else:
                time=w_head+200
            position='e'
    elif w_head>e_head:
        east.pop(0)
        if position=='w':
            if time>e_head:
                time=time+200
            else:
                time=e_head+200
            position='w'

        elif position=='e':
            if time>e_head:
                time=time+100
            else:
                time=e_head+100
            position='w'

print(time)
