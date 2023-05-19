""" https://leetcode.com/problems/clumsy-factorial/
cheating solution using eval()
"""
class Solution:
    def clumsy(self, n: int) -> int:
        ops = ['*', '//', '+', '-']
        d = 0
        expr = ''
        for i in reversed(range(2, n+1)):
            expr += str(i)+ops[d]
            d = (d+1)%4
        return eval(expr+'1')