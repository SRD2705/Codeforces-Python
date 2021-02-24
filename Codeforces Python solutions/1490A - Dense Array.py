# 1490A - Dense Array
def calc(mx,mn):
    tmp = 0
    while(1):
        if mx <= 2*mn:
            break
        else:
            mn = 2 * mn
            tmp += 1
    return tmp


for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    res = 0
    for i in range(1,n):
        mx = max(li[i],li[i-1])
        mn = min(li[i],li[i-1])
        if mx/mn >=2:   #condition for not dense
            res += calc(mx,mn)
    print(res)