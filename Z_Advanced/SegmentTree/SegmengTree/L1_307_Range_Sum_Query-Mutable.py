""" https://leetcode.com/problems/range-sum-query-mutable/
segment tree template for single point set and sum query
"""
from header import *

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
    

# array-based segment tree
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.T = [0] * (4 * self.n)
        self.todo = [0] * (4 * self.n)
        self.build(1, 1, self.n)
        
    def build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.T[o] = self.nums[l - 1]
            return
        m = (l + r) // 2
        self.build(o * 2, l, m)
        self.build(o * 2 + 1, m + 1, r)
        self.maintain(o)
    
    def do(self, o: int, l: int, r: int, val: int) -> None:
        if val!=None:
            self.T[o] = val
            self.todo[o] = val
            
    def maintain(self, o):
        self.T[o] = self.T[o*2]+self.T[o*2+1]
        
    def query_and_set(self, o, l, r, L, R, val):
        if L <= l and r <= R:
            ans = self.T[o]
            self.do(o, l, r, val)
            return ans
        m = (l + r) // 2
        if self.todo[o]:
            self.do(o * 2, l, m, val)
            self.do(o * 2 + 1, m + 1, r, val)
            self.todo[o] = None
        ans = 0
        if m >= L: 
            ans += self.query_and_set(o*2, l, m, L, R, val)
        if m < R: 
            ans += self.query_and_set(o*2+1, m+1, r, L, R, val)
        self.maintain(o)
        return ans
        

    def update(self, index: int, val: int) -> None:
        self.query_and_set(1, 1, self.n, index+1, index+1, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query_and_set(1, 1, self.n, left+1, right+1, None)
        
"""
["NumArray","sumRange","update","sumRange"]
[[[1,3,5]],[0,2],[1,2],[0,2]]
["NumArray","update","sumRange","sumRange","update","sumRange"]
[[[9,-8]],[0,3],[1,1],[0,1],[1,-3],[0,1]]
["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
[[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
"""