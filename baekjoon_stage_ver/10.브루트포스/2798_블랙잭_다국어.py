import sys
N, M= map(int,sys.stdin.readline().strip().split())
numbers = list(map(int,sys.stdin.readline().strip().split()))
gap = M
sum = 0
ans = 0
for i in range(N-2) :
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = numbers[i]+numbers[j]+numbers[k]
            if M-sum<gap and  M>=sum:
                gap = M-sum
                ans = sum
print(ans)