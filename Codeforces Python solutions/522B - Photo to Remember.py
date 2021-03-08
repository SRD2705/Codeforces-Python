n = int(input())
wsum = 0
hli = []
li=[]
mx = 0
mxc = 1
smx = 0
k = 0
for i in range(n):
    w, h = map(int, input().split())
    li.append([w,h])
    wsum += w
    if h > mx:
        smx = mx
        mx = h
    elif h == mx:
        mxc += 1
    if h > smx and h != mx:
        smx = h
    hli.append(h)
for i in range(n):
    w = li[i][0]
    h = li[i][1]
    tmp = wsum - w
    if mxc == 1 or mxc == 0:
        if h == mx:
            print(tmp*smx,end=' ')
        else:
            print(tmp*mx,end=' ')
    elif mxc > 1:
        print(tmp * mx,end=' ')