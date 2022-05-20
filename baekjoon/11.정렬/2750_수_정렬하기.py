N = int(input())
mylist = []
for _ in range(N):
    mylist.append(int(input()))

# # 버블 정렬 ver.
# for i in range(len(mylist)-1):
#     for j in range(i+1,len(mylist)):
#         if mylist[i] > mylist[j] :
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# for i in mylist:
#     print(i)

# if len(mylist)==1:                                      # 요소가 하나일 때는 삽입정렬을 쓸 수 없다.
#     print(mylist[0])
# else:
#     # 삽입 정렬 ver.
#     for i in range(1,len(mylist)):                      # 0번째 요소는 정렬 되어있음
#         for j in range(i,0,-1):
#             if mylist[j-1]>mylist[j]:
#                     mylist[j-1],mylist[j] = mylist[j],mylist[j-1]
#     for i in mylist:
#         print(i)


# Selection sort
for i in range(len(mylist)-1):
    minitem = mylist[i]
    minindex = i
    for j in range(i+1,len(mylist)):
        if mylist[j] < minitem:
            minitem = mylist[j]
            mylist[minindex],mylist[j] = mylist[j],mylist[minindex]
for i in mylist:
    print(i)