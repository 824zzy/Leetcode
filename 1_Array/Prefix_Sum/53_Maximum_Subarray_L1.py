class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_n = nums[0]
        min_n = 0
        prefix = 0
        for n in nums:
            prefix += n
            max_n = max(max_n, prefix-min_n)
            min_n = min(min_n, prefix)
        return max_n