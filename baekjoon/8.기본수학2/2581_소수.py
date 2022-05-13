def oddNum(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
M = int(input())
N = int(input())

result = [i for i in range(M,N+1) if oddNum(i) ]

if result == []:
    print(-1)
else :
    print(sum(result))
    print(result[0])