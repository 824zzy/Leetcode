class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(nums, target, comb, start):
            if target==0:
                ans.append(comb[:])
                return
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                if nums[i]>target:
                    break
                dfs(nums, target-nums[i], comb+[nums[i]], i+1)
        dfs(sorted(candidates), target, [], 0)
        return ans
    
class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        candidates = sorted(candidates)
        
        def dfs(remain, target, path):
            if target==0:
                if path not in ans:
                    ans.append(path)
            for i, c in enumerate(remain):
                if target-c>=0:
                    dfs(remain[i+1:], target-c, path+[c])

        dfs(candidates, target, [])
        return ans