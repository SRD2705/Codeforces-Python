# 1475B-New Year's Number

for _ in range(int(input())):
    n = int(input())
    cnt21 = n % 2020
    cnt20 = (n-cnt21) / 2020 - cnt21
    if cnt20>=0 and (cnt21*2021)+(cnt20*2020) == n:
        print("YES")
    else:
        print("NO")