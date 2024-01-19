""" https://leetcode.com/problems/greatest-common-divisor-traversal/submissions/
1. gcd(A[i], A[j])>1 === A[i] and A[j] share at least one common prime factor
2. prime optimization: since 1 <= nums[i] <= 10^5 ==> largest prime factor is 313
3. union find using hash table to avoid TLE
"""
from header import *

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]     

class Solution:
    def canTraverseAllPairs(self, A: List[int]) -> bool:
        n = len(A)
        dsu = {}
        def find(x):
            if x not in dsu: dsu[x] = x
            elif dsu[x]!=x: dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x, y):
            dsu[find(x)] = find(y)
            
        for x in A:
            if x==1: return len(A)==1
            # prime factorization
            pf = []
            for p in PRIMES:
                if x % p == 0:
                    pf.append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                pf.append(x)
            for x in pf:
                union(x, pf[0])
        return len(set(find(x) for x in dsu))==1
    
"""
[2,3,6]
[3,9,5]
[4,3,12,8]
[1,1]
[10]
[1,1,1,1]
[10,10]
[10007,20014]
[11]
"""