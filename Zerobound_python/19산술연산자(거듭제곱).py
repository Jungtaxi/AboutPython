
print('2의 3 거듭제곱 : %d ' %2**3)
print()

# 제곱근 구하기

print("2의 제곱근 %.2f" % 2**(1/2))
print("2의 세제곱근 %.2f" % 2**(1/3))
print()

# math 모델의 sqrt() 와 pow() 함수
import math
print('3의 2제곱근 : %f' % math.sqrt(3) )   # 하나의 매개변수만 있으면 되는 sqrt(), 제곱근만 구할 수 있어서
print('3의 4제곱 : %f' % math.pow(3,4))
print()

# 아들이 용돈을 받는데 첫달에는 200원, 매월 이전 달의 2배씩 인상한다고 하자.
# 12개월째 되는 날은?

firstMonthMoney = 200
after12Month = firstMonthMoney*(2**11)
print('12개월 후 용돈 : {}'.format(after12Month))

after12Month = int(after12Month)
strAfter12Month = format(after12Month, ',')
print(strAfter12Month, '원')

