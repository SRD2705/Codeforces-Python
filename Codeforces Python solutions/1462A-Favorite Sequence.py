# 1462A - Favorite Sequence
for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li1 = []
    i = 0
    j = len(li)-1
    while i < j:
        li1.append(li[i])
        li1.append(li[j])
        i += 1
        j -= 1
    if n % 2 != 0:
        li1.append(li[n//2])
    print(*li1)