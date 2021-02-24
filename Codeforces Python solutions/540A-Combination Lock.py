# 540A-Combination Lock
n = int(input())
li = list(map(int,input()))
li1 = list(map(int, input()))
res = 0
for i in range(n):
    if li[i] > li1[i]:
       res += min((li[i]-li1[i]),abs(li[i]-(10+li1[i])))
    elif li[i] < li1[i]:
        res += min((li1[i]-li[i]),abs(li1[i]-(10+li[i])))
print(res)