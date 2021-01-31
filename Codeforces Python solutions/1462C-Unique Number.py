# 1462C - Unique Number
for _ in range(int(input())):
    n = int(input())
    s = 0
    d = 9
    li = []
    while s < n and d > 0:
        li.append(min(n-s, d))
        s += d
        d -= 1
    if s < n:
        print(-1)
    else:
        li.reverse()
        print(*li, sep='')