""" https://leetcode.com/problems/create-sorted-array-through-instructions/
Sometime this solution TLE, it is better to consider BIT which is faster.

Add instructions to Segment Tree on the fly,
while compute the number of elements strictly less/great than current intruction.
"""
# ZKW segment tree implementation


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0] * 2 * self.n

    def update(self, i, val):
        i += self.n
        self.T[i] += val
        while i:
            if i % 2:
                l, r = i - 1, i
            else:
                l, r = i, i + 1
            self.T[i // 2] = self.T[l] + self.T[r]
            i //= 2

    def query(self, l, r):
        ans = 0
        l, r = l + self.n, r + self.n
        while l <= r:
            if l % 2:
                ans, l = ans + self.T[l], l + 1  # if l is right child
            if not r % 2:
                ans, r = ans + self.T[r], r - 1  # if r is left child
            l, r = l // 2, r // 2
        return ans


class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        lo, hi = 0, max(A)
        st = SegmentTree(hi + 1)
        ans = 0
        for i, x in enumerate(A):
            less = st.query(lo, x - 1)
            greater = st.query(x + 1, hi)
            ans += min(less, greater)
            st.update(x, 1)  # add
        return ans % (10 ** 9 + 7)


# Tree based segment tree implementation
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.sm = sm  # range sum from low to high
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, lo, hi):
        self.root = Node(lo, hi)

    def update(self, node, i, val):
        if node.lo == node.hi:
            node.sm += val  # or set node.sm = val
            return
        m = (node.lo + node.hi) // 2
        # dynamic growing
        if not node.left and not node.right:
            node.left = Node(node.lo, m)
            node.right = Node(m + 1, node.hi)

        if m >= i:
            self.update(node.left, i, val)
        elif m < i:
            self.update(node.right, i, val)
        node.sm = node.left.sm + node.right.sm

    def rangeSum(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2

        if m >= hi:
            return self.rangeSum(node.left, lo, hi)
        elif m < lo:
            return self.rangeSum(node.right, lo, hi)
        else:
            return self.rangeSum(node.left, lo, m) + self.rangeSum(
                node.right, m + 1, hi
            )


class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        lo, hi = 0, max(A)
        st = SegmentTree(0, hi)
        ans = 0
        for i, x in enumerate(A):
            less = st.rangeSum(st.root, 0, x - 1)
            greater = st.rangeSum(st.root, x + 1, hi)
            ans += min(less, greater)
            st.update(st.root, x, 1)
        return ans % (10 ** 9 + 7)
