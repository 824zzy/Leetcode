""" https://leetcode.com/problems/xor-queries-of-a-subarray/
use prefix XOR to solve the problem
"""



class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        A = list(accumulate(arr, xor, initial=0))
        return [A[r + 1] ^ A[l] for l, r in queries]
