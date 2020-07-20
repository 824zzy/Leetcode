""" Usage of `format` funtion
convert n to 32 bits unsigned integer.
"""
class Solution:
    def reverseBits(self, n):
        n = str(bin(n))[:2]
        n = n.zfill(32)[::-1]
        return int(n, 2)