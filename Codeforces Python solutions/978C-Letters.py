# 978C-Letters

d = []
n, m = map(int, input().split())
li = list(map(int, input().split()))
tmp = 0
for i in range(n):
    tmp += li[i]
    d.append(tmp)
li1 = list(map(int, input().split()))
j = 0
for i in range(m):
    while j < n:
        if li1[i] <= d[j]:
            if j == 0:
                print(j+1,li1[i])
                break
            else:
                print(j+1,abs(li1[i]-d[j-1]))
                break
        else:
            j += 1