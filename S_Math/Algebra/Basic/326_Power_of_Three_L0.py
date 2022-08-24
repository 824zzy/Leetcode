""" https://leetcode.com/problems/power-of-three/
3^20 is exceeding Integer_Range, so 3^19 is the highest power in Integer Range 
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:        
        maxP = 3 ** 19
        return n > 0 and maxP%n == 0


# check by while loop
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        while x<n:
            x *= 3
        return x==n