# 1490C - Sum of Cubes
def cubesum(n):
    s = dict()
    for i in range(1,n+1):
        if i * i * i > n:
            break
        s[i * i * i] = 1
        if (n - i * i * i) in s.keys():
            return True

    return False

for _ in range(int(input())):
    n = int(input())
    if (cubesum(n)):
        print("YES")
    else:
        print("NO")