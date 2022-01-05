""" https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
greedily find matching substrings
"""
class Solution:
    def canChoose(self, G: List[List[int]], A: List[int]) -> bool:
        i = 0
        for g in G:
            for ii in range(i, len(A)):
                if A[ii:ii+len(g)]==g:
                    i = ii+len(g)
                    break
            else: return False
        return True