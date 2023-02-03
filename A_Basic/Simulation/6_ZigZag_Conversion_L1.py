""" https://leetcode.com/problems/zigzag-conversion/
simulation
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        ans = [''] * numRows
        row = 0
        for c in s:
            ans[row] += c
            if row==0:
                step = 1
            elif row==numRows-1:
                step = -1
            row += step
        return ''.join(ans)
