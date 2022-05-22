import sys
C = int(sys.stdin.readline())
for _ in range(C):
    stud_data = list(map(int, sys.stdin.readline().split()))
    avg_score = sum(stud_data[1:])/stud_data[0]
    num = stud_data[0]
    for i in stud_data[1:]:
        if i <= avg_score:
            num -= 1
    print('{:0.3f}%'.format(100*num/stud_data[0]))
    print('{:0.3f}%'.format(100*sum(map(lambda x:x>avg_score,stud_data[1:]))/stud_data[0]))

'''
import sys
for _ in range(int(sys.stdin.readline())):
    a = list(map(int,sys.stdin.readline().strip().split()))
    mean = sum(a[1:len(a)])/a[0]
    print('%.3f'%round(sum(map(lambda x:x>mean, a[1:len(a)]))/a[0]*100,4)+"%")
'''
