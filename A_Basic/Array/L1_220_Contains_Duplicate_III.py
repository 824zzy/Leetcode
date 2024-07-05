class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) > 1000:
            nums = sorted(nums)
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    return True
            return False
        for i, n in enumerate(nums):
            for j in range(i + 1, i + 1 + k):
                if j < len(nums) and abs(nums[i] - nums[j]) <= t:
                    return True
        return False
