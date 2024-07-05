from collections import Counter


class Solution:
    def maxSumRangeQuery(self, A, req):
        n = len(A)
        count = [0] * (n + 1)
        for i, j in req:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(A)):
            res += v * c
        return res % (10 ** 9 + 7)
