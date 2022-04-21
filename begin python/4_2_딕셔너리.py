#키는 중복되지 않는다.
a = {1:'a', 1:'b'}  # 1:'a'는 지워진다.


dic = {'name':'망고',
'type': '당절임',
'ingredient':['망고','설탕','메타중아황산나트륨','치자 황색소'],
'origin':'필리핀'
}

#딕셔너리 요소에 접근하기
dic['name']

#딕셔너리 요소 값 변경하기
dic['name'] = '7D 건조 망고'

#딕셔너리 요소 추가
dic['price'] = '5000'

#딕셔너리 요소 값 제거하기
del dic['ingredient']

#존재하지 않는 키에 접근하면
dic['key']

#key 리스트 만들기
dic.keys()
type(dic.keys())
list(dic.keys())

#value 리스트 만들기
dic.values()
type(dic.values())
list(dic.values())

#key와 value 쌍 얻기
dic.items()
type(dic.items())
list(dic.items())

#key로 value 값 얻기
dic.get('name')
dic['name']

dic.get('없는 키')        #None 반환
dic['없는 키']            #KeyError 발생

dic.get('없는 키', '키가 없는데요') #디폴트 값 '키가 없는데요' 반환

key = input()
if dic.get(key):
    print(dic.get(key))
else :
    print('존재하지 않는 키에 접근하고 있습니다.')

# in 키워드
key = input()
if key in dic :
    print(dic.get(key))
else :
    print('존재하지 않는 키에 접근하고 있습니다.')