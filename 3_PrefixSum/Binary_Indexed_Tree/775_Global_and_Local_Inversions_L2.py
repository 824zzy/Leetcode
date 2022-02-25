""" https://leetcode.com/problems/global-and-local-inversions/
There are only two conditions:
1. If A[i-1] > A[i], then number of local inversions increase by 1.
2. Number of global inversions += number of elements greater than A[i] so far through: i-bit.get(x)
"""

class BIT:
    def __init__(self, n):
        self.A = [0] * (n+1)
    
    def get(self, k):
        k += 1
        sm = 0
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
    def isIdealPermutation(self, A: List[int]) -> bool:
        G, L = 0, 0
        bit = BIT(len(A))
        for i, x in enumerate(A):
            if i and A[i-1]>A[i]: L += 1
            G += i-bit.get(x)
            bit.add(x, 1)
        return G==L