""" L1
three pointer variance: use i, j as two pointer and pos to find minimum length of third side.
"""


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pos = bisect_left(nums, nums[i] + nums[j])
                ans += max(0, pos - 1 - j)
        return ans
