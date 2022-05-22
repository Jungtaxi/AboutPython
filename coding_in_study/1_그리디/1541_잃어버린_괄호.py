cal = input()
sign ='+'
signidx = 0
minus_num = 0
result = 0

for i in range(len(cal)+1):
    if i != len(cal) and cal[i] == '-':                           # - 를 만났을 때
        if i != 0 :                             # 인덱스 0이 - 가 아니라면 앞에 양수가 있는것이므로
            result += int(cal[signidx:i])       # result에 앞의 양수를 더한다.
        signidx = i                             # - 의 위치를 기록

        while i < len(cal):                     # - 뒤의 모든 값들을 다 더하면 된다.
            i += 1                              # - 뒤의 값들 보고 싶으므로 i를 뒤로 한칸 옮긴다.

            # 참고로 파이썬은 or 비교 연산에서 앞에게 True면 뒤에것을 더이상 안읽는다. 그래서 index erro 안난다.
            if i == len(cal) or cal[i] == '-' or cal[i] =='+':  # 문자열의 끝에 오거나 또는 부호를 만나면
                minus_num += int(cal[signidx+1:i])              # 숫자를 찾아내 더한다. (부호 사이의 값이 숫자)
                signidx = i                                     # 다시 부호를 기록한다.
        break

    elif i == len(cal) or cal[i] == '+' :      # -를 만나기 전, +연산으로 이루어진 값들은 다 더해버린다.
        result += int(cal[signidx:i])
        signidx = i

result -= minus_num
print(result)