import sys 
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
for i in range(1,N+1) :
    output('{}\n'.format('*'*i))