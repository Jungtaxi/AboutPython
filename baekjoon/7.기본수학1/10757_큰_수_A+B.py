for i in range(11) :
    A = input().split()
    for j in A :
        if j == A[len(A)-1] :
            print(j,end='.py\n')
        print(j,end='_')
