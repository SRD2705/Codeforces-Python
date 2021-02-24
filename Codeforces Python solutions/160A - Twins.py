# 160A - Twins
n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
s = 0
res = 0
i = 0
for i in range(n):
    s += li[i]
    if s > sum(li[i+1:]):
        res = 1
        break
print(i+1)