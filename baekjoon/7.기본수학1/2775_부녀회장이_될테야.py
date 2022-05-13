T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    mylist = [[0]*(n+1) for _ in range(k+1)]     # k행 n열의 아파트 구조. 
    mylist[0] = [i for i in range(n+1)]          # 0행을 채워줍시다.

    for h in range(1,k+1):                       # 1행부터 k행 까지; h
        mylist[h] = [sum(mylist[h-1][:w+1]) for w in range(n+1)]      # 각 호수를 채워줬습니다; w
    
    print(mylist[k][n])