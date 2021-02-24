# 1015-Points in Segments
n, m = map(int, input().split())
li = []
res = []
for i in range(n):
    x,y = map(int, input().split())
    for j in range(x,y+1):
        if j not in li:
            li.append(j)
for i in range(1,m+1):
    if i not in li:
        res.append(i)
print(len(res))
print(*res)