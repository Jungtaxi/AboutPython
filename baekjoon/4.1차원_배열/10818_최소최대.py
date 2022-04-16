N = int(input())
my_list = list(map(int,input().split()))
my_list.sort()
print('{} {}'.format(my_list[0],my_list[N-1]))