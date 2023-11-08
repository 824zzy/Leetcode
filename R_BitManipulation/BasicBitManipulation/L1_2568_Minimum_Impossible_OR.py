""" https://leetcode.com/problems/minimum-impossible-or/
based on observation, the answer can only be 2**x
"""
from header import *

class Solution:
    def minImpossibleOR(self, A: List[int]) -> int:
        A = set(A)
        for i in range(31):
            if 1<<i not in A:
                return 1<<i
            
        
        
        
"""
[2,1]
[5,3,2]
[1,25,2,72]
[4,32,16,8,8,75,1,2]
"""
"""
101
011
010
"""