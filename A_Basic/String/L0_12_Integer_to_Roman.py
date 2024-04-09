""" https://leetcode.com/problems/integer-to-roman/submissions/
greedily choose the largest roman numeral that is less than or equal to the number
"""


class Solution:
    def intToRoman(self, n: int) -> str:
        mp = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ]

        ans = ''
        for k, v in mp:
            x, n = divmod(n, k)
            ans += v * x
        return ans
