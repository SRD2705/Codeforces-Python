for _ in range(int(input())):
    n, k = map(int, input().split())
    li = []
    tmp = []
    for j in range(1,n+1):
        tmp.append(j)
    for i in range(n,0,-1):
        if i > k:
            li.append(i)
            tmp.remove(i)
        elif i < k:
            if k-i in tmp:
                if k-i != i:
                    li.append(i)
                    tmp.remove(i)
                    tmp.remove(k-i)
                else:
                    li.append(i)
                    tmp.remove(i)
        else:
            tmp.remove(i)
        if tmp == []:
            break
    if tmp != []:
        li += tmp
    print(len(li))
    print(*li)