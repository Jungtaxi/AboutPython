userPoint = 50
minAblePoint = 10
#조건식 결과에 따른 실행
print('point 사용 가능') if userPoint >= minAblePoint else\
print('포인트 사용 불가')

#조건식 결과를 변수에 할당
result = '가능' if userPoint >= minAblePoint else '불가능'
print('포인트 사용 가능 여부 = {}'.format(result))

#실습
rainPercentage = int(input('비 올 확률 입력 : '))
minRainPercentage = 55

print('우산 챙겨 ') if rainPercentage>=minRainPercentage else print('양산 챙겨')

if rainPercentage>=minRainPercentage :
    print('우산 챙겨')
else :
    print('양산 챙겨')

#실습2
import operator
minTemperature = int(input('최저기온 : '))
maxTemperature = int(input('최고기온 : '))
print('감기 조심하세요') if operator.abs(minTemperature-maxTemperature)>=11 else print('산책하기 좋은 날씨 입니다.')
if operator.abs(minTemperature-maxTemperature) :
    print('일교차 12도')
    print('감기 조심')
else :
    print('9도')
    print('산책하기 좋은 날씨 입니다.')
