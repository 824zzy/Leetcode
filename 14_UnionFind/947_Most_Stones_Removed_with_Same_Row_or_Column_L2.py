""" https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
find stones in the same row/column and not in the same group, then union them together
"""
class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
        
class Solution:
    def removeStones(self, A: List[List[int]]) -> int:
        X = []
        for i, j in A: X.extend([i, j])
        dsu = DSU(len(X))
        
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i][0]==A[j][0] and dsu.find(i)!=dsu.find(j):
                    dsu.union(i, j)
                    ans += 1
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i][1]==A[j][1] and dsu.find(i)!=dsu.find(j):
                    dsu.union(i, j)
                    ans += 1
        
        return ans