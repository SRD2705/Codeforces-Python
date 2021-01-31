# 1474D-Cleaning

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    p = [-1] * (n + 1)
    p[0] = 0
    for i in range(n):
        p[i + 1] = a[i] - p[i]
        if p[i + 1] < 0:
            break
    if p[n] == 0:
        print('YES')
        continue
    s = 0
    for i in range(n - 1, 0, -1):
        if p[i - 1] >= 0 and a[i - 1] - s >= 0 and a[i - 1] - s == a[i] - p[i - 1]:
            print('YES')
            break
        s1 = a[i] - s
        if s1 < 0:
            print('NO')
            break
        s = s1
    else:
        print('NO')
