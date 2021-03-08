for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    m = int(input())
    li1 = list(map(int, input().split()))
    mx_li = 0
    mx_li1 = 0
    tmp = 0
    tmp1 = 0
    for i in range(n):
        tmp += li[i]
        mx_li = max(tmp, mx_li)
    for j in range(m):
        tmp1 += li1[j]
        mx_li1 = max(tmp1,mx_li1)
    # print(mx_li1)
    print(mx_li + mx_li1)