N = int(input())
l = []
for M in range(1,N+1):
    H=M+sum(map(int, [i for i in str(M)]))
    if H == N:
        l.append(M)
        print(min(l))
        break
else: print(0)