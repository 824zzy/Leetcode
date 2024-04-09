""" https://leetcode.com/problems/reverse-pairs/
Basic segment tree: discretization + singe add + query sum
and slightly use binary search
"""


class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None):
        self.lo = lo
        self.hi = hi
        self.sm = sm  # range sum from low to high
        self.mx = mx  # range max from low to high
        self.lazy = lazy  # lazy propagation for range update
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A:
            self.root = self._build(lo, hi, A)
        else:
            self.root = Node(lo, hi)

    def _add(self, node, i, val):
        if node.lo == node.hi:
            node.sm += val
            node.mx += val
            return
        m = (node.lo + node.hi) // 2
        # dynamic growing without building tree
        if not node.left and not node.right:
            node.left = Node(node.lo, m)
            node.right = Node(m + 1, node.hi)

        if i <= m:
            self._add(node.left, i, val)
        elif i > m:
            self._add(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)

    def _sumQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return self._sumQuery(node.left, lo, hi)
        elif lo > m:
            return self._sumQuery(node.right, lo, hi)
        else:
            return self._sumQuery(node.left, lo, m) + \
                self._sumQuery(node.right, m + 1, hi)


class Solution:
    def reversePairs(self, A: List[int]) -> int:
        _A = sorted(set(A))
        v2i = {x: i for i, x in enumerate(_A)}
        ST = SegmentTree(0, len(v2i) - 1)

        ans = 0
        for x in reversed(A):
            hi = bisect_left(_A, x / 2) - 1
            if hi >= 0:
                ans += ST._sumQuery(ST.root, 0, hi)
            ST._add(ST.root, v2i[x], 1)
        return ans
