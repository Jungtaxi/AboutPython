N = int(input())
iter = 0
num = -1
while num != N :
    if num == -1 :
        num = N
    num = (num%10)*10+((num//10)+num%10)%10
    iter += 1
print(iter)

