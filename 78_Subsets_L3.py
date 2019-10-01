""" straight-forward solution
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in res:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res


""" Back-tracking solution
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

""" My clear solution
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def dfs(nums: List[int], sub: List[int]) -> None:
            if not nums:
                self.res.append(sub[:])
                return
            
            self.res.append(sub[:])
            for i, x in enumerate(nums):
                dfs(nums[i+1:], sub+[x])
        
        dfs(nums, [])
        return self.res