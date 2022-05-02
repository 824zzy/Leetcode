""" https://leetcode.com/problems/vowels-of-all-substrings/
from lee: https://leetcode.com/problems/vowels-of-all-substrings/discuss/1563780/JavaC%2B%2BPython-Easy-and-Concise-O(n)
"""
class Solution:
    def countVowels(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                ans += (i+1)*(len(s)-i)
        return ans