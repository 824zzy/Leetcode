""" https://leetcode.com/problems/longest-palindrome/
use frequency table to count odd and even numbers, note that one needs to add extra 1 if there is odd number
"""
from header import *

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        hasmid = False
        for _, v in cnt.items():
            if v&1: hasmid = True
            ans += v//2
        return ans*2+hasmid