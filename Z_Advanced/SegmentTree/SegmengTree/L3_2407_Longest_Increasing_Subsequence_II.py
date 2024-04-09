""" https://leetcode.com/problems/longest-increasing-subsequence-ii/
Consider this problem to use nums[i] in the dp since 1 <= nums[i], k <= 10**5,
so dp[x] = max(dp[y]+1), where y ~ [x-k, x].
The best data structure for this problem is Segment Tree.
"""
from header import *

# ZWK segment tree template


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0] * 2 * self.n

    def _set(self, i, val):
        i += self.n
        while i:
            self.T[i] = max(val, self.T[i])
            i //= 2

    def rangeMax(self, l, r):
        ans = 0
        l, r = l + self.n, r + self.n
        while l <= r:
            if l % 2:
                ans, l = max(ans, self.T[l]), l + 1  # if l is right child
            if not r % 2:
                ans, r = max(ans, self.T[r]), r - 1  # if r is left child
            l, r = l // 2, r // 2
        return ans


class Solution:
    def lengthOfLIS(self, A: List[int], k: int) -> int:
        n = max(A) + 1
        ST = SegmentTree(n)
        ans = 1
        for x in A:
            mx = ST.rangeMax(max(x - k, 0), x - 1)
            ST._set(x, mx + 1)
            ans = max(ans, mx + 1)
        return ans


# Tree based segment tree: TLE
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None):  # lazy=0 for rangeAdd
        self.lo = lo
        self.hi = hi
        self.mx = mx  # range max from low to high
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A:
            self.root = self._build(lo, hi, A)
        else:
            self.root = Node(lo, hi)

    def _set(self, node, i, val):
        if node.lo == node.hi:
            node.mx = val
            return
        m = (node.lo + node.hi) // 2
        # dynamic growing without building tree
        if not node.left and not node.right:
            node.left = Node(node.lo, m)
            node.right = Node(m + 1, node.hi)

        if i <= m:
            self._set(node.left, i, val)
        elif i > m:
            self._set(node.right, i, val)
        node.mx = max(node.left.mx, node.right.mx)

    def _maxQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.mx
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return self._maxQuery(node.left, lo, hi)
        elif lo > m:
            return self._maxQuery(node.right, lo, hi)
        else:
            return max(
                self._maxQuery(
                    node.left, lo, m), self._maxQuery(
                    node.right, m + 1, hi))


class Solution:
    def lengthOfLIS(self, A: List[int], k: int) -> int:
        n = max(A)
        ST = SegmentTree(0, n)

        for i, x in enumerate(A):
            mx = ST._maxQuery(ST.root, x - k, x - 1)
            ST._set(ST.root, x, mx + 1)
        return ST._maxQuery(ST.root, 1, n)


""" 5 4 1 2 2 2
[4,2,1,4,3,4,5,8,15]
3
[7,4,5,1,8,12,4,7]
5
[1,5]
1
[2,6,15]
5
[1,4,7,15,5]
1
[10,3,20,2,16,12]
4
"""
