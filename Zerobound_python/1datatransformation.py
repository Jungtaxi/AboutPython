num = 10
print(type(num))
num = float(num)
print(type(num))
num = str(num)
print(type(num))

print()
var1 = '' # 공백 없는 빈 문자
print(type(var1))
var1 = bool(var1)
print(var1)

print()
var2 = ' ' # 공백 있는
print(type(var2))
var2 = bool(var2)
print(var2)

print()
var1 = 'True'
var2 = 'False'
print(type(var1))
print(type(var2))

print()
var1 = bool(var1)
var2 = bool(var2)
print(var1)
print(var2)

print()
print(var1+var2)
print(type(var1+var2))