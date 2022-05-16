""" https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
use a size-fixed sliding window with size k to count vowels
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vowels = 0
        i = 0
        
        for j in range(len(s)):
            if s[j] in 'aeiou': vowels += 1
            if j>=k:
                if s[i] in 'aeiou': vowels -= 1
                i += 1
            ans = max(ans, vowels)
        return ans