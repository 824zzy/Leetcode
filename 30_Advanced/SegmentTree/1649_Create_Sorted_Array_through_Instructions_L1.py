""" https://leetcode.com/problems/create-sorted-array-through-instructions/
Add instructions to Segment Tree on the fly,
while compute the number of elements strictly less/great than current intruction.
GET TLE, sad.
"""
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
        self.T[i] += val
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
    
    
class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        mp = {x: i for i, x in enumerate(sorted(set(A)))}
        st = SegmentTree(len(A)+1)
        ans = 0
        for i, x in enumerate(A):
            less = st.query(0, mp[x]-1)
            greater = st.query(mp[x]+1, len(A))
            ans += min(less, greater)
            st.update(mp[x], 1)
        return ans%(10**9+7)