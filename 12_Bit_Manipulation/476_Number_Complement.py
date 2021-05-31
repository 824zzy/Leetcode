""" L1
"""
class Solution:
    def findComplement(self, num: int) -> int:
        num = str(bin(num))[2:]
        s = ''.join(['0' if n=='1'else '1' for n in num ])
        return int(s, 2)

class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(len(bin(num))-2):
            num = num^(2**i)
        return num