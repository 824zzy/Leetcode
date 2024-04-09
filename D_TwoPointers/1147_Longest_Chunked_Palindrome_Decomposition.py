""" https://leetcode.com/problems/longest-chunked-palindrome-decomposition/submissions/
greedily search shortest matched substring frome two sides to middle
"""


class Solution:
    def longestDecomposition(self, A: str) -> int:
        l, r = 0, len(A) - 1
        ll, rr = l, r
        ans = 0
        while l < r:
            if A[ll:l + 1] == A[r:rr + 1]:
                ans += 2
                ll, rr = l + 1, r - 1
            l, r = l + 1, r - 1
        return ans + (ll <= rr)
