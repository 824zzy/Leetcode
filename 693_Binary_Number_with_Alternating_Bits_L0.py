""" simple bit trick
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        str_n = bin(n)[2:]
        for i in range(len(str_n)-1):
            if str_n[i] == str_n[i+1]:
                return False
        return True
        