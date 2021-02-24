# 460A - Vasya and Socks
n, m = map(int, input().split())
if n < m:
    print(n)
elif m > n//2:
    print(n+1)
else:
    res = n
    while n > 0:
        tmp = n//m
        res += tmp
        if n%m == 0 and tmp == 1 or m > n:
            break
        tmp += n%m
        n = tmp
    print(res)