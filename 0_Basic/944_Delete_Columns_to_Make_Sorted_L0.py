""" https://leetcode.com/problems/delete-columns-to-make-sorted/
use zip to find all the columns and check if each column is lexicographically
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = [list(s) for s in zip(*strs)]
        return sum([1 for c in cols if c!=sorted(c)])
