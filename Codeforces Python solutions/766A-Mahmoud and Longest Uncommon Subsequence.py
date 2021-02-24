# 766A-Mahmoud and Longest Uncommon Subsequence

li = list(input())
li1 = list(input())
if li == li1:
    print(-1)
elif len(li) == len(li1):
    print(len(li))
else:
    if len(li) > len(li1):
        print(len(li))
    else:
        print(len(li1))