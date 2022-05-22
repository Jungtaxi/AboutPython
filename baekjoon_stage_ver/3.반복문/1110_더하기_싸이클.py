# N = int(input())
# tens = N//10
# ones = N%10
# iter = 0
# while True :
#     iter += 1
#     num = ones 
#     ones = (ones+tens)%10
#     tens = num
#     if N == 10*tens + ones :
#         break
# print(iter)


N = int(input())
iter = 0
num = -1
while num != N :
    if num == -1 :
        num = N
    num = (num%10)*10+((num//10)+num%10)%10
    iter += 1
print(iter)

