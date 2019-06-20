"""
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:




""" Note that brute force not work O(n^3)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    ans = max(ans, s[i:j+1], key=len)
        return ans