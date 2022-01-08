""" https://leetcode.com/problems/car-pooling/
"""
class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        A = [x for n, i, j in A for x in [[i, n], [j, -n]]]
        for i, v in sorted(A):
            c -= v
            if c<0: return False
        return True