""" https://leetcode.com/problems/nth-digit/
learn from ye: https://leetcode.com/problems/nth-digit/discuss/828924/Python3-O(logN)-solution

Observe that there are 9 numbers with 1 digit, 90 numbers with 2 digits, 900 numbers with 3 digits, ...
so, the answer is the r-th digits in q-th number start from base.
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits 
            n -= 9*base*digit
            digit += 1
            base *= 10 
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])
