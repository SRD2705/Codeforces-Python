# 1476A-K divisible Sum
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 1:
        print(k)
    elif k == 1:
        print(1)
    elif n == k:
        print(1)
    elif n > k:
        if n%k == 0:
            print(1)
        else:
            tmp = n // k
            k = (tmp+1) * k
            print((k//n)+1)
    elif n < k:
        if k % n == 0:
            print(k//n)
        else:
            print((k//n)+1)