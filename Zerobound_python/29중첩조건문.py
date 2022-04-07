exampleScore = int(input('시험 점수 입력 : '))
if exampleScore<60 :
    print('재시험 대상')
else :
    if exampleScore >= 90 :
        print('A')
    elif exampleScore >= 80 :
        print('B')
    elif exampleScore >= 70 :
        print('C')
    elif exampleScore >= 60 :
        print('D')

# 실습
userSelect = input('출퇴근 대상자 인가요? Y/N \n :')
if userSelect == 'Y' :
    print('교통수단을 선택해 주세요.')
    trans = int(input(' 1.도보,자전거\t2.버스,지하철\t3.자가용\n :'))
    if trans == 1 :
        print('세금 감면 5%')
    elif trans == 2 :
        print('세금 감면 3%')
    elif trans == 3 :
        print('추가 세금 1%')
    else :
        print('올바른 선택지를 골라주세요.')
elif userSelect == 'N' :
    print('세금 변동없습니다.')
else :
    print('잘못 선택했습니다.')