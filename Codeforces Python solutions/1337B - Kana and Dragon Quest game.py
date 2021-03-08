for _ in range(int(input())):
    x,v,l = map(int, input().split())
    if x > 20:
        for i in range(v):
            x = x // 2
            x += 10
            if x < 21:
                break
    l = l*10
    if l >= x:
        print("YES")
    else:
        print("NO")