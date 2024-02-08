""" https://leetcode.com/problems/base-7/
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: return '0'
        
        ans = ''
        n = abs(num)
        while n:
            ans = str(n%7)+ans
            n //= 7
        return '-'*(num<0)+ans