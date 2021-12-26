""" https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
split and count length
"""
class Solution:
    def mostWordsFound(self, A: List[str]) -> int:
        return max([len(s.split()) for s in A])