def solution(priorities, location):
    selection, count = sorted(priorities, reverse=True), 0
    answer = 0
    while True:
        for i, _ in enumerate(priorities):
            if _ == selection[count] :
                count += 1
                answer += 1
                if i == location:
                    break
        else :
            continue # for loop가 break으로 끊기지 않고 빠져나왔으면 실행
        break # for loop가 break으로 빠져나왔을 경우 실행
    return answer
print(solution([2,1,3,2],2))