""" https://leetcode.com/problems/k-radius-subarray-averages/
use prefix sum array to find range average
"""
from header import *


class Solution:
    def getAverages(self, A: List[int], k: int) -> List[int]:
        prefix = [0] + list(accumulate(A))
        ans = [-1] * len(A)
        for i in range(k, len(A) - k):
            ans[i] = (prefix[i + k + 1] - prefix[i - k]) // (2 * k + 1)
        return ans


# prefix sum on the fly
class Solution:
    def getAverages(self, A: List[int], k: int) -> List[int]:
        sm = sum(A[: (2 * k)])
        n = len(A)
        ans = [-1] * n
        for i in range(k, n - k):
            sm += A[i + k]
            ans[i] = sm // (2 * k + 1)
            sm -= A[i - k]
        return ans
