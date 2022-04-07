#for문으로 할 때
sum = 0
for i in range(1,11) :
    sum += i
print('sum : {}'.format(sum))

#while 문으로 할 때
sum = 0
i = 1
while i < 11 :
    sum += i
    i += 1
print('sum : {}'.format(sum))
#횟수에 의한 반복문은 for 문이 더 좋다.

#for문
sum = 0
for i in range(1,101) :
    if i % 7 == 0 and sum < 50 :
        sum += i
        print(sum)
        maxInt = i
print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(maxInt))


#while문
sum = 0
i = 0
while sum < 50 :
    i += 1
    if i % 7 == 0 :
        sum += i
        print(sum)
print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(i))



#실습
# 자동차 바퀴가 한번 구를 때마다 0.15mm씩 마모된다고 한다.
# 현재의 바퀴 두께가 30mm이고 최소 운행 가능한 바퀴 두께가 20mm라고 할 때
# 앞으로 구를 수 있는 횟수를 구해보자.

currentThickness = 30
rotationCount = 0
removeThickness = 0.15

while currentThickness >= 20 :
    currentThickness -= removeThickness
    rotationCount += 1
safeRotation = rotationCount - 1
print(safeRotation)