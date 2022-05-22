import sys
N = int(input())
score = list(map(int, sys.stdin.readline().split()))
new_score = [100*i/max(score) for i in score ]
print(sum(new_score)/N)
