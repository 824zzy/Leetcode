""" https://leetcode.com/problems/couples-holding-hands/
idea from grandyang: https://www.cnblogs.com/grandyang/p/8716597.html
1. linear scan every two seats and find if the two people are in the same set
2. if not, then union the people's group
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
    def minSwapsCouples(self, A: List[int]) -> int:
        dsu = DSU(len(A)//2)
        ans = 0
        for i in range(0, len(A), 2):
            a, b = A[i]//2, A[i+1]//2
            if dsu.find(a)!=dsu.find(b):
                dsu.union(a, b)
                ans += 1
        return ans