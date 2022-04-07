#구구단
for i in range(1,10) :
    for j in range(1,10) :
        print('{}*{}={}'.format(i,j,j*i))

#메일보내기
players = ['박찬호','박세리','박지성','김연경','이승엽']
for player in players :
    print('{}선수에게 메일 발송 !!'.format(player))