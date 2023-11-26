""" https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
only check odd and even values
"""
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return sorted(s1[::2])==sorted(s2[::2]) and sorted(s1[1::2])==sorted(s2[1::2])