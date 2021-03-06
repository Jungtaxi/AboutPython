
# 데이터 타입에 대해 알아봅니다.
print(type("안녕하세요"))
print(type(2), type(2.0))
print(type(True))

# String에 대해 배워 봅시다.

# ""를 출력해봅시다.
print(" \"\"를 출력 ")            # 이스케이프 문자 사용
print(' "" 이렇게도 출력 가능 ')  # 작은 따옴표, 큰 따옴표 혼용 

# 이스케이프 문자를 알아봅시다.
print(" 이렇게 하면 \n 줄바꿈 ")
print(" 이렇게 하면 \t 탭 입니다.")

# 여러줄 적기는 이렇게하면 좀더 편합니다
print("""
첫째줄
둘째줄
""")
print("""\
역슬래시 넣으면
앞 뒤 줄바꿈 안해요\
""")
print()

#문자열 연산자라는걸 해봅시다.
print("안녕"+"하세요!") # 단 이때 문자열 연결 연산자(+) 는 문자열 끼리만 쓸 수 있습니다.
print("반복"*3) #문자열*숫자 꼴 입니다.(순서 상관 무) 문자열 반복 연산자라고 합니다.
print()
print("문자 선택 연산자를 알아봅시다.")
a = "문자 선택 연산자를 알아봅시다."
print(a[0])
print(a[-1])
print(a[11])
# 파이썬은 문자열 인덱스가 0부터 시작합니다.
print()

# 문자열 범위 선택 연산자(슬라이싱) : [:] 을 알아봅시다.
print(a[1:10]) # 이러면 인덱스 1부터 10까지만 나옵니다.
print(a[5:]) #이러면 인덱스 5부터 끝까지 나옵니다.
# 인덱스 범위를 넘어서는 문자를 택하면 index out of range 오류가 발생합니다.
print()

# 문자열의 길이 구하기
print(len(a))

