""" https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/
for each substring A[i:len(A):k], find its Longest Increasing Subsequence(LIS)
"""


class Solution:
    def kIncreasing(self, A: List[int], k: int) -> int:
        def LIS(nums):
            vals = []
            for x in nums:
                k = bisect_right(vals, x)
                if k == len(vals):
                    vals.append(x)
                else:
                    vals[k] = x
            return len(nums) - len(vals)

        ans = 0
        for i in range(k):
            ans += LIS(A[i : len(A) : k])
        return ans
