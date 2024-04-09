""" https://leetcode.com/problems/length-of-last-word/
string simulation
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if len(s.split()) > 0 else 0
