""" https://leetcode.com/problems/find-triangular-sum-of-an-array/
similar to 118&119 Pascal Triangle
"""


class Solution:
    def triangularSum(self, A: List[int]) -> int:
        ans = A
        for i in range(len(A) - 1):
            for j in range(len(A) - i - 1):
                ans[j] = (ans[j] + ans[j + 1]) % 10
        return ans[0]
