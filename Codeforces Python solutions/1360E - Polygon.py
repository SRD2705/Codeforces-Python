for _ in range(int(input())):
    n = int(input())
    li = []
    posj = []
    posi = []
    st = True
    for i in range(n):
        tmp = list(map(int, input()))
        li.append(tmp)
    # print(li)
    for i in range(n-1):
        for j in range(n-1):
            if li[i][j] == 0:
                continue
            if li[i+1][j] == 0 and li[i][j+1] == 0:
                st = False
                break

    if st == True:
        print("YES")
    else:
        print("NO")

