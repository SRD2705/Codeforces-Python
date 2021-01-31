# 939A-Love triangle

n = int(input())
li = list(map(int, input().split()))
li.insert(0,0)
# print(li)
res = 0
for i in range(1,n):
    if i == li[li[li[i]]]:
        res = 1
        break
if res == 1:
    print("YES")
else:
    print("NO")