""" L1: 
if n&*(n-1) is true, n must be 2**x;
10101...101 (i.e. 1431655765 in decimal)
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and not n&(n-1) and n&1431655765
    
# Pythonic solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        b_num = bin(num)
        return (len(b_num)-2)%2!=0 and b_num[2]=='1' and '1' not in b_num[3:]