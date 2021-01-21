'''
C. ARRAY DESTRUCTION
time limit per test1 second
memory limit per test256 megabytes
input: standard input
output: standard output
You found a useless array a of 2n positive integers. You have realized that you actually don't need this array,
so you decided to throw out all elements of a.

It could have been an easy task, but it turned out that you should follow some rules:

In the beginning, you select any positive integer x.
Then you do the following operation n times:
select two elements of array with sum equals x;
remove them from a and replace x with maximum of that two numbers.
For example, if initially a=[3,5,1,2], you can select x=6.
Then you can select the second and the third elements of a with sum 5+1=6 and throw them out.
After this operation, x equals 5 and there are two elements in array: 3 and 2. You can throw them out on the next operation.

Note, that you choose x before the start and can't change it as you want between the operations.

Determine how should you behave to throw out all elements of a.

INPUT
The first line contains a single integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains the single integer n (1≤n≤1000).

The second line of each test case contains 2n integers a1,a2,…,a2n (1≤ai≤106) — the initial array a.

It is guaranteed that the total sum of n over all test cases doesn't exceed 1000.

OUTPUT
For each test case in the first line print YES if it is possible to throw out all elements of the array and NO otherwise.

If it is possible to throw out all elements, print the initial value of x you've chosen. Print description of n operations next.
For each operation, print the pair of integers you remove.

INPUT:
4
2
3 5 1 2
3
1 1 8 8 64 64
2
1 1 2 4
5
1 2 3 4 5 6 7 14 3 11

OUTPUT:
YES
6
1 5
2 3
NO
NO
YES
21
14 7
3 11
5 6
2 4
3 1

NOTE
The first test case was described in the statement.
In the second and third test cases, we can show that it is impossible to throw out all elements of array a.


'''

from copy import deepcopy
def checknum(li,x,y,res1,res2):
    li.remove(x)
    res1.append(x)
    li.remove(y)
    res2.append(y)
    if len(li) == 0:
        return 1
    else:
        tmp = max(x,y)
        j = len(li)-1
        i = 0
        while i < j:
            if li[i] + li[j] == tmp:
                return checknum(li,li[i],li[j],res1,res2)
            elif li[i]+li[j] > tmp:
                return 2
            else:
                i += 1
        return 2


for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    i = 0
    j = len(li)-1
    k = 0
    res1=[]
    res2=[]
    while i < j:
        li1 = deepcopy(li)
        tmp = li1[j]+li1[i]
        res1.clear()
        res2.clear()
        k = checknum(li1,li1[j],li1[i],res1,res2)
        if k == 1:
            print("YES")
            print(tmp)
            for i in range(n):
                print(res1[i],res2[i],sep=" ")
            break
        elif k == 2:
             i += 1
    if k==2:
        print("NO")