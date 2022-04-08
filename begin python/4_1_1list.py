list_a = [1,2,3]
print(list_a)

# append()
list_a.append(4)
print(list_a)

# insert()
list_a.insert(0,10)
print(list_a)

# extend()
list_a.extend([7,7,7])
print(list_a)

list_a.extend('어디보자')
print(list_a)

list_a.extend((2,3,4))
print(list_a)
print()

#인덱스로 제거하기
list_a = [1,2,3,4,5,6,7,8,9,10]

del list_a[1] # 리스트의 1번째 요소 제거
print(list_a)

print(list_a.pop()) # 마지막 요소 제거 및 return
print(list_a)

print(list_a.pop(3)) # 세번째 요소 제거 및 return
print(list_a)
print()

list_a= [0,1,2,3,4,5,6,7,8,9,10]
del list_a[5:7] # 5번째 요소부터 6번째 요소까지 제거
print(list_a)

list_a= [0,1,2,3,4,5,6,7,8,9,10]
del list_a[:3] # 3 기준 왼쪽꺼 다 제거 (3 불포함)
print(list_a)

list_a= [0,1,2,3,4,5,6,7,8,9,10]
del list_a[3:] # 3 기준 오른쪽 다 제거 (3 포함)
print(list_a)

list_a= [0,1,2,3,4,5,6,7,8,9,10]
del list_a[3:-1] # 3 기준 오른쪽 다 제거 (3 포함)
print(list_a)
print()

list_b = [1,2,1,2]
list_b.remove(2) # 가장 처음 발견된 값 2 제거
print(list_b)

list_b.clear() # 모두 제거
print(list_b)