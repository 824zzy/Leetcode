""" https://leetcode.com/problems/maximum-69-number/description/
simulation
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        A = list(str(num))
        for i in range(len(A)):
            if A[i] == '6':
                A[i] = '9'
                break
        return ''.join(A)
