import sys
N, M = map(int,sys.stdin.readline().split())
mylist = [sys.stdin.readline().rstrip() for _ in range(N)]

ans_chr = ''
ans_distence = 0

for i in range(M):
    dic = dict()
    dic['A'],dic['T'],dic['G'],dic['C'] = 0, 0, 0, 0
    
    for j in range(N):
        dic[mylist[j][i]] += 1
    
    max_cnt = 0
    max_char = ''
    for k in dic:
        if max_cnt < dic[k]:
            max_cnt = dic[k]
            max_chr = k
        elif max_cnt == dic[k]:
            if max_chr > k:
                max_chr = k
    ans_chr += max_chr
    ans_distence += N - max_cnt

print(ans_chr)
print(ans_distence)