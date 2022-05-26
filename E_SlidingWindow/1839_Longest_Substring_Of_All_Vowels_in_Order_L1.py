""" https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
use `unique` to mark the legit substring
"""
class Solution:
    def longestBeautifulSubstring(self, A: str) -> int:
        i = 0
        ans = 0
        unique = 1
        for j in range(1, len(A)):
            if A[j-1]>A[j]:
                i = j
                unique = 1
            elif A[j-1]<A[j]:
                unique += 1
            if unique==5: ans = max(ans, j-i+1)
        return ans