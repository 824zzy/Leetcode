""" L1: https://leetcode.com/problems/vowels-of-all-substrings/
here are (i + 1) * (n - i) substrings containing s[i].
"""
class Solution:
    def countVowels(self, s: str) -> int:
        return sum((i + 1) * (len(s) - i) for i, c in enumerate(s) if c in 'aeiou')