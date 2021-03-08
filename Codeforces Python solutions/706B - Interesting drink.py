
def binsrch(k,n,li):
    l = 0
    r = n-1
    mid = 0
    res = 0
    st = False
    while l <= r:
        mid = (r+l) // 2
        if li[mid] <= k:
            l = mid + 1
            res = mid
            st = True
        elif li[mid] > k:
            r = mid - 1
    if st == True:
        res += 1
    return res

n = int(input())
li = list(map(int, input().split()))
li.sort()
q = int(input())
for i in range(q):
    k = int(input())
    res = binsrch(k,n,li)
    print(res)