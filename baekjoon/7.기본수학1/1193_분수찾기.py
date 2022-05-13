X = int(input())
count = 1
roomSum = 0
while True:
    roomSum += count
    if roomSum >= X:
        break
    count += 1
temp = roomSum-X 
if count % 2 == 1:
    print('{}/{}'.format(1+temp,count-temp))     # 홀수, 아래에서 위로
else :
    print('{}/{}'.format(count-temp,1+temp))     # 짝수, 위에서 아래로