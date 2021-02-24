# 313A - Ilya and Bank Account
n = int(input())
if n >= 0:
    print(n)
else:
    tmp = str(abs(n))
    s1 = ''
    li = list(tmp)
    li.pop()
    for i in li:
        s1 += i
    tmp1 = int(s1)
    li = list(tmp)
    s2 = ''
    li.pop(-2)
    for i in li:
        s2 += i
    tmp2 = int(s2)
    if tmp1 > tmp2:
        print(-tmp2)
    else:
        print(-tmp1)