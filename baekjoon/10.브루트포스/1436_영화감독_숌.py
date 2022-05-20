N = int(input())

M = 666
cnt = 0
while True:
    if len(str(M).split('666')) > 1 :
        cnt += 1
    if cnt == N :
        print(M)
        break
    M += 1