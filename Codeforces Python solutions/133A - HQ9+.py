# 133A - HQ9+
li = list(input())
res = 0
for i in li:
    if i == 'H' or i == 'Q' or i == '9':
        res = 1
        break
if res == 1:
    print("YES")
else:
    print("NO")