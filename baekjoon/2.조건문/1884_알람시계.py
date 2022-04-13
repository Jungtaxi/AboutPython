'''a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)'''

H,M=map(int,input().split())
set=H*60+M-45
if set < 0 :
    new_H = 23
    new_M = set + 60
else :
    new_H, new_M = set//60, set%60
print(new_H,new_M)