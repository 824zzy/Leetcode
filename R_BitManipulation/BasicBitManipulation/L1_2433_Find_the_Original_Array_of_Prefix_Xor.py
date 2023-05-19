""" https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
simulate the process forwardly
"""
from header import *

class Solution:
    def findArray(self, A: List[int]) -> List[int]:
        ans = [A[0]]
        x = A[0]
        for i in range(1, len(A)):
            xx = x ^ A[i]
            ans.append(xx)
            x ^= xx
        return ans
    
    
# solution from lee: construct the arr from pref reversely
class Solution:
    def findArray(self, A):
        for i in range(len(A) - 1, 0, -1):
            A[i] ^= A[i - 1]
        return A