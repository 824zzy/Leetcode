""" https://leetcode.com/problems/largest-odd-number-in-string/
enumerate from right to left
"""


class Solution:
    def largestOddNumber(self, A: str) -> str:
        try:
            return A[: next(i for i in reversed(range(len(A))) if int(A[i]) & 1) + 1]
        except BaseException:
            return ""


"""
"52"
"4206"
"35427"
"""
