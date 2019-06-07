""" Usage of `format` funtion
convert n to 32 bits unsigned integer.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = "{0:032b}".format(n)
        return int(a[::-1], 2)