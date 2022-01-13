""" https://leetcode.com/problems/subsets/
Use bit to indicate which element should be included
"""
class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        ans = []
        N = len(A)
        for mask in range(1<<N):
            tmp = []
            for i in range(N):
                if mask&1<<i: tmp.append(A[i])
            ans.append(tmp)
        return ans