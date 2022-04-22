# A, B = input().split()
# new_A=''
# new_B=''
# for i in range(3):
#     new_A += A[2-i]
#     new_B += B[2-i]
# A = int(new_A)
# B = int(new_B)
# if A>=B :
#     print(A)
# else :
#     print(B)

A, B = input().split()
A.reverse()
B.reverse()