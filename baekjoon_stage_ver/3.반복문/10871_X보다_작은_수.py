N, X = map(int,input().split())
A = list(map(int,input().split()))
my_list = [i for i in A if i<X ]
print(" ".join(map(str, my_list)))