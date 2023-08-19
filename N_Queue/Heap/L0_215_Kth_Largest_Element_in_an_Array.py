""" https://leetcode.com/problems/kth-largest-element-in-an-array/
nlargest usage of heapq
"""
from header import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        return nlargest(k, nums)[-1]

# O(n) solution via heapq
class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        A = [-x for x in A]
        heapify(A)
        for _ in range(k):
            x = heappop(A)
        return -x