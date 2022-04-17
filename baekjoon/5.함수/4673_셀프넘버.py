def d(n):
    d_list = list(map(int,str(n)))
    return ( sum(d_list) + n )

n=1
my_list = []
while n < 10000:
    if n not in my_list:
        print(n)
        my_list.append(n)
    if d(n) < 10000:
        my_list.append(d(n))
    n += 1

# def d(n):
#     for i in str(n):
#         n += int(i)
#     return n

# numbers = set(range(1,10001))
# remove_numbers = set()

# for num in numbers:
#     remove_numbers.add(d(num))

# self_numbers = numbers - remove_numbers
# for i in sorted(self_numbers):
#     print(i)


# def d(n):
#     for i in str(n):
#         n += int(i)
#     return n

# arr = [True for i in range(0,10001)]  # 0번 인덱스부터 10000까지 True로 넣고, (헷깔리니깐 인덱스 0도 넣었어)
# for i in range(1,10001):              # i 1부터 10000까지
#     num = d(i)                        # num은 d(i)
#     if num <= 10000 :                 # 리스트 인덱스 10000 넘는거 방지
#         arr[num] = False              # d(n)에 해당하는 인덱스 들에 False 값 대입
# for i in range(1,10001):              # 0번 인덱스는 알바 아니야
#     if arr[i] :
#         print(i)