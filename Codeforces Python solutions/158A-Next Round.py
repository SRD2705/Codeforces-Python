# 158A-Next Round

n, k = map(int, input().split())
li = list(map(int, input().split()))
tmp = li[k-1]
res = 0
for i in li:
    if i >= tmp and i > 0:
        res += 1
print(res)