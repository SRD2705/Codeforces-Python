# 263A-Beautiful Matrix
j = 0
i = 0
res = 0
for i in range(5):
    li = list(map(int, input().split()))
    if 1 in li:
        j = li.index(1)
        res = abs(2-i)+abs(2-j)
        break
print(res)