'''A,B = map(int,input().split())
if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')'''


A, B = map(int,input().split())
print(['><'[A<B],'=='][A==B])