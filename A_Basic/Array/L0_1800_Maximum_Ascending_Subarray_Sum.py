""" https://leetcode.com/problems/maximum-ascending-subarray-sum/
1. greedily find the maximum sum of the ascending subarray.
2. if the current element is smaller than the previous one, reset the sum to the current element.
"""
from header import *


class Solution:
    def maxAscendingSum(self, A: List[int]) -> int:
        ans = A.copy()
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                ans[i] += ans[i - 1]
        return max(ans)

# brute force solution for contest: O(n^2)


class Solution:
    def maxAscendingSum(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            sm = A[i]
            for j in range(i + 1, len(A)):
                if A[j] > A[j - 1]:
                    sm += A[j]
                else:
                    break
            ans = max(ans, sm)
        return ans
