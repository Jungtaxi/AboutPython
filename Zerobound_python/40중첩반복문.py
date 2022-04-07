# 별 찍기
for i in range(1,10):
    for j in range(i):
        print('*', end = '')
    print()

# 일반적으로 중첩 반복문은 보통 2개, 최대 3개까지만 쓴다.
# 별 거꾸로 찍기
# for i in range(1,10):
#     for j in range(10-i):
#         print('*',end='')
#     print()

for i in range(9,0,-1):
    for j in range(i):
        print('*', end='')
    print()


# 구구단 전체 출력하기
for i in range(1,10):
    for j in range(1,10):
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    print() 
    