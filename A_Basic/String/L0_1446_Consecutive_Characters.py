""" https://leetcode.com/problems/consecutive-characters/
basic usage of group by
"""
class Solution:
    def maxPower(self, s: str) -> int:
        return max([len(list(v)) for k, v in groupby(s)])