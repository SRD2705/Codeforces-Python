# 118A-String Task
vow = ['a','e','i','o','u','y']
li = list(input())
res = ''
for i in li:
    if i.lower() not in vow:
        res += '.'
        res += str(i.lower())
print(res)