from copy import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(nums, target, comb):
            if target==0:
                ans.append(comb[:])
                return
            if target<0:
                return
            for i, n in enumerate(nums):
                if n <= target:
                    dfs(nums[i:], target-n, comb+[n])
        dfs(candidates, target, [])
        return ans