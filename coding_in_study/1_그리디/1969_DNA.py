import sys
# N 은 DNA 갯수, M은 DNA 길이
N, M = map(int,sys.stdin.readline().split())
mylist = [sys.stdin.readline().strip() for _ in range(N)]

# 각 자리만 따서 이중 리스트 만듬
# 가령 ABCD, AABD 있으면, 각 자리 따서 [AA,BA,CB,DD] 만드는 식
l = [[mylist[i][j] for i in range(N)] for j in range(M)]

# 가장 많은 count 가진 철자 뽑아보자.
anschar = ''
hamming = 0
for i in range(M):   # DNA 길이 만큼
    max_cnt = 0
    char = ''
    for j in range(N):
        cnt = l[i].count(l[i][j])
        if max_cnt < cnt:
            max_cnt = cnt
            char = l[i][j]
        elif max_cnt == cnt:
            if char > l[i][j]:
                char = l[i][j]
    anschar += char
    hamming += N - max_cnt

print(anschar)
print(hamming)
