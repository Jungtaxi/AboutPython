n = 1
while n < 10 :
    print(f'{n}번째')
    n += 1

flag = True
num = 0
sum = 0
while flag :
    num += 1
    sum += num 
    print('{}까지의 합은 {}입니다.'.format(num,sum))
    if num >= 10 :
        flag = False

# 하루에 독감으로 병원에 내방하는 환자 수가 50명에서 100명 사이일 때,
# 누적 독감 환자 수가 최초로 10,000명을 넘는 날짜를 구해보자.
import random
sum = 0
dayCount = 0
while sum < 10000 :
    patientNum = random.randint(50,100)
    sum += patientNum
    dayCount += 1
print('오늘로부터 {} 후'.format(dayCount))

sum = 0
date = 0
flag = True

while flag:
    patientNum = random.randint(50,100)
    sum += patientNum
    date += 1

    print('날짜:{},\t오늘 환자 수:{},\t누적 환자 수 :{}'.format(date,patientNum,sum))

    if sum>=10000 :
        flag = False