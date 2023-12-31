""" https://leetcode.com/problems/largest-substring-between-two-equal-characters/
enumerate every character, find the leftmost and rightmost position of the character
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for i in range(26):
            c = chr(97+i)
            l, r = 0, len(s)-1
            while l<len(s) and s[l]!=c:
                l += 1
            while r>=0 and s[r]!=c:
                r -= 1
            if l<r:
                ans = max(ans, r-l-1)
        return ans