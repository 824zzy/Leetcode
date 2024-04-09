""" https://leetcode.com/problems/container-with-most-water/
greedily find maximum area by different direction two pointers
"""


class Solution:
    def maxArea(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r - l) * min(A[l], A[r]))
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return ans
