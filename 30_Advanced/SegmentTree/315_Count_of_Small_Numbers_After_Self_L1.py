""" https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Reverse the array and compute the smaller element count of current element by indexes and segment tree.
"""
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