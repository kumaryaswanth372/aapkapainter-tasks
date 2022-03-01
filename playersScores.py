#lst = [1,2]
lst = [1,2,3,2,1]
p1 = 0
p2 = 0

def remove_odd(lst):
    score = 0
    count = 0
    for i in lst:
        #print(i)
        if i%2 == 0:
            score += i
            count += 1
        else:
            score += i
            count += 1
            break
    del lst[0:count]
    return score

for i in range(0,10):
    if lst != []:
        x = remove_odd(lst)
        p1 += x
        x1 = remove_odd(lst)
        p2 += x1

print('P1:', p1)
print('P2:', p2)