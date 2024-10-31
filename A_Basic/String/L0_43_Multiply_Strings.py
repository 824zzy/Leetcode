""" https://leetcode.com/problems/multiply-strings/
"""


class Solution:
    def multiply(self, A: str, B: str) -> str:
        A, B = A[::-1], B[::-1]
        a, b = 0, 0
        for i in range(len(A)):
            a += (ord(A[i]) - 48) * (10 ** i)
        for i in range(len(B)):
            b += (ord(B[i]) - 48) * (10 ** i)
        return str(a * b)
