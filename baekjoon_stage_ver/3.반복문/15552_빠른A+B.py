from sys import stdin as si
from sys import stdout as so
input = si.readline
print = so.write
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    print('%d\n' % (A+B))