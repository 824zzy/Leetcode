""" https://leetcode.com/problems/shifting-letters-ii/
use sweep line to count accumulated sum of each letter, then update the letters
"""
from header import *


class Solution:
    def shiftingLetters(self, s: str, A: List[List[int]]) -> str:
        n = len(s)
        SL = [0] * (n + 1)
        for i, j, k in A:
            if k == 1:
                SL[i] += 1
                SL[j + 1] -= 1
            else:
                SL[i] -= 1
                SL[j + 1] += 1

        ans = ""
        cnt = 0
        for i in range(n):
            cnt += SL[i]
            ans += chr((ord(s[i]) - 97 + cnt) % 26 + 97)
        return ans


# segment tree can solve this problem but will TLE
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=0):  # lazy=0 for rangeAdd
        self.lo = lo
        self.hi = hi
        self.sm = sm  # range sum from low to high
        self.lazy = lazy  # lazy propagation for range update
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A:
            self.root = self._build(lo, hi, A)
        else:
            self.root = Node(lo, hi)

    def rangeAddSum(self, node, val, lo, hi):
        if node.lo == lo and node.hi == hi:
            node.sm += val
            node.lazy += val
            return

        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, None, node.lazy)
            node.right = Node(m + 1, node.hi, node.lazy, None, node.lazy)
        else:
            node.left.sm += node.lazy
            node.left.lazy += node.lazy
            node.right.sm += node.lazy
            node.right.lazy += node.lazy
        node.lazy = 0
        # update the children
        if m >= hi:
            self.rangeAddSum(node.left, val, lo, hi)
        elif m < lo:
            self.rangeAddSum(node.right, val, lo, hi)
        else:
            self.rangeAddSum(node.left, val, lo, m)
            self.rangeAddSum(node.right, val, m + 1, hi)
        # update the node
        node.sm = node.left.sm + node.right.sm
        return

    def rangeAddSumQuery(self, node, lo, hi):
        if not node:
            return 0
        if node.lo == lo and node.hi == hi:
            return node.sm
        m = (node.lo + node.hi) // 2
        if hi <= m:
            return node.lazy + self.rangeAddSumQuery(node.left, lo, hi)
        elif lo > m:
            return node.lazy + self.rangeAddSumQuery(node.right, lo, hi)
        else:
            return (
                node.lazy
                + self.rangeAddSumQuery(node.left, lo, m)
                + self.rangeAddSumQuery(node.right, m + 1, hi)
            )


class Solution:
    def shiftingLetters(self, s: str, A: List[List[int]]) -> str:
        # build segment tree
        ST = SegmentTree(0, len(s))
        for i, j, d in A:
            d = -1 if d == 0 else 1
            ST.rangeAddSum(ST.root, d, i, j)
        # shift letters
        ans = ""
        for i, c in enumerate(s):
            ans += chr((ord(c) - 97 + ST.rangeAddSumQuery(ST.root, i, i)) % 26 + 97)
        return ans
