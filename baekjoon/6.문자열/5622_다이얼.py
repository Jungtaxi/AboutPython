dir = '22233344455566677778889999'
word = input()
ans = 0
for i in word :
    ans += int(dir[ord(i)-65])+1
print(ans)