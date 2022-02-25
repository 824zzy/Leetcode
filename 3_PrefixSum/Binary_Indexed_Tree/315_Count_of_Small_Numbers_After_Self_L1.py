""" https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Reverse the array and compute the smaller element count of current element by indexes and fenwick tree.
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
            

class Solution:
    def countSmaller(self, A: List[int]) -> List[int]:
        mp = {x: i for i, x in enumerate(sorted(set(A)))}
        bit = BIT(len(mp))
        ans = []
        for x in reversed(A): 
            ans.append(bit.get(mp[x]-1))
            bit.add(mp[x], 1)
        return ans[::-1]