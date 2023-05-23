""" https://leetcode.com/problems/top-k-frequent-elements/
1. apply quick select on element frequencies to find lower bound of top k frequent elements.
2. use Counter to find valid keys.
"""
from header import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        A = list(cnt.values())
        
        def partition(l, r): 
            """Return partition of A[l:r]."""
            i, j = l+1, r-1
            while i <= j: 
                if A[i] < A[l]: i += 1
                elif A[j] > A[l]: j -= 1
                else: 
                    A[i], A[j] = A[j], A[i]
                    i, j = i+1, j-1
            A[l], A[j] = A[j], A[l]
            return j
        
        shuffle(A)
        l, r = 0, len(A)
        while True: 
            m = partition(l, r)
            if m+k < len(A): l = m + 1
            elif m+k == len(A): break
            else: r = m
        
        return [key for key, val in cnt.items() if val>=A[m]]


# hash table solution
class Solution:
    def topKFrequent(self, A: List[int], k: int) -> List[int]:
        cnt = Counter(A)
        return [x for x, _ in sorted(cnt.items(), key=lambda x: -x[1])][:k]