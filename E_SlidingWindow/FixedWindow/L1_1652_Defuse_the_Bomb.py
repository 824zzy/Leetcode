""" https://leetcode.com/problems/defuse-the-bomb/
"""

from header import *


class Solution:
    def decrypt(self, A: List[int], k: int) -> List[int]:
        l = len(A)
        A = A * 2
        f = False
        if k < 0:
            f = True
            k = -k
        sm = sum(A[:k])
        ans = [0] * len(A)
        for i in range(k, len(A)):
            i = i % l
            ans[i] = sm
            sm -= A[i - k]
            sm += A[i]

        if not f:
            return ans[k + 1 : l] + ans[: k + 1]
        else:
            return ans[:l]


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0:
            k, code = abs(k), code[::-1]
            return [
                sum([code[j % len(code)] for j in range(i + 1, i + k + 1)])
                for i in range(len(code))
            ][::-1]
        else:
            return [
                sum([code[j % len(code)] for j in range(i + 1, i + k + 1)])
                for i in range(len(code))
            ]
