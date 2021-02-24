# 1374B - Multiply by 2, divide by 6
for _ in range(int(input())):
    n = int(input())
    cnt2 = 0
    cnt3 = 0
    if n == 1:
        print(0)
    else:
        while (n%2 == 0):
            n = n//2
            cnt2 += 1
        while (n%3 == 0):
            n = n//3
            cnt3 += 1
        if n==1 and cnt2 <= cnt3:
            print(2*cnt3-cnt2)
        else:
            print(-1)