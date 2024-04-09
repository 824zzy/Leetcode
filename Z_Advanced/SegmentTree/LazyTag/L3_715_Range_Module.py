""" https://leetcode.com/problems/range-module/
Range sum set + range sum query
"""


class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None):
        # def __init__(self, lo, hi, sm=0, mx=0, lazy=None):
        self.lo = lo
        self.hi = hi
        self.sm = sm  # range sum from low to high
        self.mx = mx  # range max from low to high
        self.lazy = lazy  # lazy propagation for range update
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        self.root = Node(lo, hi)

    def rangeSetSum(self, node, val, lo, hi):
        if node.lo == lo and node.hi == hi:
            node.sm = val * (node.hi - node.lo + 1)
            node.lazy = val
            return

        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            if node.lazy is not None:
                node.left = Node(node.lo, m, node.lazy *
                                 (m - node.lo + 1), None, node.lazy)
                node.right = Node(m + 1, node.hi, node.lazy *
                                  (node.hi - m), None, node.lazy)
            else:
                node.left = Node(node.lo, m)
                node.right = Node(m + 1, node.hi)
        elif node.lazy is not None:
            node.left.sm = node.lazy * (m - node.lo + 1)
            node.left.lazy = node.lazy
            node.right.sm = node.lazy * (node.hi - m)
            node.right.lazy = node.lazy
        # reset lazy tag
        node.lazy = None
        # update the children
        if m >= hi:
            self.rangeSetSum(node.left, val, lo, hi)
        elif m < lo:
            self.rangeSetSum(node.right, val, lo, hi)
        else:
            self.rangeSetSum(node.left, val, lo, m)
            self.rangeSetSum(node.right, val, m + 1, hi)
        # update the node
        node.sm = node.left.sm + node.right.sm
        return

    def rangeSetSumQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m:
            if node.lazy is not None:
                return node.lazy * (hi - lo + 1)
            else:
                return self.rangeSetSumQuery(node.left, lo, hi)
        elif lo > m:
            if node.lazy is not None:
                return node.lazy * (hi - lo + 1)
            else:
                return self.rangeSetSumQuery(node.right, lo, hi)
        else:
            if node.lazy is not None:
                return node.lazy * (hi - lo + 1)
            else:
                return self.rangeSetSumQuery(
                    node.left, lo, m) + self.rangeSetSumQuery(node.right, m + 1, hi)


class RangeModule:
    def __init__(self):
        self.ST = SegmentTree(0, 10**9 + 1)

    def addRange(self, left: int, right: int) -> None:
        self.ST.rangeSetSum(self.ST.root, 1, left, right - 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.ST.rangeSetSumQuery(
            self.ST.root, left, right - 1) == right - left

    def removeRange(self, left: int, right: int) -> None:
        self.ST.rangeSetSum(self.ST.root, 0, left, right - 1)
