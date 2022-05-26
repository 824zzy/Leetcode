# Segment Tree

There are two types of segment tree implementations: array based and tree based.

1. Array based segment tree
   1. init: initiate leaves and nodes, O(n)
   2. update: update values from leave to root, O(logn)
   3. query: O(logn+k)

## Property

Suppose we have a segment tree with `N` leaves:

1. At most `log(N)` layers
2. `2N-1` segments(nodes)
3. Given root index = `[1]`, for each node `o`, its left child index is `o*2`, its right child index is `o*2+1`
4. Given root index = `[1]`, the i-th leaf index is `N+i`

``` py
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0]*2*self.n
            
    def build(self, A):
        for i in range(self.n):
            self.T[i+self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2*i]+self.T[2*i+1]
    
    def update(self, i, val):
        """ set i-th node to val
        """
        # find index of leaf
        i += self.n
        self.T[i] = val # self.T[i] += val
        # update values from leaf to root
        while i:
            if i%2: l, r = i-1, i
            else: l, r = i, i+1
            self.T[i//2] = self.T[l]+self.T[r]
            i //= 2
    
    def query(self, l, r):
        ans = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            # if l is right child
            if l%2: ans, l = ans+self.T[l], l+1
            # if r is left child
            if not r%2: ans, r = ans+self.T[r], r-1
            l, r = l//2, r//2
        return ans
```

## Reference

- [花花酱 Segment Tree 线段树 - 刷题找工作 SP14](https://www.youtube.com/watch?v=rYBtViWXYeI)
- [https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches](https://leetcode.com/problems/range-sum-query-mutable/discuss/1205304/Python3-4-approaches)
- [Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
- [残酷小讲座：线段树 by OTTFF](https://www.youtube.com/watch?v=s7vZDDpeR7w)