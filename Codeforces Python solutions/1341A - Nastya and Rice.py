for _ in range(int(input())):
    n,a,b,c,d = map(int, input().split())
    minwt = c-d
    maxwt = c+d
    minr = n*(a-b)
    maxr = n*(a+b)
    if maxr < minwt or minr > maxwt:
        print("No")
    else:
        print("Yes")
