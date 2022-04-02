# 나머지와 몫 한번에 구하기

num1 = 10
num2 = 3
result = divmod(num1,num2)
print(result)
print('몫 : %d ' % result[0] )
print('나머지 : %d ' % result[1] )

#실습
allStCent = 25
StuCntOfGroup = 4
# groupCnt = allStCent//StuCntOfGroup
# overStuCnt = allStCent % StuCntOfGroup

result = divmod(allStCent, StuCntOfGroup)
groupCnt = result[0]
overStuCnt = result[1]


print('전체 학생 수 {}'.format(allStCent))
print('한 모둠 학생 수 {}'.format(StuCntOfGroup))
print('모둠 수 {}'.format(groupCnt))
print('남는 학생 수 {}'.format(overStuCnt))
