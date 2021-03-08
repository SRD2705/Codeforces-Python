import math
n = input()
if n == '0':
    print(0)
else:
    k = int(n,2)
    # print(k)
    i = 0
    res = 0
    while(1):
        if 4**i > k:
            break
        elif 4**i < k:
            i += 1
            res += 1
        else:
            break
    print(res)