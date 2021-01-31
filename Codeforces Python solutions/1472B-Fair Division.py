# 1472B-Fair Division
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    o = li.count(1)
    t = li.count(2)
    if o == 0 and t % 2 == 0:
        print("YES")
    elif t == 0 and o % 2 == 0:
        print("YES")
    elif o % 2 == 0 and t % 2 == 0:
        print("YES")
    elif o%2 != 0 and t % 2 == 0 and t == o:
        print("YES")
    elif o%2 == 0 and t%2 != 0 and o > 1:
        print("YES")
    else:
        print("NO")