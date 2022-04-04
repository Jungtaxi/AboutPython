num1 = 10
num2 = 20
numResult = True if num1 > num2 else False
print('num1>num2 : {}'.format(numResult))
print('num1이 num2 보다 크다.') if numResult else print('num1이 num2보다 작다.')


#실습1
#적설량을 입력하고 적설량이 30mm 이상이면 대설 경보를 발령하고 그렇지 않으면 대설 경보를 해제하는 코드를 작성해보자

limitSnowAmount = 30
snowAmount = int(input('적설량 입력(mm) : '))
print(f'{snowAmount}mm, 적설 경보! ') if snowAmount >= limitSnowAmount else \
print(f'{snowAmount}mm, 적설 경보 해제')

#실습2
#국어, 영어, 수학 점수를 입력하면 조건식을 이용해 과목별 결과와 전체 결과를 출력하는 코드를 작성해보자.

import operator

passScore1 = 60
passScore2 = 70

korScore = int(input(('국어점수 : ')))
engScore = int(input('영어점수 : '))
matScore = int(input('수학점수 : '))

totalScore = korScore + engScore + matScore
scoreAvg = totalScore / 3

print('국어 : PASS') if operator.ge(korScore, passScore1) else print('국어 FAIL')
print('영어 : PASS') if operator.ge(engScore, passScore1) else print('영어 FAIL')
print('수학 : PASS') if operator.ge(matScore, passScore1) else print('수학 FAIL')
print('시험 : PASS') if operator.ge(scoreAvg, passScore2) else print('시험 FAIL')

print('총점 : %d, 평균 : %.2f' % (totalScore, scoreAvg))

