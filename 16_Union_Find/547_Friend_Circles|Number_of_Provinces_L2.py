# Disjoint Set Union
class DSU: 
    def __init__(self, n):
        self.p = [i for i in range(n)]
    
    def find(self, u):
        if self.p[u]!=u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        n = len(M)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]==1:
                    dsu.union(i, j)
        return len(set([dsu.find(i) for i in range(n)]))