""" https://leetcode.com/problems/percentage-of-letter-in-string/
simply use str.count(chr) to compute percentage
"""
class Solution:
    def percentageLetter(self, s: str, c: str) -> int:
        return int(s.count(c)/len(s)*100)