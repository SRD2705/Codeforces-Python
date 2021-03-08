for _ in range(int(input())):
    li = list(map(int, input()))
    tmp = []
    res = 0
    for i in li:
        if tmp == []:
            tmp.append(i)
        else:
            if tmp[-1] != i:
                tmp.pop()
                res += 1
            else:
                tmp.append(i)
    # print(res)
    if res%2 != 0:
        print("DA")
    else:
        print("NET")
