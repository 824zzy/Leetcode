""" https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
class Solution:
    def kWeakestRows(self, A: List[List[int]], k: int) -> List[int]:
        A = [[i, x.count(1)] for i, x in enumerate(A)]
        A.sort(key=lambda x: x[1])
        return [i for i, x in A[:k]]
        