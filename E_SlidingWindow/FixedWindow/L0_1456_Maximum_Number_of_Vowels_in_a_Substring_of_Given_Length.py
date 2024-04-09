""" https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
use a size-fixed sliding window with size k to count vowels
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        x = sum(c in 'aeiou' for c in s[:k])
        ans = x
        for i in range(k, len(s)):
            x += (s[i] in 'aeiou')
            x -= (s[i - k] in 'aeiou')
            ans = max(ans, x)
        return ans
