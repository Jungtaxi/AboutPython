# break은 남은 반복문 종료
sum = 0
searchNum = 0
for i in range(100) :
    sum +=i
    if sum >100 :
        searchNum = i
        break
print('searchNum : {}'.format(searchNum))

#실습
#10의 팩토리얼 (10!)을 계산하는 과정에서 결과값이 50을 넘을 때의 숫자를 구하자.
result = 1
num = 0
for i in range(1,11):
    result *= i
    if result > 50 :
        num = i
        break
print('구하고자 하는 숫자는 {}, 계산 값은 {}'.format(num,result))

#실습
#새끼 강아지 체중이 2.2kg이 넘으면 이유식을 중단하려고 한다.
#한번 이유식을 먹을 때 체중이 70g 증가한다고 할 때,
#예상되는 이유식 날짜를 구하자. (현재 체중은 800g 이다.)
currentWeight = 800
maxWeight = 2200
date = 0
while True :
    currentWeight += 70
    date += 1
    if currentWeight > maxWeight :
        break
print('이유식 날짜는 {}일이고, 강아지 몸무게는 {} 이다.'\
.format(date,currentWeight))