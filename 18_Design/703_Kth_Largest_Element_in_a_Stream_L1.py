# Google
from bisect import *
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        
    def add(self, val: int) -> int:
        insort(self.nums, val)
        if self.k>len(self.nums):
            return -1
        return self.nums[-self.k]