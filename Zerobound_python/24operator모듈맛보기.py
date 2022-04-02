# 산술 연산자 관련 함수
import operator
num1 = 9
num2 = 8
print('{} + {} = {}'.format(num1,num2,operator.add(num1,num2)))
print('{} - {} = {}'.format(num1,num2,operator.sub(num1,num2)))
print('{} * {} = {}'.format(num1,num2,operator.mul(num1,num2)))
print('{} / {} = {}'.format(num1,num2,operator.truediv(num1,num2)))
print('{} % {} = {}'.format(num1,num2,operator.mod(num1,num2)))
print('{} // {} = {}'.format(num1,num2,operator.floordiv(num1,num2)))
print('{} ** {} = {}'.format(num1,num2,operator.pow(num1,num2)))
print()

# 비교 연산자 관련 함수
print('{} == {} : {}'.format(num1,num2,operator.eq(num1,num2))) #equal
print('{} != {} : {}'.format(num1,num2,operator.ne(num1,num2))) #not equal
print('{} > {} : {}'.format(num1,num2,operator.gt(num1,num2))) #greater
print('{} >= {} : {}'.format(num1,num2,operator.ge(num1,num2))) #greater equal
print('{} < {} : {}'.format(num1,num2,operator.lt(num1,num2))) #little
print('{} <= {} : {}'.format(num1,num2,operator.le(num1,num2))) #little equal
print()

# 논리 연산자 관련 함수
flag1 = True
flag2 = False
print('{} and {} : {}'.format(flag1,flag2,operator.and_(flag1,flag2)))
print('{} or {} : {}'.format(flag1,flag2,operator.or_(flag1,flag2)))
print('not {} : {}'.format(flag1,operator.not_(flag1)))
print()

# 실습
# 백신 접종 대상자는 20세 미만 또는 60세 이상자에 한합니다.
age = int(input("나이 입력 : "))
vaccine = operator.not_(operator.and_(operator.ge(age,20),operator.lt(age,60)))
print('age : %d , vaccine : %s' % (age, vaccine))

'''
vaccine = (age<20) or (age>=60)
print('age : %d, vaccine : %s' % (age, vaccine))
'''
print()

# 실습
# random과 operator 모듈을 사용해서 10부터 100사이의 난수 중 십의 자리와 일의 자리가 각각 3의 배수인지 판단하는 코드를 작성해보자.
import random

rInt = random.randint(10,100)
num10 = operator.floordiv(rInt,10)
num1 = operator.mod(rInt,10)

print('난수 : %d' % rInt)
print('십의 자리 : %d' % num10)
print('일의 자리 : %d' % num1)
print('십의 자리는 3의 배수이다 : {}'.format(operator.mod(num10, 3) == 0 ))
print('일의 자리는 3의 배수이다 : {}'.format(operator.mod(num1,3) == 0 ))
