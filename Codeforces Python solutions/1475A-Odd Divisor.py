# 1475A-Odd Divisor

import math
def Log2(x):
    if x == 0:
        return False
    return (math.log10(x) / math.log10(2))


def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

for _ in range(int(input())):
    n = int(input())
    if isPowerOfTwo(n) == True:
        print("NO")
    else:
        print("YES")