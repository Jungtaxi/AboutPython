import sys
M, N = map(int, sys.stdin.readline().split())
tile = []
for _ in range(M):
    L = sys.stdin.readline().strip()
    tile.append(L)

color1, color2 = 'B', 'W'

mincnt = 64

for m in range(M-7): 
    for n in range(N-7):
        
        cnt1, cnt2 = 0, 0
        for i in range(m,m+8):
            for j in range(n,n+8):
                if tile[i][j] != color1 :
                    cnt1 += 1
                if tile[i][j] != color2 :
                    cnt2 += 1
                color1, color2 = color2, color1
            color1, color2 = color2, color1

        if cnt1<mincnt : mincnt = cnt1
        if cnt2<mincnt : mincnt = cnt2

print(mincnt)

