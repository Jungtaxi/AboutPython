N = int(input())

big = N//5
while True :
    residue = N-5*big
    if residue%3 == 0 :
        small = residue // 3 
        result = big + small
        break
    big -= 1
    if big <0 :
        result = -1
        break

print(result)
