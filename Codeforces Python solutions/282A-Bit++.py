# 282A-Bit++
n = int(input())
res = 0
for _ in range(n):
    li = list(input())
    for i in li:
        if i == '+':
            res += 1
            break
        elif i == '-':
            res -= 1
            break
print(res)