N = int(input())
mylist = [input().strip() for _ in range(N)]

# 병합 정렬
def merge1(datas):
    if len(datas)==1:
        return datas
    mid = len(datas)//2
    left = merge1(datas[:mid])
    right = merge1(datas[mid:])
    mergelist = []
    i, j = 0,0
    while True:
        if i == len(left):
            mergelist += right[j:]
            break
        elif j == len(right):
            mergelist += left[i:]
            break
        elif left[i]<right[j]:
            mergelist.append(left[i])
            i += 1
        else : 
            mergelist.append(right[j])
            j += 1
    return mergelist

[print(i) for i in merge1(mylist)]