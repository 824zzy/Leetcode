# Facebook: TODO: dfs solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1 or sum(nums)%2 != 0:
            return False
        target = sum(nums) / 2
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                if temp+nums[j] == target:
                    return True
                elif temp+nums[j] < target:
                    temp += nums[j]
        return False
        