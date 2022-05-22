# N개 배열, 하나의 숫자는 연달아 K개만 쓸 수 있음, 총 M개의 숫자를 더함
N, M, K = map(int,input().split())
mylist = list(map(int,input().split()))
max_item = 0
max_idx = 0
for i in range(N):                  # max 값과, max의 인덱스 값을 구한다.
    if max_item < mylist[i]:
        max_item = mylist[i]
        max_idx = i

del mylist[max_idx]                # max 값을 소거한 후 최댓값을 구해 두번째로 최댓값을 구했다.
second_item = max(mylist)

ans, cnt = 0, 0
while M > 0:
    if M > K and cnt%(K+1) == 0: # 이전에 두번째 최댓값이 더해졌고, M이 아직 K보다 크면
        ans += K*max_item        # 최댓값을 K개 더한다.
        cnt += K                 # K개 만큼 count가 더해진다.
        M -= K                   # K개 만큼 M에서 K가 빠진다.

    elif M < K and cnt%(K+1) == 0:  # 이전에 두번째 최댓값이 더해졌고, M이 K보다 작으면
        ans += M*max_item           # 남은 M개를 만큼 최댓값을 다 더한다.
        M -= M                      # M이 다 소진되고, While문은 끝이 난다.

    else:
        ans += second_item      # 이전에 max_item 일 때
        cnt += 1                # 두번째로 최댓값을 더한 후, count를 1 센다.
        M -= 1                  # M에서 1 뺀다.
print(ans)