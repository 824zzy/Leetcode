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

# Backtracking routine
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(nums: List[int], tmp: List[int]) -> None:
            if len(nums) == len(tmp):
                self.res.append(tmp[:])
                return
            
            for i, x in enumerate(nums):
                if x not in tmp:
                    dfs(nums, tmp+[x])
        
        dfs(nums, [])
        return self.res