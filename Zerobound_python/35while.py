#1부터 100까지 정수 중 2의 배수와 3의 배수 출력

n=1
while n < 101 :
    if n % 2 == 0:
        print(f'{n}은 2의 배수 입니다.')
    if n % 3 == 0 :
        print(f'{n}은 3의 배수 입니다.')
    n += 1

gugudanNum = int(input('희망 구구단 입력 : '))

n = 1
while n<10 :
    print('{}*{}={}'.format(gugudanNum, n, gugudanNum*n))
    n += 1
