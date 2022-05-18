import sys
sys.setrecursionlimit(10**6)

def star(N):
    if N == 1:
        return ['*']
    stars = star(N//3)
    L = []

    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(N//3)+s)
    for s in stars:
        L.append(s*3)
    return L

N = int(sys.stdin.readline().strip())
print('\n'.join(star(N)))