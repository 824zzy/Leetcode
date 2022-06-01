""" https://leetcode.com/problems/falling-squares/
TODO: segment/range set modification + segment/range max query
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
    
    def rangeUpdate(self, node, val, lo, hi):
        # if node: print(node.lo, node.hi, lo, hi)
        if node.lo==lo and node.hi==hi:
            # node.mx = max(node.mx, val) # or rangeSet node.mx = val
            # node.lazy = max(node.lazy, val) # or rangeSet node.lazy = val
            node.mx = val
            node.lazy = val
            return 
        
        m = (node.lo+node.hi)//2
        # push lazy to children, if no children, create them
        if not node.left and not node.right:
            node.left = Node(node.lo, m, node.lazy, node.lazy, node.lazy)
            node.right = Node(m+1, node.hi, node.lazy, node.lazy, node.lazy)
        else:
            # node.left.mx = max(node.left.mx, node.lazy)
            # node.left.lazy = max(node.left.lazy, node.lazy)
            # node.right.mx = max(node.right.mx, node.lazy)
            # node.right.lazy = max(node.right.lazy, node.lazy)
            node.left.mx = node.lazy
            node.left.lazy = node.lazy
            node.right.mx = node.lazy
            node.right.lazy = node.lazy
        # reset lazy tag
        node.lazy = 0
        # update the children
        if m>=hi:
            self.rangeUpdate(node.left, val, lo, hi)
        elif m<lo:
            self.rangeUpdate(node.right, val, lo, hi)
        else:
            self.rangeUpdate(node.left, val, lo, m)
            self.rangeUpdate(node.right, val, m+1, hi)
        # update the node
        node.mx = max(node.left.mx, node.right.mx, node.mx)
        return
    
    def rangeMax(self, node, lo, hi):
        # if node: print(node.lo, node.hi, lo, hi, node.mx, node.lazy, node.sm)
        # print(lo, hi, node)
        
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.mx
        m = (node.lo+node.hi)//2
        
        if hi<=m: return self.rangeMax(node.left, lo, hi)
        elif lo>m: return self.rangeMax(node.right, lo, hi)
        else: 
            # return max(node.lazy, self.rangeMax(node.left, lo, m), self.rangeMax(node.right, m+1, hi))
            return max(self.rangeMax(node.left, lo, m), self.rangeMax(node.right, m+1, hi))
    
            
class Solution:
    def fallingSquares(self, A: List[List[int]]) -> List[int]:
        ans = []
        ST = SegmentTree(0, 10**9)
        for i, j in A:
            mx = ST.rangeMax(ST.root, i, i+j)
            print("range max from {} to {}: {}".format(i, i+j, mx))
            ST.rangeUpdate(ST.root, mx+j, i, i+j)
            print("global max: ", ST.root.mx)
            ans.append(ST.root.mx)
            print('----')
            
        return ans
"""
[[4,9],[8,8],[6,8],[8,2],[1,2]]
[[1,2],[2,3],[6,1]]
[[9,7],[1,9],[3,1]]
[[100,100],[200,100]]
"""
        