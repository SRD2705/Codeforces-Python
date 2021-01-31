# 1474B-Different Divisors

x = 1000000
res = [True for i in range(x+1)]
def sieve(x,res):
    res[0] = False
    res[1] = False
    p = 2
    while p*p <= x:
        if res[p] == True:
            for i in range(p*p,x+1,p):
                res[i] = False
        p += 1
sieve(x,res)

def findprime_in_bound(low,up,res):
    for i in range(low,up):
        if res[i]:
            return i

for _ in range(int(input())):
    n = int(input())
    tmp1 = findprime_in_bound(1+n,1000000,res)
    tmp2 = findprime_in_bound(tmp1+n,1000000,res)
    print(tmp1*tmp2)