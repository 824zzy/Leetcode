# Gaussian sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        t_sum = int(n * (n+1) / 2)
        n_sum = sum(nums)
        return t_sum-n_sum