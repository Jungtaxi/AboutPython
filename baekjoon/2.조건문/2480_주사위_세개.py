# 잘못된 답안
# a, b, c = map(int, input().split())
# if a==b==c :
#     print(10000+1000*a)
# elif a!=b!=c:
#     print(max(a,b,c)*100)
# else :
#     print(1000+100*a) if a==b or a==c \
#     else print(1000+100*b)

#숏코딩
# a,b,c=sorted(map(int,input().split()))
# print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)



a, b, c = map(int, input().split())
if a==b==c :
    print(10000+1000*a)
elif not(a==b or b==c or a==c):
    print(max(a,b,c)*100)
else :
    print(1000+100*a) if a==b or a==c \
    else print(1000+100*b)


