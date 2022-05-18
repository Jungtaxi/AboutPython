import sys
N = int(sys.stdin.readline().strip())
profiles = []
for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    profiles.append([x,y])
rank = []
for i in range(N):
    a = 1
    for x,y in profiles:
        if profiles[i][0] < x and profiles[i][1] < y :
            a += 1
    rank.append(a)
print(' '.join(map(str,rank)))