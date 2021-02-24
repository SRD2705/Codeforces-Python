# 1480A-Yet Another String Game

for _ in range(int(input())):
    li = list(input())
    for i in range(len(li)):
        tmp = ord(li[i])
        if i % 2 == 0:
            if tmp != 97:
                li[i] = chr(97)
            else:
                li[i] = chr(tmp+1)
        else:
            if tmp != 122:
                li[i] = chr(122)
            else:
                li[i] = chr(tmp-1)
    print(*li,sep='')