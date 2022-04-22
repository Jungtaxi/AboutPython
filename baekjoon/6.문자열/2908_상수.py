#for loop
# A, B = input().split()
# reverse_A=''
# reverse_B=''
# for i in range(3):
#     reverse_A += A[i] + reverse_A
#     reverse_B += B[i] + reverse_B
# A = int(reverse_A)
# B = int(reverse_B)
# if A>=B :
#     print(A)
# else :
#     print(B)

#reversed()
# A, B = input().split()
# A = int(''.join(reversed(A)))
# B = int(''.join(reversed(B)))
# if A>=B : print(A)
# else : print(B)

#slice
A,B = input().split()
A = int(A[::-1])
B = int(B[::-1])
if A>=B : print(A)
else : print(B)