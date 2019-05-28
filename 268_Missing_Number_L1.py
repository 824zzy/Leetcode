
""" basic solution via set
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = list(set(nums))
        for i in range(len(s)):
            if i != s[i]:
                return i
        return len(s)

""" tricky solution using math
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        t_sum = int(n * (n+1) / 2)
        n_sum = sum(nums)
        # print(t_sum, n_sum)
        return t_sum-n_sum