# 1020B - Badge
n = int(input())
li = list(map(int, input().split()))
hole = [0]*n
for i in range(n):
    hole = [0] * n
    j = i
    while hole[j]<2:
        hole[j] += 1
        j = li[j] - 1
    print(j+1,end=' ')