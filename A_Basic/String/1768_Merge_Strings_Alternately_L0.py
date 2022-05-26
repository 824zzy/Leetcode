""" https://leetcode.com/problems/merge-strings-alternately
basic usage of zip_longest
"""
class Solution:
    def mergeAlternately(self, x: str, y: str) -> str:
        ans = ''
        for xx, yy in zip_longest(x, y, fillvalue=''):
            ans += xx
            ans += yy
        return ans