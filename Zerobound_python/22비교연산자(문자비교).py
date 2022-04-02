#아스키 코드를 이용한 문자 비교
char1 = 'A' # 65 
char2 = 'S' # 83

print("\'{}\' > \'{}\' : \'{}\'".format(char1, char2, char1>char2))
print("\'{}\' >= \'{}\' : \'{}\'".format(char1, char2, char1>=char2))
print("\'{}\' < \'{}\' : \'{}\'".format(char1, char2, char1<char2))
print("\'{}\' <= \'{}\' : \'{}\'".format(char1, char2, char1<=char2))
print("\'{}\' != \'{}\' : \'{}\'".format(char1, char2, char1!=char2))
print("\'{}\' == \'{}\' : \'{}\'".format(char1, char2, char1==char2))

# 문자와 아스키 코드 변환
print("'A' -> {}".format(ord('A')))        # 'A' -> 65
print("'S' -> {}".format(ord('S')))        # 'S' -> 83
print()

print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))


# 문자열 비교 : 문자열 자체만 비교 가능
str1 = 'Hello'
str2 = 'hello'

print('{} == {} : {}'.format(str1, str2, str1==str2))
print('{} != {} : {}'.format(str1, str2, str1!=str2))
print()

# 실습
# 알파벳을 입력하면 아스키 코드로 출력하는 함수를 만들어 보자
userInputAlphabet = input('알파벳 입력 : ')
print('{}의 아스키 코드는 {} 입니다.'.format(userInputAlphabet, ord(userInputAlphabet)))

# 아스키코드를 입력하면 알파벳을 출력하는 함수를 만들어 보자
userInputAscii = int(input('아스키코드 입력 : '))
print('{}의 알파벳은 {} 입니다.'.format(userInputAscii,chr(userInputAscii)))


