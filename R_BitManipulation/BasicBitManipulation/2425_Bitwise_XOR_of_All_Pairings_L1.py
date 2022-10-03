""" https://leetcode.com/problems/bitwise-xor-of-all-pairings/
There are three conditions:
1. If the length of num1 and num2 are both even, then the XOR of all pairings is 0.
2. If the length of num1 and num2 are both odd, then the XOR of all pairings is the XOR of all elements.
3. If one of the length is even and the other is odd, then the XOR of all pairings is the XOR of the even one.
"""
from header import *

class Solution:
    def xorAllNums(self, A: List[int], B: List[int]) -> int:
        if len(A)%2==0 and len(B)%2==0: 
            return 0
        if len(A)%2==1 and len(B)%2==1: 
            return reduce(lambda a, b: a^b, A+B)
        else:
            if len(A)%2==0: return reduce(lambda a, b: a^b, A)
            else: return reduce(lambda a, b: a^b, B)
        
"""
[2,1,3]
[10,2,5,0]
[1,2]
[3,4]
[8,6,29,2,26,16,15,29]
[24,12,12]
[25,29,3,10,0,15,2]
[12]
"""