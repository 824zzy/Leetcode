""" https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/
two pointers
"""

from header import *


class Solution:
    def resultsArray(self, A: List[int], k: int) -> List[int]:
        if k == 1:
            return A
        ans = [-1] * (len(A) - k + 1)
        i = 0
        for j in range(1, len(A)):
            if j and A[j] - A[j - 1] == 1:
                if j - i + 1 >= k:
                    ans[j - k + 1] = A[j]
            else:
                i = j
        return ans
