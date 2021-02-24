# 1453A-Cancel the Trains
for _ in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li1 = list(map(int,input().split()))
    res = list(set(li).intersection(set(li1)))
    print(len(res))