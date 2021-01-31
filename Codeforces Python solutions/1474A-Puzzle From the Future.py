# 1474A-Puzzle From the Future
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input()))
    res = []
    ans = []
    if li[0] == 0:
        res.append(1)
        ans.append(1)
    else:
        res.append(2)
        ans.append(1)
    for i in range(1, n):
        if li[i] == 1 and res[i-1] == 1:
            res.append(2)
            ans.append(1)
        elif li[i] == 0 and res[i-1] == 1:
            res.append(0)
            ans.append(0)
        elif li[i] == 1 and res[i-1] == 2:
            res.append(1)
            ans.append(0)
        elif li[i] == 0 and res[i-1] == 2:
            res.append(1)
            ans.append(1)
        elif li[i] == 0 and res[i-1] == 0:
            res.append(1)
            ans.append(1)
        elif li[i] == 1 and res[i-1] == 0:
            res.append(2)
            ans.append(1)
    print(*ans, sep='')