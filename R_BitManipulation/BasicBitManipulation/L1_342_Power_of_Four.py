""" https://leetcode.com/problems/power-of-four/

"""
from header import *

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n.bit_count()==1 and n.bit_length()%2==1
    
# num & (num-1): set lowest 1 bit to 0; 0x55555555: 0101 0101 0101 0101 0101 0101 0101 0101, aim to only keep 1 bit in odd position
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not (num & (num-1)) and num & 0x55555555


# naive while loop solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0: return False
        while n!=1:
            if n%4: return False
            n //= 4
        return True