""" https://leetcode.com/problems/word-pattern/
the same as 205
check the length of sets
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern)==len(s) and len(set(s))==len(set(pattern))==len(set(zip(s, t)))