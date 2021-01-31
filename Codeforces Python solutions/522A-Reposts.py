# 522A-Reposts

from collections import defaultdict
d = defaultdict(list)
res = 1
for _ in range(int(input())):
    li = list(input().split())
    d[li[-1].upper()].append(li[0].upper())


def bfs(s):
    res = 0
    vis = []
    q = [s]
    q.append(-1)
    while q:
        s = q[0]
        if s == -1:
            res += 1
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
    return res

k = bfs("POLYCARP")
print(k)