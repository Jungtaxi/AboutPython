N = int(input())
l = []
for M in range(1,N+1):
    H=M+sum(map(int, [i for i in str(M)]))
    if H == N:
        print(M)
        break
else: print(0)