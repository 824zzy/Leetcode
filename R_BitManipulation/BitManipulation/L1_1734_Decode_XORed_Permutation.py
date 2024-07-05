""" https://leetcode.com/problems/decode-xored-permutation/
"""
from header import *


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = reduce(xor, range(1, n + 1))
        odd = reduce(xor, encoded[1::2])
        perm = [total ^ odd]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
