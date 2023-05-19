""" https://leetcode.com/problems/create-sorted-array-through-instructions/
Add instructions to BIT on the fly,
while compute the number of elements strictly less/great than current intruction
"""
class BIT:
    def __init__(self, n):
        self.A = [0] * (n+1)
    
    def sum(self, k):
        sm = 0
        k += 1
        while k:
            sm += self.A[k]
            k -= k & -k
        return sm
    
    def add(self, k, x):
        k += 1
        while k<len(self.A):
            self.A[k] += x
            k += k & -k
            

class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        bit = BIT(max(A)+1)
        ans = 0
        for i, x in enumerate(A):
            ans += min(bit.sum(x-1), i-bit.sum(x))
            bit.add(x, 1)
        return ans % (10**9+7)