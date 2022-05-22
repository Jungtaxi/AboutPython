N = int(input())
c = 0
for num in range(1,N+1):
    if num// 100 == 0 :
        c += 1
        continue
    if num == 1000:
        break
    num_str = str(num)
    a = int(num_str[1])-int(num_str[0])
    if int(num_str[2])-int(num_str[1]) == a:
        c += 1
        continue
print(c)