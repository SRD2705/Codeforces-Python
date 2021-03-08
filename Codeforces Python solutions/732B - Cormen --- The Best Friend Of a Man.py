n,k = map(int, input().split())
li = list(map(int, input().split()))
res = 0
for i in range(1,n):
    if li[i-1] + li[i] < k:
        res += k -(li[i-1] + li[i])
        li[i] = k - li[i-1]
print(res)
print(*li)