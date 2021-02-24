# 208A - Dubstep
li = list(map(str, input().split(sep='WUB')))
space = li.count('')
for i in range(space):
    li.remove('')
print(*li)