#리스트 내포
a = [i*i for i in range(0,20,2)]
print(a,'\n')

#삼항조건문 이용한 comprehension
fruitBasket = ['사과','바나나','오렌지','체리','초콜릿']
fruit = [fruit for fruit in fruitBasket if fruit != '초콜릿']
print(fruit,'\n')

#다른 예시
a = ['apple','banana','orange']
b = [x for x in a if 'na' in x]
print(b,'\n')


#zip()
a = [1,2,3]
b = ['a','b','c']
c = zip(a,b)
d = list(c)
print(d)
