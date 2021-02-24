# 1352C - K-th Not Divisible by n
for _ in range(int(input())):
    n, k = map(int, input().split())
    res = 0
    while(1):
        tmp = k//n-res
        if tmp == 0:
            break
        k += tmp
        res += tmp
    print(k)