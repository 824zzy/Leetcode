""" https://leetcode.com/problems/count-sorted-vowel-strings/
"""
class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dp(i, j):
            if i==n: return 1
            ans = 0
            for jj in range(j, 6):
                ans += dp(i+1, jj)
            return ans
        
        return dp(0, 1)