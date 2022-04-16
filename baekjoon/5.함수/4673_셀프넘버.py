# def d(n):
#     d_list = map(int,list(str(n)))
#     return ( sum(d_list) + n )

# n=1
# my_list = []
# while n < 10000:
#     if n not in my_list:
#         print(n)
#         my_list.append(n)
#     if d(n) < 10000:
#         my_list.append(d(n))
#     n += 1

# def d(n):
#     for i in str(n):
#         n += int(i)
#     return n

# numbers = set(range(1,10001))
# remove_numbers = set()

# for num in numbers:
#     remove_numbers.add(d(num))

# self_numbers = numbers - remove_numbers
# for i in sorted(self_numbers):
#     print(i)

from ast import Num


def d(n):
    for i in str(n):
        n += int(i)
    return n

arr = [True for i in range(1,10001)]
for i in range(1,10001):
    num = d(i)
    if num <= 10000 :
        print(num)
        arr[num] = False
for i in range(1,10001):
    if arr[i] :
        print(i)

