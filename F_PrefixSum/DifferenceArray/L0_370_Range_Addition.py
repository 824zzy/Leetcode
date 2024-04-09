""" https://leetcode.com/problems/range-addition/
sweep line template
"""


class Solution:
    def getModifiedArray(self, n: int, updates: List[List[int]]) -> List[int]:
        A = [0] * n
        updates.sort()

        for i, j, x in updates:
            A[i] += x
            if j + 1 < n:
                A[j + 1] -= x

        cnt = 0
        for i, x in enumerate(A):
            cnt += A[i]
            A[i] = cnt
        return A
