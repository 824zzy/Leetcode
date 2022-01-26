""" https://leetcode.com/problems/subsets/
Use bit to indicate which element should be included
"""
class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        for mask in range(1<<len(A)):
            ans.append([A[i] for i in range(len(A)) if mask>>i &1]) # or mask & 1<<i
        return ans