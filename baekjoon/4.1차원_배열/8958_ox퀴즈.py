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

