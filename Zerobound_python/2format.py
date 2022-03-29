name = "홍길동"
age = 28

#f 사용
print(f"내 이름은 {name} 입니다. 내 나이는 {age} 입니다.")
#format 함수 사용
print("내 이름은 {} 입니다. 내 나이는 {} 입니다.".format(name, age))
#format에서 인덱스 사용
print("내 이름은 {0} 입니다. 내 나이는 {1} 인데, 내 이름은 {0} 입니다.".format(name,age))

#형식문자 이용한 데이터 출력 
print('user name : %s' % name)
print('user age : %d' % age )
print('내 이름은 %s, 내 나이는 %d' % (name, age))

# 소숫점 자리 수 정하기 %.nf -> 소수점 n 자리 까지 표현
pi = 3.141
print('pi : %f' % pi)
print('pi : %g' % pi )
print('pi : %.1f' % pi)
print('pi : %d' % pi)
print('pi : %.3f' %pi)
print('pi : %+10f' % pi)

