""" https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Reverse the array and compute the smaller element count of current element by indexes and segment tree.

Segment tree type: discretization + single point add + range sum query
"""
# Tree-based segment tree
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
    
    def _sumQuery(self, node, lo, hi):
        if not node: return 0
        if node.lo==lo and node.hi==hi: return node.sm
        m = (node.lo+node.hi)//2
        if hi<=m: return self._sumQuery(node.left, lo, hi)
        elif lo>m: return self._sumQuery(node.right, lo, hi)
        else: return self._sumQuery(node.left, lo, m)+self._sumQuery(node.right, m+1, hi)
        

class Solution:
    def countSmaller(self, A: List[int]) -> List[int]:
        mp = {x: i for i, x in enumerate(sorted(set(A)))}
        st = SegmentTree(0, len(mp)-1)
        ans = []
        for x in reversed(A):
            ans.append(st._sumQuery(st.root, 0, mp[x]-1))
            st._add(st.root, mp[x], 1)
        return ans[::-1]


# ZKW segment tree
class ST:
    def __init__(self, n):
        self.n = n
        self.T = [0]*2*self.n
            
    def build(self, A):
        for i in range(self.n):
            self.T[i+self.n] = A[i]
        for i in reversed(range(self.n)):
            self.T[i] = self.T[2*i]+self.T[2*i+1]
    
    def update(self, i, val):
        i += self.n
        self.T[i] += val
        while i:
            if i%2: l, r = i-1, i
            else: l, r = i, i+1
            self.T[i//2] = self.T[l]+self.T[r]
            i //= 2
    
    def query(self, l, r):
        ans = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            if l%2: ans, l = ans+self.T[l], l+1
            if not r%2: ans, r = ans+self.T[r], r-1
            l, r = l//2, r//2
        return ans
    
class Solution:
    def countSmaller(self, A: List[int]) -> List[int]:
        mp = {x: i for i, x in enumerate(sorted(set(A)))}
        st = ST(len(mp))
        
        ans = []
        for x in reversed(A):
            ans.append(st.query(0, mp[x]-1))
            st.update(mp[x], st.T[mp[x]]+1)
        return ans[::-1]