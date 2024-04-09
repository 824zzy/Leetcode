""" https://leetcode.com/problems/describe-the-painting/
"""
from header import *


class Solution:
    def splitPainting(self, A: List[List[int]]) -> List[List[int]]:
        SL = []
        for i, j, k in A:
            SL.extend([(i, k), (j, -k)])
        SL.sort()

        cnt = 0
        seen = Counter()
        for i, x in SL:
            cnt += x
            seen[i] = cnt
        A = sorted(seen.items())

        ans = []
        for i in range(len(A) - 1):
            if A[i][1] != 0:
                ans.append([A[i][0], A[i + 1][0], A[i][1]])
        return ans


# elegant implementation without using Counter by ye
class Solution:
    def splitPainting(self, A: List[List[int]]) -> List[List[int]]:
        SL = []
        for i, j, k in A:
            SL.extend([(i, k), (j, -k)])
        SL.sort()

        cnt = 0
        pre = 0
        ans = []
        for i, x in SL:
            if pre < i and cnt:
                ans.append([pre, i, cnt])
            pre = i
            cnt += x
        return ans
