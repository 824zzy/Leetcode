# Ultimate Segment Tree Templates

TODO: Sweepline, monotonic stack, and some of the binary search problems (add more type of problems can be solve by segment tree).

There are three types of segment tree implementations: array-based, tree-based and ZKW segment tree.

This template covers all the functions that may used in segment tree problem. Overall,

1. `init`: initiate the size of segment tree.
2. `_build`: Given an array, initiate leaves and nodes. Time complexity: O(n)
3. `_add`: add the value from leave to root. Time complexity: O(logn)
4. `_set`: set the value from leave to root. Time complexity: O(logn)
5. `rangeSum`: TODO:. O(logn+k)

## Property

Suppose we have a segment tree with `N` leaves:

1. At most `log(N)` layers
2. `2N-1` segments(nodes)
3. Given root index = `[1]`, for each node `o`, its left child index is `o*2`, its right child index is `o*2+1`
4. Given root index = `[1]`, the i-th leaf index is `N+i`

## General Segment Tree

### Tree based segment tree

TODO: update some of the templates

``` py
# Discretization from value to index if necessary
v2i = {x: i for i, x in enumerate(sorted(set(A)))}

class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=None): # lazy=0 for rangeAdd
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
            node.mx = A[lo]
        else:
            m = (lo+hi)//2
            node.left = self._build(lo, m, A)
            node.right = self._build(m+1, hi, A)
            node.sm = node.left.sm + node.right.sm
            node.mx = max(node.left.mx, node.right.mx)
        return node
    
    def _add(self, node, i, val):
        if node.lo==node.hi:
            node.sm += val
            node.mx += val
            return 
        m = (node.lo+node.hi)//2
        # dynamic growing without building tree
        if not node.left and not node.right: 
            node.left = Node(node.lo, m)
            node.right = Node(m+1, node.hi)

        if i<=m: self._add(node.left, i, val)
        elif i>m: self._add(node.right, i, val)
        node.sm = node.left.sm + node.right.sm
        node.mx = max(node.left.mx, node.right.mx)

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
        if hi<=m: return self._sumQuery(node.left, lo, hi)
        elif lo>m: return self._sumQuery(node.right, lo, hi)
        else: return self._sumQuery(node.left, lo, m)+self._sumQuery(node.right, m+1, hi)

    def _maxQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if hi<=m: return self._maxQuery(node.left, lo, hi)
        elif lo>m: return self._maxQuery(node.right, lo, hi)
        else: return max(self._maxQuery(node.left, lo, m), self._maxQuery(node.right, m+1, hi))

    """
    Range add sum & query
    """
    def rangeAddSum(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.sm += val
            node.lazy += val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, None, node.lazy)
            node.right = Node(m+1, node.hi, node.lazy, None, node.lazy)
        else:
            node.left.sm += node.lazy
            node.left.lazy += node.lazy
            node.right.sm += node.lazy
            node.right.lazy += node.lazy
        node.lazy = 0
        # update the children
        if m>=hi:
            self.rangeAddSum(node.left, val, lo, hi)
        elif m<lo:
            self.rangeAddSum(node.right, val, lo, hi)
        else:
            self.rangeAddSum(node.left, val, lo, m)
            self.rangeAddSum(node.right, val, m+1, hi)
        # update the node
        node.sm = node.left.sm + node.right.sm
        return

    def rangeAddSumQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.sm
        m = (node.lo+node.hi)//2
        if hi<=m: return node.lazy+self.rangeAddSumQuery(node.left, lo, hi)
        elif lo>m: return node.lazy+self.rangeAddSumQuery(node.right, lo, hi)
        else: return node.lazy+self.rangeAddSumQuery(node.left, lo, m)+self.rangeAddSumQuery(node.right, m+1, hi)

    """
    Range add max & query: 732, 731, 729
    """
    def rangeAddMax(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.mx += val
            node.lazy += val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, 0, node.lazy, node.lazy)
            node.right = Node(m+1, node.hi, 0, node.lazy, node.lazy)
        else:
            node.left.mx += node.lazy
            node.left.lazy += node.lazy
            node.right.mx += node.lazy
            node.right.lazy += node.lazy
        node.lazy = 0
        # update the children
        if m>=hi:
            self.rangeAddMax(node.left, val, lo, hi)
        elif m<lo:
            self.rangeAddMax(node.right, val, lo, hi)
        else:
            self.rangeAddMax(node.left, val, lo, m)
            self.rangeAddMax(node.right, val, m+1, hi)
        # update the node
        node.mx = max(node.left.mx, node.right.mx)
        return

    def rangeAddMaxQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if node.lazy!=None: return node.lazy
        if hi<=m: return node.lazy+self.rangeAddMaxQuery(node.left, lo, hi)
        elif lo>m: return node.lazy+self.rangeAddMaxQuery(node.right, lo, hi)
        else: return node.lazy+max(self.rangeAddMaxQuery(node.left, lo, m), self.rangeAddMaxQuery(node.right, m+1, hi))

    
    """
    range set sum & query: 715
    """
    def rangeSetSum(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.sm = val*(node.hi-node.lo+1)
            node.lazy = val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            if node.lazy!=None:
                node.left = Node(node.lo, m, node.lazy*(m-node.lo+1), None, node.lazy)
                node.right = Node(m+1, node.hi, node.lazy*(node.hi-m), None, node.lazy)
            else:
                node.left = Node(node.lo, m)
                node.right = Node(m+1, node.hi)
        elif node.lazy!=None:
            node.left.sm = node.lazy*(m-node.lo+1)
            node.left.lazy = node.lazy
            node.right.sm = node.lazy*(node.hi-m)
            node.right.lazy = node.lazy
        # reset lazy tag
        node.lazy = None
        # update the children
        if m>=hi:
            self.rangeSetSum(node.left, val, lo, hi)
        elif m<lo:
            self.rangeSetSum(node.right, val, lo, hi)
        else:
            self.rangeSetSum(node.left, val, lo, m)
            self.rangeSetSum(node.right, val, m+1, hi)
        # update the node
        node.sm = node.left.sm+node.right.sm
        return

    def rangeSetSumQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.sm
        m = (node.lo+node.hi)//2
        if node.lazy!=None: return node.lazy*(hi-lo+1)
        if hi<=m: return self.rangeSetSumQuery(node.left, lo, hi)
        elif lo>m: return self.rangeSetSumQuery(node.right, lo, hi)
        else: return self.rangeSetSumQuery(node.left, lo, m)+self.rangeSetSumQuery(node.right, m+1, hi)

    """
    range set max: 699
    """
    def rangeSetMax(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.mx = val
            node.lazy = val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            node.left = Node(node.lo, m, None, 0, node.lazy)
            node.right = Node(m+1, node.hi, None, 0, node.lazy)
        elif node.lazy!=None:
            node.left.mx = node.lazy
            node.left.lazy = node.lazy
            node.right.mx = node.lazy
            node.right.lazy = node.lazy
        # reset lazy tag
        node.lazy = None
        # update the children
        if m>=hi: self.rangeSetMax(node.left, val, lo, hi)
        elif m<lo: self.rangeSetMax(node.right, val, lo, hi)
        else:
            self.rangeSetMax(node.left, val, lo, m)
            self.rangeSetMax(node.right, val, m+1, hi)
        # update the node
        node.mx = max(node.left.mx, node.right.mx, node.mx)
        return

    def rangeSetMaxQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if node.lazy!=None: return node.lazy
        if hi<=m: return self.rangeSetMaxQuery(node.left, lo, hi)
        elif lo>m: return self.rangeSetMaxQuery(node.right, lo, hi)
        else: return max(self.rangeSetMaxQuery(node.left, lo, m), self.rangeSetMaxQuery(node.right, m+1, hi))
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

    def _build(self, A):
        for i in range(self.n): 
            self.T[i+self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2*i] + self.T[2*i+1]
    
    def _add(self, i, val):
        i += self.n
        diff = val - self.T[i]
        while i:
            self.T[i] += diff
            i //= 2

    def _set(self, i, val):
        i += self.n
        while i:
            self.T[i] = max(val, self.T[i])
            i //= 2
            
    def rangeSum(self, l, r):
        ans = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            if l%2: ans, l = ans+self.T[l], l+1 # if l is right child
            if not r%2: ans, r = ans+self.T[r], r-1 # if r is left child
            l, r = l//2, r//2
        return ans

    def rangeMax(self, l, r):
        ans = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            if l%2: ans, l = max(ans, self.T[l]), l+1 # if l is right child
            if not r%2: ans, r = max(ans, self.T[r]), r-1 # if r is left child
            l, r = l//2, r//2
        return ans
```

## Reference

- [花花酱 Segment Tree 线段树 - 刷题找工作 SP14](https://www.youtube.com/watch?v=rYBtViWXYeI)
- [https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches](https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches)
- [Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
- [残酷小讲座：线段树 by OTTFF](https://www.youtube.com/watch?v=s7vZDDpeR7w)