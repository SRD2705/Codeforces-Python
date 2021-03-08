for _ in range(int(input())):
    n = int(input())
    res = 0
    li = list(input())
    li.append(li[0])
    c = False
    ac = False
    for i in range(n):
        if li[i] == '-' or li[i+1] == '-':
            res += 1
        if li[i] == '>':
            c = True
        if li[i] == '<':
            ac = True
    if c == True and ac == True:
        print(res)
    else:
        print(n)