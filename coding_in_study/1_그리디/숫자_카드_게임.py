N,M = map(int,input().split())

mylist = [[] for _ in  range(N)]

minmax = 0
for i in range(N):
    mylist[i] = list(map(int,input().split()))
    if minmax < min(mylist[i]):
        minmax = min(mylist[i])

print(minmax)