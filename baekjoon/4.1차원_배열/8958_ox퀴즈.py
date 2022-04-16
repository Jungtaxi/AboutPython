# X를 기준으로 split 하기
# import sys

# n = int(input())
# for i in range(n):
#     ans = sys.stdin.readline().rstrip()
#     res = 0
#     for j in ans.split('X'):
#         k = j.count('O')
#         res += k*(k+1)/2

#     print(int(res))

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    quiz = sys.stdin.readline().rstrip()
    score = 0
    sum = 0
    for i in range(len(quiz)) :
        if quiz[i] == 'O':
            score += 1
        else :
            score = 0
        sum += score
    sys.stdout.write('{}\n'.format(str(sum)))

