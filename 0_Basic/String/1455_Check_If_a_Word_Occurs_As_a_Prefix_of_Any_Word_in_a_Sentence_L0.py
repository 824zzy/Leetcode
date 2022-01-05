""" https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
brute force
"""
class Solution:
    def isPrefixOfWord(self, A: str, p: str) -> int:
        for i, w in enumerate(A.split()):
            if len(w)>=len(p):
                if w[:len(p)]==p: return i+1
        return -1