n = int(input())
tmp = 0
res = []
i = 0
while n > tmp:
    i += 1
    tmp += i
    if tmp > n:
        tmp -= i
        break
    else:
        res.append(i)
tmp = tmp - res.pop()
res.append(n-tmp)
print(len(res))
print(*res)