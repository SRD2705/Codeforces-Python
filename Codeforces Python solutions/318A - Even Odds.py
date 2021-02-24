# 318A - Even Odds
n, k = map(int, input().split())
e = n // 2
o = n-e
if k > o:
    tmp = k - o
    print(tmp*2)
else:
    print(k + (k-1))