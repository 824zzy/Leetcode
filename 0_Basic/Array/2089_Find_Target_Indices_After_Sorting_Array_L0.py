""" https://leetcode.com/problems/find-target-indices-after-sorting-array/
sort and find index
"""
class Solution:
    def targetIndices(self, A: List[int], t: int) -> List[int]:
        A.sort()
        return [i for i, a in enumerate(A) if t==a]