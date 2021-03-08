for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    s = list(set(li))
    if len(s) == n:
        print("NO")
    else:
        print("YES")