# 문자열의 format() 함수
print("{}".format(10))
print("{} {}".format(10, "이 문자열이 되는 겁니다."))
a = "{} {}".format(31, 32.3)
print(type(a))
print(a)
b = "파이썬 열공해서 첫 연봉 {}만원 만들겠다.".format(5000)
print(b)
# {} 보다 매개변수가 많으면 남는 매개변수는 버려지기 때문에 문제가 되지 않지만
# {} 가 매개변수 보다 더 많으면 Index Error 가 발생합니다.
print()

# format()의 다양한 기능
# 정수
output_a = "{:d}".format(52)
print(type(output_a))
print(output_a) 

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)   # 5칸 안에 출력
print(output_b)

# 빈칸을 0으로 채우기
output_c = "{:05d}".format(52)
print(output_c)
output_d = "{:05d}".format(-52)
print(output_d)

# 기호 붙여 출력하기
output_e = "{:+d}".format(52)
output_f = "{:+d}".format(-53)
print(output_e)
print(output_f)

# 기호 부분 띄워서 출력
output_g = "{: d}".format(42)
output_h = "{: d}".format(-32)
print(output_g)
print(output_h)
print()

# 위에 배운거 조합 해보자
output_I = "{:+5d}".format(53)
output_J = "{:+5d}".format(-53)
output_K = "{:=+5d}".format(53)        # 기호를 앞으로 밀기
output_L = "{:=+5d}".format(-53)       # 기호를 앞으로 밀기
output_M = "{:+05d}".format(53)        # 0으로 채우기
output_N = "{:+05d}".format(-53)       # 0으로 채우기

print(output_I)
print(output_J)
print(output_K)
print(output_L)
print(output_M)
print(output_N)
print(type(output_N))
print()

# float 자료형으로 해보기
a = "{:f}".format(52.323)
b = "{:15f}".format(53.232)
c = "{:+15f}".format(53.232)
e = "{:=15f}".format(53.232)
d = "{:+015f}".format(53.232)
f = "{:=+15f}".format(53.232)
print(a)
print(b)
print(c)
print(e)
print(d)
print(f)
print()

# float 에서 소숫점 자리 지정하기
a = "{:15.2f}".format(53.232)
print(a)
print()

# float 에서 의미없는 소숫점 제거하기
a = "{:g}".format(32.32000)
print(a)
print()

# 대소문자 바꾸기
a = "hI nice to meet you!"
print(a.upper(), "upper() 써보자")
print(a.lower(), "lower() 써보자")

# 공백 지우기 trim 또는 strip을 한다고 합니다.
a = """
        공백 지우기 해보자
"""
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(a)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(a.lstrip())
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(a.rstrip())
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(a.strip())
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print()



'''
isalnum() : 알파벳 또는 숫자로만 구성되어 있는지
isalpha() : 알파벳으로만 구성되어 있는지
isidentifier() : 문자열이 식별자로 사용할 수 있는 것인지
isdecimal() : 문자열이 정수형태인지 확인
isdigit() : 문자열이 숫자로 인식될 수 있는 것인지
isspace() : 문자열이 공백으로만 구성되어 있는지
islower() : 문자열이 소문자로만 구성되어 있는지
isupper() : 문자열이 대문자로만 구성되어 있는지
'''
print("TrainA10".isalnum())
print()

# 문자열 찾기 ( 인덱스 구하기 )
a = "안녕 안녕 하세요"
print(a.find("안녕")) # 왼쪽에서부터 찾았을 때
print(a.rfind("안녕")) # 오른쪽에서부터 찾았을 때
print()

# in 연산자
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

# 문자열 자르기
a = "10 20 30 40 50".split(" ")
print(a)