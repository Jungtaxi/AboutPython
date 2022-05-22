def oddNum(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

M, N = map(int,input().split())
numbers = [i for i in range(2,N+1)]
idx = 0
temp = numbers[idx]
while True :
    if oddNum(temp):
        if temp >= M:
            print(temp)
        for i in range(2,(N//temp)+1):
            if i*temp in numbers :
                numbers.remove(i*temp)
    idx += 1
    if idx == len(numbers):
        break
    temp = numbers[idx]

