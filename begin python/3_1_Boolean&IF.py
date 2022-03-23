# 논리 연산자 not, and, or
x = 10
under_20 = x < 20
print("under_20 : ", under_20)
print("not under_20 : ", not under_20)

# 치킨 그리고 쓰레기 가져와! 하면 쓰레기 싫어서 False
# 치킨 또는 쓰레기 가져와! 하면 치킨만 가져가도 되니깐 True
print(True and False)
print(True or False)


# 양수 인지 음수인지
x = int(input("정수를 입력하세요> "))
if x>0 :
    print("양수입니다!")
elif x<0 :
    print("음수입니다!")
else :
    print("0 입니다!")
print()

# 날짜 시간 물어보는
import datetime
now = datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour < 12 :
    print("지금은 오전 입니다")
else :
    print("지금은 {}시로 오후 입니다.".format(now.hour))

if 3<= now.month <= 5 :
    print("지금은 {}달로 봄입니다".format(now.month))
if 6<= now.month <= 8 :
    print("지금은 {}달로 여름입니다.".format(now.month))

# 조건식에서 불 값을 어떤식으로 만들까
# 끝자리로 짝수와 홀수 구분
number = input("정수를 입력하세요 : ")
last_character = number[-1]
last_num = int(last_character)
if last_num % 2 == 0 :
    print("짝수입니다!")
if last_num == 1 \
    or last_num == 3 \
    or last_num == 5 \
    or last_num == 7 \
    or last_num == 9 :
    print("{}은 홀수입니다!".format(last_num))

