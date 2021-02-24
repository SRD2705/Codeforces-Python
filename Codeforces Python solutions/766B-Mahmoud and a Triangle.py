# 766B-Mahmoud and a Triangle

n = int(input())
li = list(map(int, input().split()))
res = 0
li.sort()
if n < 3:
    print("NO")
else:
    for i in range(n-2):
        if li[i] + li[i+1] > li[i+2]:
            res = 1
            break
    if res == 1:
        print("YES")
    else:
        print("NO")