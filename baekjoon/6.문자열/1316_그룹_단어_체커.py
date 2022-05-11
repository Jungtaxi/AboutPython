T = int(input())
count = 0
for _ in range(T):
    s = input()    
    if len(s)==1:
        count += 1
        continue
    elif len(s) == 2:
        count += 1
        continue
    for idx, item in enumerate(s[:-1]):
        if item != s[idx+1]:
            if s.count(item,idx+1) > 0:
                break
    else: count += 1
print(count)