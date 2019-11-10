""" Yahoo
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        str_n = bin(n)[2:]
        for i in range(len(str_n)-1):
            if str_n[i] == str_n[i+1]:
                return False
        return True
        
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        for i in range(1, len(n), 2):
            try:
                if n[i]!='0' or n[i-1]=='0' or n[i+1]=='0':
                    return False
            except:
                if n[i]!='0' or n[i-1]=='0':
                    return False
        return True