from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3^20 is exceding  Integer_Range So 3^19 is the highest power in Integer Range 
        maxP = 3 ** 19
        return n > 0 and maxP%n == 0