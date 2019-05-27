""" more tricky solution: bit-feature
1. convert A to binary
    bin(number): '0b***'
2. make sure '1' in index 3 and all '0' in the rest.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n = str(bin(n))
        if n[2] == '1' and '1' not in n[3:]:
            return True
        else:
            return False


""" naive method using for loop
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a = 1
        while a <= n:
            if a == n:
                return True
            a *= 2
        return False
        
        