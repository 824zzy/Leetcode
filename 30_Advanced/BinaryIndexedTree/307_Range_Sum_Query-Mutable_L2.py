""" https://leetcode.com/problems/range-sum-query-mutable/
"""
class BIT:
    def __init__(self, n):
        self.A = [0] * (n+1)
    
    def get(self, k):
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
            

class NumArray:
    def __init__(self, A: List[int]):
        self.A = A
        self.bit = BIT(len(A))
        for i, x in enumerate(A):
            self.bit.add(i, x)

    def update(self, k: int, x: int) -> None:
        self.bit.add(k, x-self.A[k])
        self.A[k] = x
        
    def sumRange(self, l: int, r: int) -> int:
        return self.bit.get(r)-self.bit.get(l-1)
