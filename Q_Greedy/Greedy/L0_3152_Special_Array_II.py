""" https://leetcode.com/problems/special-array-ii/
greedily find the longest subarray with the same parity
"""

from header import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        A = [1]
        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i - 1] % 2:
                A.append(A[-1] + 1)
            else:
                A.append(1)

        ans = []
        for i, j in queries:
            if j - i + 1 == A[j] - A[i] + 1:
                ans.append(True)
            else:
                ans.append(False)
        return ans


"""
[3,4,1,2,6]
[[0,4]]
[4,3,1,6]
[[0,2],[2,3]]
"""
