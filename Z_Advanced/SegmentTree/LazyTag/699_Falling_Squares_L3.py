""" https://leetcode.com/problems/falling-squares/
segment tree range set and query range set's max
"""
class Node:
    def __init__(self, lo, hi, sm=0, mx=0, lazy=0):
        self.lo = lo
        self.hi = hi
        self.sm = sm # range sum
        self.mx = mx # range max
        self.lazy = lazy # lazy propagation for range update
        self.left = None
        self.right = None
        
class SegmentTree:
    def __init__(self, lo, hi, A=[]):
        self.root = Node(lo, hi)
    
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
    
    def rangeSetMax(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if hi<=m: return max(node.lazy, self.rangeSetMax(node.left, lo, hi))
        elif lo>m: return max(node.lazy, self.rangeSetMax(node.right, lo, hi))
        else: return max(node.lazy, self.rangeSetMax(node.left, lo, m), self.rangeSetMax(node.right, m+1, hi))
    
            
class Solution:
    def fallingSquares(self, A: List[List[int]]) -> List[int]:
        ans = []
        ST = SegmentTree(0, 10**9)
        for i, j in A:
            mx = ST.rangeSetMax(ST.root, i, i+j-1)
            ST.rangeSet(ST.root, mx+j, i, i+j-1)
            ans.append(ST.root.mx)
        return ans
"""
[[3,2],[8,3],[1,4],[8,10],[9,3]]
[[6,1],[9,2],[2,4]]
[[4,9],[8,8],[6,8],[8,2],[1,2]]
[[1,2],[2,3],[6,1]]
[[9,7],[1,9],[3,1]]
[[100,100],[200,100]]
"""
        