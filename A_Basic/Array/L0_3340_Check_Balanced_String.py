""" https://leetcode.com/problems/check-balanced-string/
array simulation
"""


class Solution:
    def isBalanced(self, A: str) -> bool:
        o, e = 0, 0
        for i in range(len(A)):
            if i & 1:
                e += int(A[i])
            else:
                o += int(A[i])
        return o == e
