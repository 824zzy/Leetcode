""" usage of itertools and back-tracking
"""
# list(permutations(nums))
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rv = list(permutations(nums))
        for i in range(len(rv)):
            rv[i] = list(rv[i])
        return rv

# Backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(nums, cur):
            if not nums: 
                self.ans.append(cur)
                return
            for i, n in enumerate(nums):
                dfs(nums[:i]+nums[i+1:], cur+[n])
        dfs(nums, [])
        return self.ans