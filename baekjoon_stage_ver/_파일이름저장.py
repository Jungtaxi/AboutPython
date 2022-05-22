c=0
B=[]
C=[]
while True:
    c += 1
    A = input().split()
    if A == ['.']:
        break
    if c%2 ==0 :
        continue
    try :
        A.remove('다국어')
    except :
        pass
    B = A[1:-3]
    C.append(B)

for i in C :
    print('_'.join(i), end='.py')
    print()
