""" Clouder
"""
class Solution:
    def findComplement(self, num: int) -> int:
        num = str(bin(num))[2:]
        s = ''.join(['0' if n=='1'else '1' for n in num ])
        return int(s, 2)
