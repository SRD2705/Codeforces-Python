# 337A - Puzzles
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
i = 0
j = n-1
tmp = 0
res = 99999999999999
while j != m:
    tmp = abs(li[i]-li[j])
    res = min(tmp,res)
    i += 1
    j += 1
print(res)