'''
D. CLEANING
time limit per test2 seconds
memory limit per test256 megabytes
input:standard input
output:standard output
During cleaning the coast, Alice found n piles of stones. The i-th pile has ai stones.
Piles i and i+1 are neighbouring for all 1≤i≤n−1. If pile i becomes empty, piles i−1 and i+1 doesn't become neighbouring.

Alice is too lazy to remove these stones, so she asked you to take this duty. She allowed you to do only the following operation:
Select two neighboring piles and, if both of them are not empty, remove one stone from each of them.
Alice understands that sometimes it's impossible to remove all stones with the given operation,
so she allowed you to use the following superability:

Before the start of cleaning, you can select two neighboring piles and swap them.
Determine, if it is possible to remove all stones using the superability not more than once.

INPUT:
The first line contains a single integer t (1≤t≤104) — the number of test cases.
The first line of each test case contains the single integer n (2≤n≤2⋅105) — the number of piles.
The second line of each test case contains n integers a1,a2,…,an (1≤ai≤109) — the number of stones in each pile.
It is guaranteed that the total sum of n over all test cases doesn't exceed 2⋅105.

OUTPUT:
For each test case, print YES or NO — is it possible to remove all stones using the superability not more than once or not.

INPUT:
5
3
1 2 1
3
1 1 2
5
2 2 2 1 3
5
2100 1900 1600 3000 1600
2
2443 2445

OUTPUT:
YES
YES
YES
YES
NO

NOTE:
Note
In the first test case, you can remove all stones without using a superability: [1,2,1]→[1,1,0]→[0,0,0].
In the second test case, you can apply superability to the second and the third piles and then act like in the first testcase.
In the third test case, you can apply superability to the fourth and the fifth piles, thus getting a=[2,2,2,3,1].
In the fourth test case, you can apply superability to the first and the second piles, thus getting a=[1900,2100,1600,3000,1600].
'''


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    p = [-1] * (n + 1)
    p[0] = 0
    for i in range(n):
        p[i + 1] = a[i] - p[i]
        if p[i + 1] < 0:
            break
    if p[n] == 0:
        print('YES')
        continue
    s = 0
    for i in range(n - 1, 0, -1):
        if p[i - 1] >= 0 and a[i - 1] - s >= 0 and a[i - 1] - s == a[i] - p[i - 1]:
            print('YES')
            break
        s1 = a[i] - s
        if s1 < 0:
            print('NO')
            break
        s = s1
    else:
        print('NO')
