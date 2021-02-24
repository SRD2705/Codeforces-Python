# 1481B-New Colony
for _ in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    pos = -2
    if len(li) == 1:
        pos = -1
    for i in range(k):
        for j in range(n-1):
            if li[j] < li[j+1]:
                li[j] += 1
                pos = j+1
                break
            elif li[j] >= li[j+1]:
                if j+1 == n-1:
                    pos = -1
                    break
        if pos == -1:
            break
    print(pos)