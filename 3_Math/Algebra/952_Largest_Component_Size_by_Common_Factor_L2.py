""" https://leetcode.com/problems/largest-component-size-by-common-factor/
math + union find: Sieve of Eratosthenes
"""
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    
    def find(self, u):
        if self.p[u]!=u: self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(max(A)+1)
        for x in A:
            for p in range(2, int(sqrt(x))+1):
                if x%p==0:
                    dsu.union(x, p)
                    dsu.union(x, x//p)
        
        cnt = Counter(dsu.find(x) for x in A)
        return max(cnt.values())