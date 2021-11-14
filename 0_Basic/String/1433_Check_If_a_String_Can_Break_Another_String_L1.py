""" https://leetcode.com/problems/check-if-a-string-can-break-another-string/
Sort s1 and s2 and compare if each characters in s1 is consistently larger/smaller than s2.
"""
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        return all(c1 <= c2 for c1, c2 in zip(s1, s2)) or all(c1 >= c2 for c1, c2 in zip(s1, s2))