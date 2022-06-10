""" https://leetcode.com/problems/range-sum-query-mutable/
segment tree template
"""
# ZWK segment tree
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0]*2*self.n

    def _build(self, A):
        for i in range(self.n): 
            self.T[i+self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2*i] + self.T[2*i+1]
    

    def _set(self, i, val):
        i += self.n
        diff = val - self.T[i]
        while i:
            self.T[i] += diff
            i //= 2
            
    def rangeSum(self, l, r):
        ans = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            if l%2: ans, l = ans+self.T[l], l+1 # if l is right child
            if not r%2: ans, r = ans+self.T[r], r-1 # if r is left child
            l, r = l//2, r//2
        return ans
            
class NumArray:
    def __init__(self, nums: List[int]):
        self.ST = SegmentTree(len(nums))
        self.ST._build(nums)
        
    def update(self, index: int, val: int) -> None:
        self.ST._set(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.ST.rangeSum(left, right)

# tree-based segment tree
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None):
        self.lo = lo
        self.hi = hi
        self.sm = sm # range sum from low to high
        self.mx = mx # range max from low to high
        self.lazy = lazy # lazy propagation for range update
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A: self.root = self._build(lo, hi, A)
        else: self.root = Node(lo, hi)

    def _build(self, lo, hi, A):
        node = Node(lo, hi)
        if lo==hi: 
            node.sm = A[lo]
        else:
            m = (lo+hi)//2
            node.left = self._build(lo, m, A)
            node.right = self._build(m+1, hi, A)
            node.sm = node.left.sm + node.right.sm
        return node

    def _set(self, node, i, val):
        if node.lo==node.hi:
            node.sm = val
            node.mx = val
            return 
        m = (node.lo+node.hi)//2
        # dynamic growing without building tree
        if not node.left and not node.right: 
            node.left = Node(node.lo, m)
            node.right = Node(m+1, node.hi)

        if i<=m: self._set(node.left, i, val)
        elif i>m: self._set(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)
    
    def _sumQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.sm
        m = (node.lo+node.hi)//2
        if node.lazy!=None: return node.lazy*(hi-lo+1)
        if hi<=m: return self._sumQuery(node.left, lo, hi)
        elif lo>m: return self._sumQuery(node.right, lo, hi)
        else: return self._sumQuery(node.left, lo, m)+self._sumQuery(node.right, m+1, hi)

            
class NumArray:
    def __init__(self, A: List[int]):
        self.ST = SegmentTree(0, len(A)-1, A)
        
    def update(self, index: int, val: int) -> None:
        self.ST._set(self.ST.root, index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.ST._sumQuery(self.ST.root, left, right)