""" https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
simulation
"""
class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s = s.replace('AB', '').replace('CD', '')
        return len(s)