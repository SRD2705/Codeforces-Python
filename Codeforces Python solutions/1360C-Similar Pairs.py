# 1360C-Similar Pairs

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    reso = []
    rese = []
    res = 0
    for i in li:
        if i%2 == 0:
            rese.append(i)
        else:
            reso.append(i)
    if len(reso)%2 == 0 and len(rese)%2 == 0:
        res = 1
        print("YES")
    else:
        o =len(reso)
        e = len(rese)
        m = 0
        k = 0
        while m < o and k < e:
            if abs(rese[k] - reso[m]) == 1:
                res = 1
                break
            elif reso[m] > rese[k]:
                k += 1
            else:
                m += 1
        if res == 1:
            print("YES")
        else:
            print("NO")