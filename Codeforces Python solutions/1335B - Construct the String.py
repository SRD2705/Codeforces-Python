# 1335B - Construct the String

for _ in range(int(input())):
    n,a,b = map(int, input().split())
    li = []
    val = 97
    for i in range(b):
        li.append(chr(val))
        val += 1
    end = val
    val = 97
    tmp = n // b
    res = li * tmp
    while len(res) != n:
        if val == end:
            val = 97
            res.append(chr(val))
            val += 1
        else:
            res.append(chr(val))
            val += 1
    print(*res, sep = '')