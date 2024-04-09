""" https://leetcode.com/problems/monotone-increasing-digits/
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        A = list(map(int, str(n)))
        stk = []
        for i, x in enumerate(A):
            while stk and stk[-1] > x:
                x = stk.pop() - 1
            stk.append(x)
            if len(stk) <= i:
                break
        return int(''.join(map(str, stk)).ljust(len(A), '9'))


"""
332 = 999=>399=>299
10 = 99>19>9
321 = 999=>399=>299
"""
