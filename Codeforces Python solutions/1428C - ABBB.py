for _ in range(int(input())):
    li = list(input())
    res = []
    for i in range(len(li)):
        if res == []:
            res.append(li[i])
        else:
            if res[-1] == 'A' and li[i] == 'B':
                res.pop()
            elif res[-1] == 'B' and li[i] == 'B':
                res.pop()
            else:
                res.append(li[i])
    print(len(res))