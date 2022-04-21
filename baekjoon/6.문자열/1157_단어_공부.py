# alpha = input().upper()
# alphabet = set(alpha)
# max_c = 0
# second_c = 0
# second_ans = '.'
# for i in alphabet:
#     c=0
#     for j in alpha:
#         if i == j :
#             c += 1
#     if c == max_c:
#         second_ans = ans
#         second_c = c
#         ans = i
#     elif c>max_c :
#         max_c = c
#         ans = i
# if second_c==max_c and second_ans != ans :
#     print('?')
# else :
#     print(ans)


import collections

s= list(input().upper())

count = collections.Counter(s)
if len(set(s)) == 1:
    print(count.most_common()[0][0])
elif count.most_common()[0][1] == count.most_common()[1][1] :
    print('?')
else :
    print(count.most_common()[0][0])
