""" https://leetcode.com/problems/power-of-four/
observation: 
power of 4 must be "1XX..XX" where the length of X is even
"""
from header import *

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        if n<=0: return False
        s = str(bin(n)[2:])
        return len(s)&1 and set(s[1:])==set('0')


# naive while loop solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0: return False
        while n!=1:
            if n%4: return False
            n //= 4
        return True