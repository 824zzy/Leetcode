""" https://leetcode.com/problems/count-good-triplets-in-an-array/
TODO: from: https://leetcode.com/problems/count-good-triplets-in-an-array/discuss/1783431/Python3-sortedlist-and-fenwick-tree
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
    def goodTriplets(self, A, B):
        mp = {x: i for i, x in enumerate(A)}
        N = len(A)
        bit = BIT(N)
        ans = 0

        for i, x in enumerate(B):
            x = mp[x]
            left = bit.sum(x)
            right = (N - 1 - x) - (bit.sum(N - 1) - left)
            ans += left * right
            bit.add(x, 1)
        return ans
