""" https://leetcode.com/problems/excel-sheet-column-title/
Euclidean algorithm（辗转相除）
Note that first number is 1 (instead of 0).
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n:
            n, rm = divmod(n-1, 26)
            ans = chr(ord('A')+rm) + ans
        return ans