""" https://leetcode.com/problems/isomorphic-strings/submissions/
the same as 290
check the length of sets
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(t)==len(s) and len(set(s))==len(set(t))==len(set(zip(s, t)))