""" L0
convert string "0"-"9" to numeric: ord(num_chr)-48
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        num1, num2 = list(num1)[::-1], list(num2)[::-1]
        for i in range(len(num1)):
            n1 += (ord(num1[i])-48)*(10**i)
        
        for i in range(len(num2)):
            n2 += (ord(num2[i])-48)*(10**i)

        return str(n1+n2)