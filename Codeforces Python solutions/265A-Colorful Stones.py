# 265A-Colorful Stones
li = list(input())
li1 = list(input())
tmp = li[0]
j = 0
for i in range(len(li1)):
    if tmp == li1[i]:
        j += 1
        tmp = li[j]
print(j+1)