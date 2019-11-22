from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        maxP = 3 ** int(log(2**31-1, 3))
        return n > 0 and maxP%n == 0