list_a = [273,32,103,"문자열",True,False]
print(len(list_a))
print(list_a[0]) # 첫번째 인덱스(0)의 요소
print(list_a[5]) # 마지막 인덱스(5)의 요소
print(list_a[1:3]) #인덱스 1과 2의 요소가 튀어나온다.
print(list_a[1:-1]) #인덱스 1부터 4까지의 부분리스트
list_a[0] ='변경' # 0번째 요소가 바뀐다.
print(list_a)
print(list_a[-6])
print(list_a[3][1:3])
print()

list_a = [273,32,103,"문자열",True,False,[2,3,5]]
print(list_a[3][0])
print(list_a[3][1])
print(list_a[-1])
print(list_a[-1][1])
print()

list_a = [1,2,3]
print(list_a+list_a)
print(list_a*3)
print(len(list_a))