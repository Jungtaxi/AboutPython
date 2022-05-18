import sys
sys.setrecursionlimit(10 ** 6)

def starblink(N):
    if N == 3 :
        return [[],[1]]

    beforeblink = starblink(N//3)

    blinklist = [[],[]]
    blinklist[0] = beforeblink[0]+beforeblink[1]
    for i in range(len(blinklist[0])):
        blinklist[0].append(blinklist[0][i] + N//3)
        blinklist[0].append(blinklist[0][i] + 2*(N//3))

    blinklist[0] = list(set(sorted(blinklist[0])))

    blinklist[1] = [i for i in range(N//3,(N//3)*2)]

    return blinklist

N = int(input())
blinklist = starblink(N)

for i in range(N):
    for j in range(N):
        if i in blinklist[0] and j in blinklist[0]:
            print(' ',end='')
        elif i in blinklist[1] and j in blinklist[1]:
            print(' ',end='')
        else : print('*',end='')
    print()