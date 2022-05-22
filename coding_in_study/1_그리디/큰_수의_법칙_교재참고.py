N, M, K = map(int,input().split())
mylist = list(map(int,input().split()))

mylist.sort()
first = mylist[-1]
second = mylist[-2]

first_cnt = M//(K+1) + M%(K+1)
second_cnt = M - first_cnt

ans = first_cnt*first + second_cnt*second
print(ans)