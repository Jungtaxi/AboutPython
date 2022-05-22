import sys
A, B, V = map(int, sys.stdin.readline().split() )
day = (V-A) // (A-B)
temp = (A-B)*day
while True :
    temp += A
    day += 1
    if temp >= V:
        break
    temp -= B

print(day)