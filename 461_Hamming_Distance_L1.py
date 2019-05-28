""" straightforward and buildtin function
zfill(n): padding zero in the front
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit_x = bin(x)[2:]
        bit_y = bin(y)[2:]
        if len(bit_x) > len(bit_y):
            bit_y = bit_y.zfill(len(bit_x))
        else:
            bit_x = bit_x.zfill(len(bit_y))
            
        res = 0
        for i, j in zip(bit_x, bit_y):
            if i != j:
                res += 1
        return res

""" bit-manipulation trick
"""
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')


""" basic answer
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x or y:
            ans = ans + (x%2 ^ y%2)
            x = x / 2
            y = y / 2
        return ans
        