import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
for i in range(1,N+1) :
    output('%d\n' % i)

# print(*range(1,int(input())+1), sep='\n')

# def foo(x,y,z):
#     print("x=" + str(x))
#     print("y=" + str(y))
#     print("z=" + str(z))
# mylist = [1,2,3]
# foo(*mylist)
# mydict = {'x':1,'y':2,'z':3}
# foo(**mydict)