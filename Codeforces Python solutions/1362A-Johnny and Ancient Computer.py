# 1362A-Johnny and Ancient Computer
for _ in range(int(input())):
    a,b = map(int, input().split())
    res = -1
    if a>b:
        a,b = b,a
    while a < b:
        if b%8 == 0 and b//8 >= a:
            b = b//8
        elif b%4 == 0 and b//4 >= a:
            b = b//4
        elif b%2 == 0 and b//2 >= a:
            b = b//2
        else:
            break
        res += 1
    if a==b:
        print(res+1)
    else:
        print(-1)