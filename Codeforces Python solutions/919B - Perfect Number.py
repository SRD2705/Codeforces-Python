def cal(x):
    ans = 0
    while (x):
        ans += x % 10
        x = x // 10
    return ans

n = int(input())
res = 19
n -= 1
while(n):
    res += 9
    if cal(res) == 10:
        n -= 1
print(res)