""" https://leetcode.com/problems/maximum-swap/
max digit after min digit by greedy
"""


class Solution:
    def maximumSwap(self, A: int) -> int:
        A = list(map(int, list(str(A))))
        mi = ma = mima = None
        for i in reversed(range(len(A))):
            # find max digit
            if not ma or A[i] > A[ma]:
                ma = i
            # find min digit before max digit
            if A[i] < A[ma]:
                mi, mima = i, ma

        if mima:
            A[mima], A[mi] = A[mi], A[mima]
        return int("".join(map(str, A)))
