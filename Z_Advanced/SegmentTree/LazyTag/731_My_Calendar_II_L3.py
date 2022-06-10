""" https://leetcode.com/problems/my-calendar-ii/
Even though sweep line is a more efficient solution, segment tree with lazy tag is also available.

Range max add + range max query
"""
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
        
    def rangeAdd(self, node, val, lo, hi):
        if node.lo==lo and node.hi==hi:
            node.mx += val # or rangeSet node.sm = val
            node.lazy += val # or rangeSet node.lazy = val
            return 

        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them on the fly
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, node.lazy, node.lazy)
            node.right = Node(m+1, node.hi, node.lazy, node.lazy, node.lazy)
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
        node.mx = max(node.left.mx, node.right.mx, node.mx)
        return

    def rangeAddMax(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        if m>=hi: return node.lazy+self.rangeAddMax(node.left, lo, hi)
        elif m<lo: return node.lazy+self.rangeAddMax(node.right, lo, hi)
        else: return node.lazy+max(self.rangeAddMax(node.left, lo, m), self.rangeAddMax(node.right, m+1, hi))
    
        
class MyCalendarTwo:
    def __init__(self):
        self.ST = SegmentTree(0, 10**9)

    def book(self, lo: int, hi: int) -> bool:
        rangemx = self.ST.rangeAddMax(self.ST.root, lo, hi-1)
        if rangemx==2: return False
        self.ST.rangeAdd(self.ST.root, 1, lo, hi-1)
        return True

"""
["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
[[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
["MyCalendarTwo","book","book","book","book","book","book"]
[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
[[],[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
"""
        