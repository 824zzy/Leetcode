""" L4
TODO: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/1312722/Python-Two-solutions-explained
"""
from sortedcontainers import SortedList
    
class Solution:
    def maxSumSubmatrix(self, M, k):
        def countRangeSum(nums, U):
            SList, ans = SortedList([0]), -float("inf")
            for s in accumulate(nums):
                idx = SList.bisect_left(s - U) 
                if idx < len(SList): ans = max(ans, s - SList[idx])        
                SList.add(s)
            return ans
        
        m, n, ans = len(M), len(M[0]), -float("inf")
        
        for i, j in product(range(1, m), range(n)):
            M[i][j] += M[i-1][j]
                
        M = [[0]*n] + M
        
        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(M[r1], M[r2])]
            ans = max(ans, countRangeSum(row, k))
            
        return ans