word = input()
a = word.count('c=')
b = word.count('c-')
c =word.count('dz=')
d = word.count('d-')
e = word.count('lj')
f = word.count('nj')
g =word.count('s=')
h = word.count('z=')-c

print(len(word)-a-b-2*c-d-e-f-g-h)

word = input()
print(len(word)-sum(word.count(i) for i in ['=','-','lj','nj','dz=']))
