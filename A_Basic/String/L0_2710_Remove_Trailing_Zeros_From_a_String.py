""" https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
implement rstrip
"""


class Solution:
    def removeTrailingZeros(self, A: str) -> str:
        # return A.rstrip('0')
        for i in reversed(range(len(A))):
            if A[i] != "0":
                return A[: i + 1]
