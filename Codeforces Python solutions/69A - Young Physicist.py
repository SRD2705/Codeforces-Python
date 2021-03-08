tmp1 = 0
tmp2 = 0
tmp3 = 0
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    tmp1 += a
    tmp2 += b
    tmp3 += c
if tmp1 == 0 and tmp2 == 0 and tmp3 == 0:
    print("YES")
else:
    print("NO")