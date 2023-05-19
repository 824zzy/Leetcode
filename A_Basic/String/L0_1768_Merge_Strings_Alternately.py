""" https://leetcode.com/problems/merge-strings-alternately
basic usage of zip_longest
"""
from header import *

class Solution:
    def mergeAlternately(self, x: str, y: str) -> str:
        ans = ''
        for xx, yy in zip_longest(x, y, fillvalue=''):
            ans += xx
            ans += yy
        return ans
    

# linear scan
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = [''] * 200
        for i in range(len(word1)):
            ans[2*i] = word1[i]
        for i in range(len(word2)):
            ans[2*i+1] = word2[i]
        return ''.join(ans)