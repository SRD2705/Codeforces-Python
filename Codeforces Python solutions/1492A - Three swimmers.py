# 1492A - Three swimmers
for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
    if p % a == 0 or p % b == 0 or p % c == 0:
        print(0)
    else:
        res = min(abs(a - p%a),abs(b - p%b), abs(c - p%c))
        print(res)
