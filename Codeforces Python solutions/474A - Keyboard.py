tmp = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
tmp1 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']
tmp2 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
n = input()
li = list(input())
if n == 'R':
    for i in range(len(li)):
        if li[i] in tmp:
            if li[i] == tmp[0]:
                print(tmp[0],end = '')
            else:
                print(tmp[(tmp.index(li[i]))-1],end = '')
        elif li[i] in tmp1:
            if li[i] == tmp1[0]:
                print(tmp1[0],end = '')
            else:
                print(tmp1[(tmp1.index(li[i]))-1],end = '')
        else:
            if li[i] == tmp2[0]:
                print(tmp2[0],end = '')
            else:
                print(tmp2[(tmp2.index(li[i]))-1],end = '')
elif n == 'L':
    for i in range(len(li)):
        if li[i] in tmp:
            if li[i] == tmp[len(tmp)-1]:
                print(tmp[-1],end = '')
            else:
                print(tmp[(tmp.index(li[i]))+1],end = '')
        elif li[i] in tmp1:
            if li[i] == tmp1[len(tmp1)-1]:
                print(tmp1[-1],end = '')
            else:
                print(tmp1[(tmp1.index(li[i]))+1],end = '')
        else:
            if li[i] == tmp2[len(tmp2)-1]:
                print(tmp2[-1],end = '')
            else:
                print(tmp2[(tmp2.index(li[i]))+1],end = '')