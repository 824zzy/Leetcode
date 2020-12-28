class Solution:
    def combinationSum(self, candidates: List[int], t: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        def dfs(cand, s, path):
            if s>t: return
            if s==t: self.ans.append(path)
            for i, c in enumerate(cand):
                if s+c>t: break
                dfs(cand[i:], s+c, path+[c])
        dfs(candidates, 0, [])
        return self.ans
    
    
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
