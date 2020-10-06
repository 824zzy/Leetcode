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
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def dfs(path, t):
            if t==0:
                self.ans.append(path)
                return
            elif t<0:
                return
            for c in candidates:
                if not path or c>=path[-1]:
                    dfs(path+[c], t-c)
        dfs([], target)
        return self.ans
