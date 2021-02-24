# 158B-Taxi
n = int(input())
li = list(map(int, input().split()))
o,t,th,f = map(li.count, range(1,5))
res = 0
res += f
res += th
res += t // 2
if t % 2 != 0:
    res+= 1
if th<o:
    o -= th
    if t % 2 != 0:
        o -= 2
    if o>0:
        res+= o//4
        if o%4 != 0:
            res+=1
print(res)