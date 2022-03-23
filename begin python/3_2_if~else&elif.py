number = input("숫자를 입력하세요 : ")
last_char = number[-1]
last_num = int(last_char)
if last_num % 2 == 0 :
    print("{}는 짝수입니다!".format(number))
else :
    print("{}는 홀수입니다.".format(number))

for i in range(4) :
    score = float(input("학점을 입력하세요 : "))
    if score >= 4.5 :
        print("신")
    elif score >= 4.2 :
        print("교수님의 사랑")
    elif score >= 3.5 :
        print("현 체제의 수호자")
    elif score >= 2.8 :
        print("일반인")
    elif score >= 2.3 :
        print("일탈을 꿈꾸는 소시민")
    elif score >= 1.75 :
        print("오락문화의 선구자")
    elif score >= 1.0 :
        print("불가촉천민")
    elif score >= 0.5 :
        print("자벌레")
    elif score > 0 :
        print("플랑크톤")
    else :
        print("시대를 앞서가는 혁명의 씨앗")

'''
조건문의 매개변수가 boolean 이 아니면 자동으로 boolean으로 바뀝니다.
None, 0, 0.0, 빈 컨테이너 ( "" , [] 등 )은 false 로 바뀝니다.
'''

# 아직 구현 못한 코드 ; pass
# 입력을 받아서 양수인지 음수인지 알려주는데 양수일때는 아직 구현 못했다고 합시다.
number = int(input("아직 구현 못했습니다. : "))
if number > 0 :
    # 아직 미구현 상태 입니다.
    raise NotImplementedError  # 강제로 오류 발생
else :
    pass


