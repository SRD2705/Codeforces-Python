n,m = map(int, input().split())
li = list(map(int,input().split()))
li.sort()
res = 0
for i in li:
    if i < 0:
        res += abs(i)
        m -= 1
    if m == 0:
        break
print(res)