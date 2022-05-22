import sys
sys.setrecursionlimit(10**6)

def star(N):
    if N ==1 :
        return ['*']
    before = star(N//3)
    l = []
    for i in before:
        l.append(3*i)
    for i in before:
        l.append(i+' '*(N//3)+i)
    for i in before:
        l.append(3*i)
    return l

N = int(input())
print('\n'.join(star(N)))