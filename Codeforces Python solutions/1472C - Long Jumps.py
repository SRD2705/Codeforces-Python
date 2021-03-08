for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    res = [0]*n
    tmp = 0
    for i in range(n-1,-1,-1):
        res[i] = li[i]
        tmp = i+li[i]
        if tmp<n:
            res[i] += res[tmp]
    print(max(res))