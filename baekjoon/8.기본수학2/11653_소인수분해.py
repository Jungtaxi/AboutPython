import math
N = int(input())
mylist = []
i = 2
while N != 1:
    if N % i == 0:
        mylist.append(i)
        N /= i
    else :
        i += 1
for j in mylist:
    print(j)