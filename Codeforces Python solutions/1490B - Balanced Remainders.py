# 1490B - Balanced Remainders
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    c0 = n//3
    c1 = n//3
    c2 = n//3
    res = 0
    for i in range(n):
        k = li[i] % 3
        if k == 0:
            if c0 > 0:
                c0 -= 1
            elif c1 > 0:
                c1 -= 1
                res += 1
            else:
                c2 -= 1
                res += 2
        elif k == 1:
            if c1 > 0:
                c1 -= 1
            elif c2 > 0:
                c2 -= 1
                res += 1
            else:
                c0 -= 1
                res += 2
        elif k == 2:
            if c2 > 0:
                c2 -= 1
            elif c0 > 0:
                c0 -= 1
                res += 1
            else:
                c1 -= 1
                res += 2
    print(res)