"""
"""
# Back-track by Recursion
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(nums: List[int], tmp: int, remain: int) -> None:
            if remain == 0:
                self.res.append(tmp[:])
                return
            if remain < 0:
                return
            
            for i, x in enumerate(nums):
                if x <= remain:
                    dfs(nums[i:], tmp+[x], remain-x)
            """ the for loop can be writen as follow but not suggested
            for i in range(index, len(nums)):
                tmp.append(nums[i])
                dfs(nums, tmp, remainder-nums[i], i)
                tmp.pop()
            """

        dfs(nums, [], target)
    return self.res