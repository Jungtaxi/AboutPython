print('계절 : 봄, 여름, 가을, 겨울')
seasonSTr = input('계절 입력 : ')

if seasonSTr == '봄':
    print('{} : {}'.format('봄', 'Spring'))
elif seasonSTr == '여름':
    print('{} : {}'.format('여름','Summer'))
elif seasonSTr == '가을':
    print('{} : {}'.format('가을', 'Fall'))
elif seasonSTr == '겨울':
    print('{} : {}'.format('겨울', 'Winter'))
else :
    print('검색이 나오지 않습니다.')


print('1.카페라떼(3.5) \t 2.에스프레소(3.0) \t 3.아메리카노(2.0) \t 4.곡물라떼(4.0)\
 \t 5. 밀크티(4.3)')
userMenu = input('메뉴 선택 : ')
print('-'*20)
if userMenu == '1' :
    print('메뉴 : 카페라떼')
    print(format(3500, ','), '원')
elif userMenu == '2' :
    print('메뉴 : 에스프레소')
    print(format(3000, ','), '원')
elif userMenu == '3' :
    print('메뉴 : 아메리카노')
    print(format(2000, ','), '원')
elif userMenu == '4' :
    print('메뉴 : 곡물라떼')
    print(format(4000, ','), '원')
elif userMenu == '5' :
    print('메뉴 : 밀크티')
    print(format(4300, ','), '원')
else :
    print('알맞는 메뉴를 선택해주세요 (1~5)')
print('-'*20)