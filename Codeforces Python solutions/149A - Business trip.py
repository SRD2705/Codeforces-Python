n = int(input())
li = list(map(int,input().split()))
res = 0
if n == 0:
    print(0)
else:
    li.sort(reverse=True)
    for i in li:
        n -= i
        res += 1
        if n <= 0:
            break
    if n <= 0:
        print(res)
    else:
        print(-1)