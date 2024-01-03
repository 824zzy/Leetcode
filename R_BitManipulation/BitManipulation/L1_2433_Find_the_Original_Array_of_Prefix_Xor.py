""" https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
simulate the process reversely
"""
from header import *

class Solution:
    def findArray(self, A: List[int]) -> List[int]:
        pre1 = 0
        ans = []
        for x in A:
            pre2 = pre1^x
            ans.append(pre2)
            pre1 ^= pre2
        return ans
    
    
# solution from lee: construct the arr from pref reversely
class Solution:
    def findArray(self, A):
        for i in range(len(A) - 1, 0, -1):
            A[i] ^= A[i - 1]
        return A