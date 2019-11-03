# Hash table the same as Two Sum II
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target-nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target-nums[i]]+1, i+1]

# Two Pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        for _ in range(len(nums)):
            if nums[i]+nums[j] == target:
                return [i+1, j+1]
            elif nums[i]+nums[j] < target:
                i += 1
            else:
                j -= 1