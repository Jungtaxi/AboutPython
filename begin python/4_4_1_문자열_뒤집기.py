#slice 사용
string = 'Hello my world!'
reversed_string = string[::-1]
print(reversed_string)

#reversed() 사용
''.join(reversed(string))

#reverse() 쓰고 싶으면
string_list = list(string)
string_list.reverse()
''.join(string_list)

#for loop
reversed_string = ''
for i in string:
    reversed_string = i + reversed_string
