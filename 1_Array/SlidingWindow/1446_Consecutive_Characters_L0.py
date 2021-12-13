""" https://leetcode.com/problems/consecutive-characters/
window size is controlled by checking if s[i] and s[j] are the same
"""
class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        ans = 1
        for j in range(len(s)):
            if s[i]!=s[j]: i = j
            ans = max(ans, j-i+1)
        return ans