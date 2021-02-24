# 1487A - Arena
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    tmp = li[0]
    res = 0
    for i in li:
        if i > tmp:
            res += 1
    print(res)