def quick_sort(datas,start,end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while (left <= right):
        while (left<=end) and (datas[left]<=datas[pivot]):  #끝까지 가면 len(datas) 까지 간다.
            left+=1
        while (right>start) and (datas[right]>=datas[pivot]): #끝까지 가면 0 까지 간다.
            right-=1
        if left > right :
            datas[right], datas[pivot] = datas[pivot], datas[right]
            print(datas)
        else:
            datas[right], datas[left] = datas[left], datas[right]
            datas
    quick_sort(datas,start,right-1)
    quick_sort(datas,right+1,end)

N = int(input())
mylist = [input() for _ in range(N)]
quick_sort(mylist,0,len(mylist)-1)
[print(i) for i in mylist]