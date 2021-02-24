# 1481A-Space Navigation

for _ in range(int(input())):
    r = 0
    u = 0
    d = 0
    l = 0
    x, y = map(int,input().split())
    li = list(input())
    res = 0
    if x > 0:
        r = x
    elif x < 0:
        l = abs(x)
    if y > 0:
        u = y
    elif y < 0:
        d = abs(y)
    for i in li:
        if i == 'R':
            if r != 0:
                r -= 1
        elif i == "U":
            if u != 0:
                u -= 1
        elif i == "D":
            if d != 0:
                d -= 1
        elif i == 'L':
            if l != 0:
                l -= 1
        if r == 0 and u == 0 and d == 0 and l == 0:
            res = 1
            break
    if res == 0:
        print("NO")
    elif res == 1:
        print("YES")