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
        def dfs(nums, perm):
            if not nums:
                self.ans.append(perm)
                return
            for i in range(len(nums)):
                t = perm[:]
                t.append(nums[i])
                # print(nums[0:i]+nums[i+1:], nums[i], t)
                dfs(nums[0:i]+nums[i+1:], t)
            
        dfs(nums, [])
        return self.ans