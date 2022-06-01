""" https://leetcode.com/problems/range-sum-query-mutable/
ZWK segment tree template
"""
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0]*2*self.n

    def build(self, A):
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
            
        
class NumArray:
    def __init__(self, nums: List[int]):
        self.ST = SegmentTree(len(nums))
        self.ST.build(nums)
        
    def update(self, index: int, val: int) -> None:
        self.ST.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.ST.rangeSum(left, right)