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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU(n)
        for i in connections:
            dsu.union(i[0], i[1])
        p = len(set([dsu.find(i) for i in range(len(dsu.p))]))-1
        if n-len(connections)>1:
            return -1
        else:
            return p