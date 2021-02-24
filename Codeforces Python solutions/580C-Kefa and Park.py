# 580C-Kefa and Park

def go_bfs():
    bfs = [(li[0], 0, 0)]
    sums = 0
    while bfs:
        leaf = True
        count, v, p = bfs.pop(0)
        for j in graph[v]:
            if j == p:
                continue
            leaf = False
            if li[j] == 0:
                bfs.append((0, j, v))
            elif count + 1 <= m:
                bfs.append((count + 1, j, v))
        if leaf:
            sums += 1

    return sums

if __name__ == '__main__':
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    graph = [[] for i in range(n)]
    for i in range(n - 1):
        s, d = map(int, input().split())
        graph[s - 1].append(d - 1)
        graph[d - 1].append(s - 1)
    # print(graph)
    print(go_bfs())