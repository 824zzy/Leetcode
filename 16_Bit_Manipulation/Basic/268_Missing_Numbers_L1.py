""" https://leetcode.com/problems/missing-number/
variance of 136
XOR each number with complete list
"""
class Solution:
    def missingNumber(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            ans ^= (i+1) ^ A[i]
        return ans