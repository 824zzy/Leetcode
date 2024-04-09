""" https://leetcode.com/problems/power-of-two/
check if only the first bit is 1 by finding the number from the lowest bit to the end.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n == (n & -n)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n & 1:
                return False
            n >>= 1
        return True
