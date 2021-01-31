# 913B-Christmas Spruce
from collections import defaultdict
d = defaultdict(list)
n = int(input())
li = []
for i in range(2,n+1):
    k = int(input())
    d[k].append(i)
# print(d)

def check(s,vis,q):
    res = 0
    if s not in vis:
        vis.append(s)
        q.pop(0)
        for node in d[s]:
            if node not in vis:
                if node not in d.keys():
                    res += 1
                else:
                    q.append(node)

    else:
        q.pop(0)
        for node in d[s]:
            if node not in vis:
                if node not in d.keys():
                    res += 1
                else:
                    q.append(node)
    return res

def bfs(s):
    res = 0
    vis = []
    q = [s]
    while q:
        s = q[0]
        res = check(s,vis,q)
        if res < 3:
            return 0
    return 1

k = bfs(1)
if k == 1:
    print("Yes")
else:
    print("No")




