""" https://leetcode.com/problems/implement-strstr/
index usage
"""
class Solution:
    def strStr(self, A: str, B: str) -> int:
        if B in A: return A.index(B)
        else: return -1