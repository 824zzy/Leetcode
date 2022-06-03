# Ultimate Segment Tree Templates

TODO: Sweepline, monotonic stack, and (add more type of problems can be solve by segment tree).

There are three types of segment tree implementations: array-based, tree-based and ZKW segment tree.

This template covers all the functions that may used in segment tree problem. Overall,

1. `init`: initiate the size of segment tree.
2. `buildTree`: Given an array, initiate leaves and nodes. Time complexity: O(n)
3. `update`: update values from leave to root, note that the update can be add or set. Time complexity: O(logn)
4. `rangeSum`: TODO:. O(logn+k)

## Property

Suppose we have a segment tree with `N` leaves:

1. At most `log(N)` layers
2. `2N-1` segments(nodes)
3. Given root index = `[1]`, for each node `o`, its left child index is `o*2`, its right child index is `o*2+1`
4. Given root index = `[1]`, the i-th leaf index is `N+i`

## General Segment Tree

### Tree based segment tree

``` py
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.sm = sm # range sum from low to high
        self.mx = mx # range max from low to high
        self.lazy = lazy # lazy propagation for range update
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        if A: self.root = self.buildTree(lo, hi, A)
        else: self.root = Node(lo, hi)

    def buildTree(self, lo, hi, A):
        node = Node(lo, hi)
        if lo==hi: 
            node.sm = A[lo]
            node.mx = A[lo]
        else:
            m = (lo+hi)//2
            node.left = self.buildTree(lo, m, A)
            node.right = self.buildTree(m+1, hi, A)
            node.sm = node.left.sm + node.right.sm
            node.mx = max(node.left.mx, node.right.mx)
        return node
    
    def update(self, node, i, val):
        if node.lo==node.hi:
            node.sm += val # or set node.sm = val
            node.mx += val # or set node.mx = val
            return 
        m = (node.lo+node.hi)//2
        # dynamic growing without building tree
        if not node.left and not node.right: 
            node.left = Node(node.lo, m)
            node.right = Node(m+1, node.hi)

        if i<=m: self.update(node.left, i, val)
        elif i>m: self.update(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)
        
    def rangeAdd(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.sm += val
            node.mx += val
            node.lazy += val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, node.lazy, node.lazy)
            node.right = Node(m+1, node.hi, node.lazy, node.lazy, node.lazy)
        else:
            node.left.sm += node.lazy
            node.left.mx += node.lazy
            node.left.lazy += node.lazy
            node.right.sm += node.lazy
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
        node.sm = node.left.sm+node.right.sm
        node.mx = max(node.left.mx, node.right.mx, node.mx)
        return

    def rangeAddSum(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.sm
        m = (node.lo+node.hi)//2
        if hi<=m: return node.lazy+self.rangeAddSum(node.left, lo, hi)
        elif lo>m: return node.lazy+self.rangeAddSum(node.right, lo, hi)
        else: return node.lazy+self.rangeAddSum(node.left, lo, m)+self.rangeAddSum(node.right, m+1, hi)

    def rangeAddmax(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if hi<=m: return node.lazy+self.rangeAddmax(node.left, lo, hi)
        elif lo>m: return node.lazy+self.rangeAddmax(node.right, lo, hi)
        else: return node.lazy+max(self.rangeAddmax(node.left, lo, m), self.rangeAddmax(node.right, m+1, hi))

    def rangeSet(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.sm = val
            node.mx = val
            node.lazy = val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, node.lazy, node.lazy)
            node.right = Node(m+1, node.hi, node.lazy, node.lazy, node.lazy)
        else:
            node.left.sm = max(node.left.sm, node.lazy)
            node.left.mx = max(node.left.mx, node.lazy)
            node.left.lazy = max(node.left.lazy, node.lazy)
            node.right.sm = max(node.right.sm, node.lazy)
            node.right.mx = max(node.right.mx, node.lazy)
            node.right.lazy = max(node.right.lazy, node.lazy)
        # reset lazy tag
        node.lazy = 0
        # update the children
        if m>=hi:
            self.rangeSet(node.left, val, lo, hi)
        elif m<lo:
            self.rangeSet(node.right, val, lo, hi)
        else:
            self.rangeSet(node.left, val, lo, m)
            self.rangeSet(node.right, val, m+1, hi)
        # update the node
        node.sm = node.left.sm+node.right.sm
        node.mx = max(node.left.mx, node.right.mx, node.mx)
        return

    def rangeSetSum(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.sm
        m = (node.lo+node.hi)//2
        if hi<=m: return max(node.lazy, self.rangeSetSum(node.left, lo, hi))
        elif lo>m: return max(node.lazy, self.rangeSetSum(node.right, lo, hi))
        else: return max(node.lazy, self.rangeSetSum(node.left, lo, m), self.rangeSetSum(node.right, m+1, hi))
    
    def rangeSetMax(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if hi<=m: return max(node.lazy, self.rangeSetMax(node.left, lo, hi))
        elif lo>m: return max(node.lazy, self.rangeSetMax(node.right, lo, hi))
        else: return max(node.lazy, self.rangeSetMax(node.left, lo, m), self.rangeSetMax(node.right, m+1, hi))
```

### Array based segment tree

``` py
TODO:
```

## ZKW Segment Tree

``` py
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0]*2*self.n

    def buildTree(self, A):
        for i in range(self.n): 
            self.T[i+self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2*i] + self.T[2*i+1]
    
    def update(self, i, val):
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
```

## Reference

- [花花酱 Segment Tree 线段树 - 刷题找工作 SP14](https://www.youtube.com/watch?v=rYBtViWXYeI)
- [https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches](https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches)
- [Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
- [残酷小讲座：线段树 by OTTFF](https://www.youtube.com/watch?v=s7vZDDpeR7w)