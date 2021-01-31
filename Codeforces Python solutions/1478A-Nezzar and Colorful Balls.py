# 1478A-Nezzar and Colorful Balls

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    res = 1
    tmp = 1
    for i in range(1,n):
        if li[i-1] == li[i]:
            tmp += 1
        else:
            res = max(res,tmp)
            tmp = 1
    res = max(res,tmp)
    print(res)