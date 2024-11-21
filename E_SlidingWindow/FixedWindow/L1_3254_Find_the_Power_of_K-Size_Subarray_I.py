""" https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
fixed sliding window

Maintain a fixed sliding window with size k while checking the subarray is consecutive or not.
Optimal solution see 3255 using two pointers.
"""

from header import *


# O
class Solution:
    def resultsArray(self, A: List[int], k: int) -> List[int]:
        def check(A):
            for i in range(1, len(A)):
                if A[i - 1] + 1 != A[i]:
                    return False
            return True

        sw = A[:k]
        ans = [-1] * (len(A) - k + 1)
        if check(sw):
            ans[0] = max(sw)
        for i in range(k, len(A)):
            sw.pop(0)
            sw.append(A[i])
            if check(sw):
                ans[i - k + 1] = max(sw)
        return ans
