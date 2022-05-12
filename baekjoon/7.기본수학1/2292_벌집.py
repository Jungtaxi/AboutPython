# N = int(input())
# n = 1
# while True:
#     S = 1+(6*(n-1)*n)//2
#     if N <= S:
#         break
#     n +=1
# print(n)

n = int(input())

count = 1
roomSum = 1
while roomSum < n:
    roomSum += 6*count
    count += 1
print(count)