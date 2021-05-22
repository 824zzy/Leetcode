# Hash table the same as Two Sum II
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target-nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target-nums[i]]+1, i+1]