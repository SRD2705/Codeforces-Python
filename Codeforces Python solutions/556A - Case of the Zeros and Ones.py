n = int(input())
li = list(map(int, input()))
res = []
for i in li:
    if res == []:
        res.append(i)
    else:
        if res[-1] != i:
            res.pop()
        else:
            res.append(i)
print(len(res))
