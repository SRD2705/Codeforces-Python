# 1343A - Candies
for _ in range(int(input())):
    n = int(input())
    tmp = 3
    k = 2
    while(1):
        if n % tmp == 0:
            break
        else:
            tmp += 2**k
            k += 1
    res = n // tmp
    print(res)