import sys
# my_list = []
# for i in range(9):
#     my_list.append(int(sys.stdin.readline().strip()))
# print(max(my_list))
# print(my_list.index(max(my_list))+1)

my_list = [int(sys.stdin.readline()) for i in range(9)]
print(max(my_list))
print(my_list.index(max(my_list))+1)