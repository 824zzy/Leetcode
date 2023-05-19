""" https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
use a hash table to store the sparse vector
"""
from header import *

class SparseVector:
    
    def __init__(self, A: List[int]):
        self.vec = {i: A[i] for i in range(len(A)) if A[i]}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, A: 'SparseVector') -> int:
        ans = 0
        for k, v1 in self.vec.items():
            if k in A.vec:
                ans += v1*A.vec[k]
        return ans