T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    X = N//H+1              # 호수는 H로 나눈 몫이다. 단, 처음은 0이 아니라 1부터 시작하기 때문에 1을 더해줘야함
    Y = N%H                 # 층은 H로 나눈 후 나머지 값이다.
    if N % H == 0 :         # N이 H로 나누어 떨어지게 되면
        Y = H               # Y값은 0이 아니라 H가 되어야 한다.
        X = N//H            # X값은 N//H+1 이 아니라 N//H 이다.
                            # 이는 N%H 값이 0일 때, N//H 값이 알아서 1 올라간 상태이기 때문이다. 

    if X < 10 :             # X가 10보다 작으면 X 앞에 '0'을 붙여줘야 한다.
        X = '0'+str(X)

    print('{}{}'.format(Y,X))