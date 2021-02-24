# 1006C - Three Parts of the Array
n = int(input())
li = list(map(int, input().split()))
i = 0
j = n-1
s1 = li[0]
s2 = li[n-1]
res = 0
while i < j:
    if s1 > s2:
        j -= 1
        s2 += li[j]
    elif s1 < s2:
        i += 1
        s1 += li[i]
    else:
        res = s1
        i += 1
        s1 += li[i]
print(res)