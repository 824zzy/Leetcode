""" https://leetcode.com/problems/gcd-sort-of-an-array/
union find + sieve of eratosthenes 
"""
from header import *

class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    
    def find(self, u):
        if self.p[u]!=u: self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
        
class Solution:
    def gcdSort(self, A: List[int]) -> bool:
        m = max(A)
        dsu = DSU(m+1)
        seen = set(A)
        # modified sieve of eratosthenes
        sieve = [1]*(m+1)
        sieve[0] = sieve[1] = 0
        for k in range(m//2+1):
            if sieve[k]:
                for x in range(2*k, m+1, k):
                    sieve[x] = 0
                    if x in seen: dsu.union(k, x)
        
        return all(dsu.find(x) == dsu.find(y) for x, y in zip(A, sorted(A)))