# 580A - Kefa and First Steps
n = int(input())
li = list(map(int, input().split()))
c = 0
tmp = 0
res = 0
for i in range(n):
    if li[i] >= tmp:
        c += 1
        tmp = li[i]
        res = max(res, c)
    else:
        c = 1
        tmp = li[i]
print(res)
