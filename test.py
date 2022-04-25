input_num = int(input())
for number in range(2, input_num):
    flag = True
    for n in range(2,number):
        if number%n ==0:
            flag = False
            break
        
    if flag :
        print('{}는 소수'.format(number))
    else :
        print('{}는 합성수'.format(number))