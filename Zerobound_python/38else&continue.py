# continue는 실행 생략하고 다음 반복 실행 시작
for i in range(100):
    if i % 7 != 0 :
        continue
    print('{}는 7의 배수 입니다.'.format(i))

# else는 반복문이 종료된 후 실행
cnt=0
for i in range(1,100) :
    if i %7 != 0 :
        continue
    print('{}는 7의 배수'.format(i))
    cnt += 1
else:
    print('99개의 정수 중 7의 배수는 {}개 입니다.'.format(cnt))

#실습
#1부터 100까지 정수 중 3과 7의 공배수를 출력하자
minNum = 0
for i in range(1,101) :
    if i % 3 != 0 or i % 7 != 0 :
        continue
    print('공배수 : {}'.format(i))
    if minNum == 0 :
        minNum = i
else :
    print('최소공배수는 {} 입니다.'.format(minNum))    
