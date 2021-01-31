# 115A-Party

from collections import defaultdict
d = defaultdict(list)
n = int(input())
li = []
for i in range(1,n+1):
    k = int(input())
    if k == -1:
        li.append(i)
    else:
        d[k].append(i)
# print(d)

def bfs(s):
    lev = 0
    vis = []
    q = [s]
    q.append(-1)
    while q:
        s = q[0]
        if s == -1:
            lev += 1
            q.pop(0)
            if q != []:
                q.append(-1)
        elif s not in vis:
            vis.append(s)
            q.pop(0)
            for node in d[s]:
                if node not in vis:
                    q.append(node)
        else:
            q.pop(0)
            for node in d[s]:
                if node not in vis:
                    q.append(node)
    return lev

res = []
tmp = 0
for i in li:
    if i in d.keys():
        tmp = bfs(i)
        res.append(tmp)
# print(tmp)
if res == []:
    print(1)
else:
    print(max(res))