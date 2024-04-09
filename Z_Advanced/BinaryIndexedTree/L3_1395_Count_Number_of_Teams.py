""" https://leetcode.com/problems/count-number-of-teams/discuss/878333/Python-Fenwick-tree-O(NlogN)-solution-beats-99
index-based BIT
"""


class BIT:
    def __init__(self, n):
        self.A = [0] * (n + 1)

    def sum(self, k):
        sm = 0
        k += 1
        while k:
            sm += self.A[k]
            k -= k & -k
        return sm

    def add(self, k, x):
        k += 1
        while k < len(self.A):
            self.A[k] += x
            k += k & -k


class Solution:
    def numTeams(self, A: List[int]) -> int:
        bit1, bit2 = BIT(len(A)), BIT(len(A))
        ans = 0
        A = sorted((x, i) for i, x in enumerate(A))
        N = len(A)
        for _, i in reversed(A):
            bit2.add(N - i - 1, 1)

        ans = 0
        for _, i in A:
            bit2.add(N - i - 1, -1)
            a, b = bit1.sum(i), bit2.sum(N - i - 1)
            ans += a * b + (i - a) * (N - i - b - 1)
            bit1.add(i, 1)
        return ans
