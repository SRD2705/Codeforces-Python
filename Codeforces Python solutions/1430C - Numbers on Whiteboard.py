import math
for _ in range(int(input())):
    n = int(input())
    tmp = 0
    print(2)
    for i in range(n,0,-1):
        if i == n:
            tmp = math.ceil(((i)+(i-1))/2)
        else:
            print(i,tmp)
            tmp = math.ceil(((i)+tmp)/2)