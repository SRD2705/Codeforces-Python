# 96A - Football
li = list(map(int, input()))
c = 1
res = 0
for i in range(1,len(li)):
    if li[i] != li[i-1]:
        c = 1
    else:
        c += 1
    if c >= 7:
        res = 1
        break
if res == 1:
    print("YES")
else:
    print("NO")