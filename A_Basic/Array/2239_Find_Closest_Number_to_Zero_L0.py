""" https://leetcode.com/problems/find-closest-number-to-zero/
use abs and x as min's key function
"""
class Solution:
    def findClosestNumber(self, A: List[int]) -> int:
        return min(A, key=lambda x: (abs(x), -x))