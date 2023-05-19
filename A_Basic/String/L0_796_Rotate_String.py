""" https://leetcode.com/problems/rotate-string/
check if p in s+s
"""
class Solution:
    def rotateString(self, s: str, p: str) -> bool:
        return p in s*2 and len(s)==len(p)
