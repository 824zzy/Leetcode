""" https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        return sum(a.count(c) for c in 'aeiouAEIOU')==sum(b.count(c) for c in 'aeiouAEIOU')