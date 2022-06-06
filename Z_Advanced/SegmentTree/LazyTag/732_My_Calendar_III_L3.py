""" https://leetcode.com/problems/my-calendar-iii/
Range max add + global max query

1. build a tree-based segment tree whose root node is ranging from 0 to 10**9+1.
2. update the range max by lazy tag
3. simply return the root(global)'s mx

Note that we should only update all the related nodes for [lo, hi), so the parameter of rangeAdd is (lo, ho-1)
"""
class Node:
    def __init__(self, lo, hi, mx=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.mx = mx # range sum or range max
        self.lazy = lazy # lazy propagation for range update
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A: self.root = self.buildTree(A, lo, hi)
        else: self.root = Node(lo, hi)
        
    def rangeAdd(self, node, val, lo, hi):
        # range matched
        if node.lo == lo and node.hi == hi:
            node.mx += val
            node.lazy += val
            return 
        
        m = (node.lo + node.hi) // 2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, node.lazy)
            node.right = Node(m+1, node.hi, node.lazy, node.lazy)
        else:
            node.left.mx += node.lazy
            node.left.lazy += node.lazy
            node.right.mx += node.lazy
            node.right.lazy += node.lazy
		# reset lazy tag
        node.lazy = 0
        # update the children
        if m>=hi:
            self.rangeAdd(node.left, val, lo, hi)
        elif m<lo:
            self.rangeAdd(node.right, val, lo, hi)
        else:
            self.rangeAdd(node.left, val, lo, m)
            self.rangeAdd(node.right, val, m+1, hi)
        # update the node
        node.mx = max(node.left.mx, node.right.mx)
        return
    
    
class MyCalendarThree:
    def __init__(self):
        self.ST = SegmentTree(0, 10**9+1)

    def book(self, lo: int, hi: int) -> int:
        self.ST.rangeAdd(self.ST.root, 1, lo, hi-1)
        return self.ST.root.mx