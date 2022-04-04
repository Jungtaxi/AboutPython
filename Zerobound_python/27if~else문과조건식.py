userPoint = 50
minAblePoint = 10
#조건식 결과에 따른 실행
print('point 사용 가능') if userPoint >= minAblePoint else\
print('포인트 사용 불가')

#조건식 결과를 변수에 할당
result = '가능' if userPoint >= minAblePoint else '불가능'
print('포인트 사용 가능 여부 = {}'.format(result))