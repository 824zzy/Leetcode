""" https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
greedy sorting
"""
from header import *

class Solution:
    def maxCoins(self, A: List[int]) -> int:
        A.sort(reverse=True)
        n = len(A)//3
        return sum(A[1::2][:n])
    
"""
[2,4,1,2,7,8]
[2,4,5]
[9,8,7,6,5,1,2,3,4]

981 762 543
"""