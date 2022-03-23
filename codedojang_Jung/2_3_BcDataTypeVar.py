pi = 3.14159265 # 변수를 선언 후 할당합니다.
print(pi,"\n") # 변수를 참조합니다.

# 복합 대입 연산자, 연산 후에 대입
number = 100
print(number)
number +=10
print(number)
number /= 10
print(number)
number *= 2
print(number)
number **=2
print(number)
number %= 3
print(number)
print()

# 문자열 복합 대입 연산자
string = "안녕하세요"
print(string)
string += "!"
print(string)
string *= 2
print(string)
print()

# 사용자 입력
string = input("인사말을 입력하세요> ")
print(string)

number = input("숫자를 입력하세요> ")
print(number)
print("number의 자료형은 ",type(number),"입니다.")
# 다음과 같이 input()은 boolean을 넣어도, 숫자를 넣어도 항상 str 입니다.

# cast를 해봅시다.
number = int(number)
print(number + 2)
float_number = input("float number 을 입력해봅시다> ")
float_number = float(float_number)
print(float_number+2)
# float을 int 로 바꾸려고 하면 valueError 가 발생함에 유의합니다.
print()

# 숫자를 문자열로 바꿀수도 있습니다.
output_a = str(52)
output_b = str(32.253)
print(output_a+output_b)